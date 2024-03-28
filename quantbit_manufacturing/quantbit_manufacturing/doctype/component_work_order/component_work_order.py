# Copyright (c) 2024, Quantbit Technologies Pvt. Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

def gatevalue(value):
	return value if value else 1

def getval(value):
	return value if value else 0

class ComponentWorkOrder(Document):

	# Fetch Child table from Component Manifest doctype to Component Work Order Doctype
	@frappe.whitelist()
	def get_raw_materials(self):
		if self.finished_item_code:
			doc_name = frappe.get_value('Component Manifest',{'finished_item_code': self.finished_item_code, "enable": True}, "name")
			if doc_name:
				doc = frappe.get_doc('Component Manifest', doc_name)
				
				self.finished_item_group = doc.finished_item_group				
				self.append('finished_item_details',{
					'item_code':doc.finished_item_code,
					'item_name':doc.finished_item_name,
					'qty':doc.quantity_to_manufacturing,
					'component_manifest':doc.name,
				})
				for d in doc.get("raw_materials"):
					self.append('component_raw_item', {	
						"item_code": d.item_code,
						"item_name": d.item_name,
						"quantity": d.quantity,
						"actual_quantity":d.quantity,
						"percentage_input":d.percentage_input,
						"uom": d.uom,
						"check":d.check,
						"total": d.total,
					})
					
				self.get_default_warehouse()
				self.set_source_warehouse()
				self.available_qty()

								
			else:
				frappe.throw(("Component Manifest not found for item code {0}").format(self.finished_item_code))

	# After adding entry in finished item details child table
	@frappe.whitelist()
	def get_manifest_raw_mate(self):
		for i in self.get("finished_item_details"):
			doc_name = frappe.get_value('Component Manifest', {'finished_item_code': i.item_code, "enable": True}, "name")
			if doc_name:
				doc = frappe.get_doc('Component Manifest', doc_name)
				i.qty = doc.quantity_to_manufacturing
				i.component_manifest = doc.name
				for d in doc.get("raw_materials"):
					existing_entry = self.get_existing_entry(d.item_code)
					if existing_entry:
						existing_entry.actual_quantity += float(d.quantity)
						existing_entry.percentage_input += float(d.percentage_input)
					else:
						self.append('component_raw_item', {    
							"item_code": d.item_code,
							"item_name": d.item_name,
							"actual_quantity": d.quantity,
							"percentage_input": d.percentage_input,
							"uom": d.uom,
							"check": d.check,
							"total": d.total,
							"finished_item_name": doc.finished_item_code,
							'reference_id': i.name,
							'used_quantity': getval(i.updatedqty) * d.quantity,
							'quantity': gatevalue(i.updatedqty) * d.quantity
						})

				self.set_source_warehouse()
				self.available_qty()

			if i.item_code and not doc_name:
				frappe.throw("Component Manifest not found for item code")

	def get_existing_entry(self, item_code):
		for entry in self.component_raw_item:
			if entry.item_code == item_code:
				return entry
		return None


	# Calculate Available Quantity in source warehouse In Component Raw Item			
	@frappe.whitelist()
	def available_qty(self):
		for row in self.get("component_raw_item"):
			if row.source_warehouse and row.item_code:
				doc_name = frappe.get_value('Bin',{'item_code':row.item_code,'warehouse': row.source_warehouse}, "actual_qty")
				row.available_qty = doc_name


	#Calculate Updated Quantity depends on OK Quantity and Rejected Quantity fields on form *fields are hidden*
	@frappe.whitelist()
	def calculate_Updated_quantity(self):
		self.updated_quantity_to_manufacturing = self._calculate_total(self.ok_quantity, self.rejected_quantity)
		self.calculate_quantity_in_component_row_item()
	
	def _calculate_total(self, *values):
		return sum(value for value in values if value is not None)


	# Calculate Quantity and Used Quantity In Component Raw Item depends on OK Quantity and Rejected Quantity fields on form *fields are hidden*		
	@frappe.whitelist()
	def calculate_quantity_in_component_row_item(self):
		for row in self.get("component_raw_item"):
			row.quantity = (self.updated_quantity_to_manufacturing * row.actual_quantity)/self.quantity_to_manufacturing
			row.used_quantity = (self.updated_quantity_to_manufacturing * row.actual_quantity)/self.quantity_to_manufacturing



	#Calculate Uquantity depends on OK Quantity and Rejected Quantity in child table
	@frappe.whitelist()
	def calculate_Uquantity(self):
		for i in self.get("finished_item_details"):
			i.updatedqty = self._calculate_total(i.okqty, i.rejqty)
		self.quantity_in_cri_from_fid()
			
		
	def _calculate_total(self, *values):
		return sum(value for value in values if value is not None)


	# Calculate Quantity and Used Quantity In Component Raw Item from child table ok and rejected qty			
	@frappe.whitelist()
	def quantity_in_cri_from_fid(self):
		for row in self.get("component_raw_item"):
			quantity = 0
			for i in self.get("finished_item_details"):
				if i.component_manifest :
					quantity_to_manufacturing = gatevalue(frappe.get_value("Component Manifest",i.component_manifest ,'quantity_to_manufacturing'))
					doc = frappe.get_all('Raw Materials for Component Manifest' , filters = {'parent':i.component_manifest , 'item_code': row.item_code} , fields = ['quantity'])
					for d in doc:
						quantity = quantity + ((getval(d.quantity) / getval(quantity_to_manufacturing)) * getval(i.updatedqty))

			row.actual_quantity = quantity
			row.used_quantity = quantity
				# row.used_quantity = (i.updatedqty * row.actual_quantity)/i.qty



	# If Source Warehouse is same for all Raw Item then Set selected source warehouse for all child entries
	@frappe.whitelist()
	def set_source_warehouse(self):
		if self.source_warehouse:
			for i in self.get('component_raw_item'):			
				i.source_warehouse = self.source_warehouse
   
    
    # calculating power consumption
	@frappe.whitelist()
	def calculating_power_consumption(self):
		if self.power_reading_initial and  self.power_reading_final:
			self.power_consumed = self.power_reading_final - self.power_reading_initial
			if self.power_consumed < 0 :
				frappe.throw("The 'Power Consumed' should not be negative")

	
	# get scrap quantity based on percentage input and checked component raw item 
	@frappe.whitelist()
	def get_quantity_per(self):
		total = sum(i.used_quantity for i in self.get('component_raw_item') if i.check)
		percentage_items = [i for i in self.get('scrap_items') if i.percentage_input]
		for i in percentage_items:
			i.used_quantity = (i.percentage_input * total) / 100


	# calculate used quantity depends on percentage input in component raw item and scrap items child table 
	@frappe.whitelist()
	def get_quantity_compo(self):
		total = sum(i.quantity for i in self.get('component_raw_item') if i.check)
		percentage_items = [i for i in self.get('component_raw_item') if i.percentage_input]
		for i in percentage_items:
			i.used_quantity = (i.percentage_input * total) / 100


	# To Set Default Warehouse from Foundry Setting
	@frappe.whitelist()
	def get_default_warehouse(self):
		warehouse = frappe.get_value('Foundry Setting',{'name': self.company}, "name")
		if warehouse:
			doc = frappe.get_doc('Foundry Setting', warehouse)
			self.source_warehouse = doc.default_source_warehouse
			self.target_warehouse = doc.default_target_warehouse
		

	def on_submit(self):
		self.Manufacturing_stock_entry()
		self.mi_stock_entry_scrap_details()



	# After Submitting Component Work Order Manufacturing Stock Entry will be created 
	@frappe.whitelist()
	def Manufacturing_stock_entry(self):
		total = sum(i.updatedqty for i in self.get('finished_item_details') if i.updatedqty)
		for f in self.get("finished_item_details"):
			doc = frappe.new_doc("Stock Entry")
			doc.stock_entry_type = "Manufacture"
			doc.company = self.company
			doc.posting_date =self.posting_date
			doc.append("items", {
				"item_code": f.item_code,
				"qty": f.okqty,
				"t_warehouse": self.target_warehouse,
				"is_finished_item": True,
			})
			
			for i in self.get("component_raw_item"):	
				doc.append("items", {
					"s_warehouse": i.source_warehouse,
					"item_code": i.item_code,
					"item_name": i.item_name,
					"qty": (f.updatedqty *  i.used_quantity)/total ,
				})
			
			for j in self.get("operational_cost"):
				doc.append("additional_costs", {
					"expense_account": j.operations,
					"description": j.description,
					"amount":(f.updatedqty *  j.cost )/total,
				})

			doc.custom_component_work_order = self.name
			doc.insert()
			doc.save()
			doc.submit()


	# After Submitting Component Work Order Material Issue Stock Entry of Scrap Information will be created 
	@frappe.whitelist()
	def mi_stock_entry_scrap_details(self):
		doc = frappe.new_doc("Stock Entry")
		doc.stock_entry_type = "Material Issue"
		doc.company = self.company
		doc.posting_date =self.posting_date
		for i in self.get("scrap_items"):
			doc.append("items", {
				"s_warehouse": i.source_warehouse,
				"item_code": i.item_code,
				"item_name": i.item_name,
				"qty": i.used_quantity,
			})
		if doc.items:
			doc.custom_component_work_order = self.name
			doc.insert()
			doc.save()
			doc.submit()


	
	