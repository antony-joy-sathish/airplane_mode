import frappe
from frappe.utils import nowdate, add_days

def send_rent_reminders():
    config = frappe.get_single("Shop Configuration")
    if not config.enable_reminder:
        return

    due_shops = frappe.get_all("Shop", filters={"status": "Occupied"}, fields=["name", "tenant", "rent_amount", "lease_expiry"])
    for shop in due_shops:
        tenant = frappe.get_doc("Tenant", shop.tenant)
        message = f"Dear {tenant.tenant_name}, your rent of ₹{shop.rent_amount} for shop {shop.name} is due."
        frappe.sendmail(recipients=[tenant.email], subject="Rent Reminder", message=message)
