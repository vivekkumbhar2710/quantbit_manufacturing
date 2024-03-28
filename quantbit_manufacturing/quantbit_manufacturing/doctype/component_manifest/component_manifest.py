# Copyright (c) 2024, Quantbit Technologies Pvt. Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ComponentManifest(Document):


	@frappe.whitelist()
	def get_quantity_per(self):
		total = sum(i.quantity for i in self.get('raw_materials') if i.check)
		percentage_items = [i for i in self.get('raw_materials') if i.percentage_input]

		for i in percentage_items:
			i.quantity = (i.percentage_input * total) / 100







	