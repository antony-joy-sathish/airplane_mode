// Copyright (c) 2025, deepak and contributors
// For license information, please see license.txt

frappe.pages['revenue-dashboard'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Revenue Dashboard',
        single_column: true
    });

    // Create chart container
    $(frappe.render_template("<div id='revenue_chart'></div>", {})).appendTo(page.body);

    // Fetch revenue data via frappe.call
    frappe.call({
        method: "frappe.client.get_list",
        args: {
            doctype: "Airplane Ticket",
            fields: ["flight", "total_amount"],
            filters: { status: "Booked" }
        },
        callback: function(r) {
            if (!r.message) return;

            // Group revenue by flight
            let revenueMap = {};
            r.message.forEach(row => {
                if (!revenueMap[row.flight]) {
                    revenueMap[row.flight] = 0;
                }
                revenueMap[row.flight] += row.total_amount;
            });

            // Prepare chart data
            let labels = Object.keys(revenueMap);
            let values = Object.values(revenueMap);

            // Render chart
            new frappe.Chart("#revenue_chart", {
                data: {
                    labels: labels,
                    datasets: [
                        {
                            name: "Total Revenue",
                            values: values
                        }
                    ]
                },
                type: "donut", // or "bar", "line"
                height: 300,
                colors: ["#7cd6fd", "#743ee2", "#ffa3ef", "#ffd700"]
            });
        }
    });
};
