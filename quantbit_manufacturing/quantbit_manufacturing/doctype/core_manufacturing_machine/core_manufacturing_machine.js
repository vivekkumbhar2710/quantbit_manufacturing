// Copyright (c) 2024, Quantbit Technologies Pvt. Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Core Manufacturing Machine', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Core Manufacturing Machine', {
	refresh: function (frm) {
		frm.set_query("core_type", function () { // Replace with the name of the link field
			return {
				filters: [
					["Core Type", "company", '=', frm.doc.company] // Replace with your actual filter criteria
				]
			};
		});
	}
});