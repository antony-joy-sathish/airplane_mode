# Copyright (c) 2025, deepak and contributors
# For license information, please see license.txt
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator):   # ✅ Use WebsiteGenerator if you want it as a webpage
    def on_submit(self):
        # When flight is submitted → mark as completed
        self.status = "Completed"
        frappe.msgprint(f"✈️ Flight {self.name} marked as Completed")

    def get_context(self, context):
        # Show sidebar on flight detail page
        context.show_sidebar = True

        # Format duration if available
        total_seconds = int(self.duration or 0)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        duration_parts = []
        if hours > 0:
            duration_parts.append(f"{hours}h")
        if minutes > 0:
            duration_parts.append(f"{minutes}m")
        if seconds > 0:
            duration_parts.append(f"{seconds}s")

        context.flight_duration = " ".join(duration_parts) if duration_parts else "N/A"

        return context

    def get_page_info(self):
        return {
            "title": f"Flight {self.name}",
            "route": self.name.lower(),
            "context": {"doc": self}
        }
