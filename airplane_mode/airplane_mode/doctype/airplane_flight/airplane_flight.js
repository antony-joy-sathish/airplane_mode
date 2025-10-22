// Copyright (c) 2025, deepak and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
    airplane(frm) {
        if (frm.doc.airplane) {
           frm.set_value("route", "/flights/" + (frm.doc.airplane || "").toLowerCase().replace(/\s+/g, "-"));
        }
    }
});

