import frappe

def execute():
    # Fetch all tickets without a seat
    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"seat": ["is", "not set"]},
        fields=["name", "seat"]
    )

    for t in tickets:
        seat_value = f"S-{t.name}"

        frappe.db.set_value("Airplane Ticket", t.name, "seat", seat_value)

    frappe.db.commit()
