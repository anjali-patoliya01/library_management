# Copyright (c) 2024, anju and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class client_side_scripting(Document):
	pass


@frappe.whitelist()
def frappe_call(msg):
	# import time
	# time.sleep(5)
	# frappe.msgprint(msg)

	return 'hii this message from frm_call'