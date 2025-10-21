frappe.ready(function() {
    const urlParams = new URLSearchParams(window.location.search);

    let flight = urlParams.get("flight");
    let flight_price = urlParams.get("flight_price");

    // Auto set Flight
    if (flight) {
        frappe.web_form.set_value("flight", flight);
    }

    // Auto set Price (Read Only)
    if (flight_price) {
        frappe.web_form.set_value("flight_price", flight_price);
    }
});
