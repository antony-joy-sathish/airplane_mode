# Copyright (c) 2025, deepak and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Shop(WebsiteGenerator):
	def before_save(self):
		self.route = f"shops/{self.name.lower().replace(' ','-')}"

	def validate(self):
		# Validate lease dates
		if self.lease_start_date and self.lease_expiry_date:
			if self.lease_start_date >= self.lease_expiry_date:
				frappe.throw("Lease Expiry Date must be greater than Lease Start Date")

		# Validate rent amount
		shop_config = frappe.get_single("Shop Configuration")
		default_rent = shop_config.default_rent

		if self.rent_amount is not None and self.rent_amount < default_rent:
			frappe.throw(f"Rent amount must be greater than or equal to the default rent: {default_rent}")
