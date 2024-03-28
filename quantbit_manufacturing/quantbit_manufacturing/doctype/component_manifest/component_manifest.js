// Copyright (c) 2024, Quantbit Technologies Pvt. Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Component Manifest', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Raw Materials for Component Manifest', {
	check: function(frm) {
		frm.call({
			method:'get_quantity_per',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Raw Materials for Component Manifest', {
	percentage_input: function(frm) {
		frm.call({
			method:'get_quantity_per',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Raw Materials for Component Manifest', {
	quantity: function(frm) {
		frm.call({
			method:'get_quantity_per',
			doc:frm.doc
		})
	}
});


frappe.ui.form.on('Component Manifest', {
    setup: function(frm) {
        frm.set_query("finished_item_code", function(doc) {
            if (frm.doc.finished_item_group) {
                return {
                    filters: [
                        ['Item', 'item_group', '=', frm.doc.finished_item_group],
                    ]
                };
            } else {
               
                return {};
            }
        });
    },
});


frappe.ui.form.on('Component Manifest', {
	setup: function(frm) {
		
			frm.set_query("item_code", "raw_materials", function(doc, cdt, cdn) {
				let d = locals[cdt][cdn];
				if(frm.doc.core_type){
					return {
						filters: {
							'custom_core_type':frm.doc.core_type,
						}
					};
				}
						
			})
	
    },
});
