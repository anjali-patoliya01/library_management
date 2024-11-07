// Copyright (c) 2024, anju and contributors
// For license information, please see license.txt

frappe.query_reports["server_side_scripting_Script_report"] = {
	filters: [
		{
			"fieldname": "name",
			"label": __("server_side_scripting"),
			"fieldtype": "Link",
			"options": "server_side_scripting",
		},

		{
			"fieldname": "dob",
			"label": __("DOB"),
			"fieldtype": "Date",
			// "options": "server_side_scripting",
		},

		{
			"fieldname": "age",
			"label": __("Age"),
			"fieldtype": "Data",
		},
	],
};
