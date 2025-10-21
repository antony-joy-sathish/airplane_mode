# Copyright (c) 2025, deepak and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):

    def before_insert(self):
        """Assign a random seat if not set."""
        if not self.seat:
            seat_number = random.randint(1, 99)
            seat_letter = random.choice(["A", "B", "C", "D", "E"])
            self.seat = f"{seat_number}{seat_letter}"

            frappe.logger().info(f"🎫 Assigned seat: {self.seat}")
            frappe.msgprint(
                msg=f"🎫 Ticket created successfully. Assigned Seat: {self.seat}",
                title="Success",
                indicator="green"
            )

    def validate(self):
        """Validate add-ons, calculate total, and check capacity."""

        # 1️⃣ Add-ons validation (no duplicates)
        addons = [d.item for d in self.add_ons]
        if len(addons) != len(set(addons)):
            duplicates = [x for x in addons if addons.count(x) > 1]
            duplicates = list(set(duplicates))
            frappe.throw(f"Add-ons item(s) already selected: {', '.join(duplicates)}. Kindly remove duplicates.")

        # 2️⃣ Total amount calculation
        addons_total = sum(d.amount for d in self.add_ons)
        self.total_amount = (self.flight_price or 0) + addons_total

        # 3️⃣ Seat capacity check
        if self.flight:  # assuming you have a Link field "flight" in Ticket
            flight = frappe.get_doc("Airplane Flight", self.flight)

            if not flight.airplane:
                frappe.throw("This flight has no airplane assigned.")

            airplane = frappe.get_doc("Airplane", flight.airplane)

            # Count tickets already booked for this flight
            ticket_count = frappe.db.count(
                "Airplane Ticket",
                {"flight": self.flight}
            )

            if ticket_count >= airplane.capacity:
                frappe.throw(
                    f"❌ Cannot create ticket. Airplane {airplane.name} "
                    f"has only {airplane.capacity} seats, which are already booked."
                )

    def on_submit(self):
        """Only allow submission if status = Boarded."""
        if self.status != "Boarded":
            frappe.throw("Only Boarded tickets can be submitted", frappe.ValidationError)