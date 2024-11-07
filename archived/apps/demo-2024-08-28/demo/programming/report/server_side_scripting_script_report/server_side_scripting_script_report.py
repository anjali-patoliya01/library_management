# Copyright (c) 2024, anju and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe import msgprint


def execute(filters=None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	if not filters: 
		filters={}
	

	columns = get_columns()
	data = get_data(filters)

	if not data:
		msgprint(_("No record found"))

	all_data = []
	for d in data:
		row = {
			'first_name': d.first_name,
			'dob': d.dob,
			'age': d.age
		}
		all_data.append(row)

	chart = get_chart_data(all_data)
	report_summary = get_report_summary(all_data)

	return columns, all_data, None , chart, report_summary


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Name"),
			"fieldname": "first_name",
			"fieldtype": "Data",
			"width" : '120'
		},
		{
			"label": _("DOB"),
			"fieldname": "dob",
			"fieldtype": "Date",
			"width" : '120'
		},
		{
			"label": _("Age"),
			"fieldname": "age",
			"fieldtype": "Data",
			"width" : '100'
		},
	]


def get_data(filters) -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = 'server_side_scripting',
		fields = ['first_name', 'dob', 'age'],
		filters = conditions,
		order_by = 'first_name'
	)
	return data
	



def get_conditions(filters):
	"""Return conditions based on filters."""
	conditions = {}
	for key, value in filters.items():
		if value:
			conditions[key] = value

	return conditions


def get_chart_data(all_data):
	""" Use to get pie chart """

	if not all_data:
		return None

	labels = ['age <= 45', 'age > 45']

	age_data ={
		'age <= 45' : 0,
		'age > 45' : 0,
	}
	datasets = []

	for entry in all_data:
		age = entry.get('age') 
		if age is not None:
			if age <= 45:
				age_data['age <= 45'] += 1
			else:
				age_data['age > 45'] += 1
	
	datasets.append({
		'name' : 'Age Status',
		'values' : [age_data.get('age <= 45'), age_data.get('age > 45')]
	})

	chart = {
		'all_data' :{
			'labels': labels,
			'datasets': datasets
		},
		'type' : 'bar',
		'height' : 300
	}

	return chart





def get_report_summary(all_data):
	if not all_data:
		return None

	age_below_45, age_above_45 = 0, 0

	for entry in all_data:
		age = entry.get('age')
		if age is not None: 
			if age <= 45:
				age_below_45 += 1
			else:
				age_above_45 += 1

	return [
		{
			'value': age_below_45,
			'indicator' : "Green",
			'labels' : 'Age below 45',
			'datatype' : 'Int',
		},
		{
			'value': age_above_45,
			'indicator' : "Red",
			'labels' : 'Age Above 45',
			'datatype' : 'Int',
		},
	]
