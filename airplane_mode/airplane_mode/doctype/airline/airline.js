// Copyright (c) 2025, deepak and contributors
// For license information, please see license.txt
frappe.ui.form.on("Airline", {
    onload: function (frm) {
        if (frm.doc.website && frm.doc.website.trim() !== "") {
            // remove duplicates manually
            let link_label = "See Official Website";
            let already_added = frm.page.web_links.some(link => link.label === link_label);

            if (!already_added) {
                frm.add_web_link(frm.doc.website, link_label);
            }
        }
    },

    website: function (frm) {
        if (frm.doc.website && frm.doc.website.trim() !== "") {
            // remove old link first
            frm.page.web_links = [];
            frm.add_web_link(frm.doc.website, "See Official Website");
        }
    },

    bbefore_save: function (frm) {
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


