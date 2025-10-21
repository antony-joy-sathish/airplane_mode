// Copyright (c) 2025, deepak and contributors
// For license information, please see license.txt


frappe.ui.form.on("Airplane Ticket", {
    refresh: function (frm) {
        // Add custom button
        frm.add_custom_button("Assign Seat", () => {
            // Create dialog
            let d = new frappe.ui.Dialog({
                title: "Assign Seat",
                fields: [
                    {
                        label: "Seat Number",
                        fieldname: "seat_number",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],
                primary_action_label: "Assign",
                primary_action(values) {
                    frm.set_value("seat", values.seat_number);  // Set value in form
                    frm.save(); // optional: auto save after assignment
                    d.hide();
                }
            });
            d.show();
        });
    },


    enable: function (frm) {

        let row = frm.add_child('add_ons', {

            item: "Demo",
            amount: "200.00"
        })
        frm.refresh_field('add_ons')
    }
});



