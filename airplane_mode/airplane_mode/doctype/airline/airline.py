# Copyright (c) 2025, deepak and contributors
# For license information, please see license.txt

import frappe
import time
from frappe.model.document import Document

class Airline(Document):
    
    def before_save(self):
        old_doc = self.get_doc_before_save()
        if old_doc and self.headquarters == old_doc.headquarters:
            frappe.msgprint("Both are same")
        else:
            frappe.msgprint("Not same")

@frappe.whitelist()
def fake_progress():
    # no real long task, just send final result
    return {"progress": 100, "msg": "Saved successfully ✅"}




