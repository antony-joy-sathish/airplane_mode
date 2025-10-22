// Copyright (c) 2025, deepak and contributors
// For license information, please see license.txt
frappe.ui.form.on("Airline", {
    onload: function (frm) {
        add_website_link(frm);
    },

    before_save: function (frm) {
        frappe.call({
            method: "airplane_mode.airplane_mode.doctype.airline.airline.long_task",
            callback: function (r) {
                if (r.message) {
                    frappe.msgprint(r.message);
                }
            }
        });
    }
});

function add_website_link(frm) {
    if (!frm.doc.website || frm.doc.website.trim() === "") return;

    // remove all existing web links first
    frm.page.web_links = [];

    // now add one clean link
    frm.add_web_link(frm.doc.website, "See Official Website");
}



