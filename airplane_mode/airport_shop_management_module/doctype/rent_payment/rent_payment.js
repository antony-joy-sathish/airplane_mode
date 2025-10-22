// Copyright (c) 2025, deepak and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rent Payment", {
    // Trigger when cost or amount_paid changes
    cost: function(frm) {
        calculate_remaining(frm);
    },

    amount_paid: function(frm) {
        calculate_remaining(frm);
    }
});

// Helper function
function calculate_remaining(frm) {
    const cost = frm.doc.cost || 0;
    const amount_paid = frm.doc.amount_paid || 0;
    const remaining = cost - amount_paid;

    frm.set_value('remaining', remaining);
    if (remaining == 0){
        frm.set_value("payment_status", "Paid")
    }else{
        frm.set_value("payment_status", "Pending")
    }
}

