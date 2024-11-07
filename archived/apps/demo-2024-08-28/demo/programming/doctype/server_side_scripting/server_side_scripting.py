# Copyright (c) 2024, anju and contributors
# For license information, please see license.txt
from frappe import _
import frappe
from frappe.model.document import Document


############################################################
######                 EVENTS                         ######
############################################################

# class server_side_scripting(Document):

	# def validate(self):
	# 	frappe.msgprint("Hello Frappe from 'validate' event")


	# def before_save(self):
	# 	frappe.throw("Hello Frappe from 'before_save' event")

	
	# def before_insert(self):
	# 	frappe.throw("Hello Frappe from 'before_insert' event")
	

	# def after_insert(self):
	# 	frappe.throw("Hello Frappe from 'after_insert' event")


	# def on_update(self):
	# 	frappe.msgprint("Hello Frappe from 'on_update' event")

	
	# def before_submit(self):
		# frappe.msgprint("Hello Frappe from 'before_submit' event")

	
	# def on_submit(self):
	# 	frappe.msgprint"Hello Frappe from 'on_submit' event")


	# def on_cancel(self):
	# 	frappe.msgprint("Hello Frappe from 'on_cancel' event")
	

	# def on_trash(self):
	# 	frappe.msgprint("Hello Frappe from 'on_trash' event")


	# def after_delete(self):
	# 	frappe.msgprint("Hello Frappe from 'after_delete' event")





############################################################
######                Value Fetching                  ######
############################################################

# class server_side_scripting(Document):

# 	# def validate(self):
# 	# 	frappe.msgprint(_('my full name is "{0}" ').
# 	# 	format(self.first_name+" "+self.middle_name+" "+self.last_name))


# 	# ''' fetch value from child able '''

# 	# def validate(self):
# 	# 	for row in self.get("family_members"):
# 	# 		frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}' ")
# 	# 		.format(row.idx, row.name1, row.relation))





############################################################
######           frappe.get_doc(doctype, name)        ######
############################################################
""" return a document object of the record identified by doctype and name """ 

class server_side_scripting(Document):

	# frappe.get_doc(doctype, name)

	def validate(self):
		self.get_document()


	def get_document(self):
		doc = frappe.get_doc('client_side_scripting', self.client_side_doc)
		frappe.msgprint(_("The first name is {0} and age is {1}").
		format(doc.first_name, doc.age))


		for row in doc.get("family_members"):
			frappe.msgprint(_("{0}. The family member name is '{1}' and relation is '{2}' ")
			.format(row.idx, row.name1, row.relation))






# ############################################################
# ######              frappe.new_doc                    ######
# ############################################################

# class server_side_scripting(Document):
# 	def validate(self):
# 		self.new_document()

# 	def new_document(self):
# 		doc =frappe.new_doc("client_side_scripting")
# 		doc.first_name = 'Payal'
# 		doc.last_name = 'thummar'
# 		doc.age = 20
# 		doc.append('family_members', {
# 			'name1':'ab',
# 			'age':50,
# 			'relation':'sister'
# 		})
# 		doc.insert()





# ############################################################
# ######      frappe.delete_doc(doctype, name)          ######
# ############################################################

# class server_side_scripting(Document):
# 	def validate(self):
# 		frappe.delete_doc("client_side_scripting", "A")



############################################################
######                   Document method              ######
############################################################

# class server_side_scripting(Document):

# # doc.insert method
	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc =frappe.new_doc("client_side_scripting")
	# 	doc.first_name = 'Srushti'
	# 	doc.last_name = 'Mayani'
	# 	doc.age = 21
	# 	doc.append('family_members', {
	# 		'name1':'niyati',
	# 		'age':25,
	# 		'relation':'sister'
	# 	})
	# 	doc.insert()

		# some escape hatches that can be used to skip certain checks
		# doc.insert{
		# 	ignore_permissions = True # ignore write permission during insert
		# 	ignore_links = True # ignore link validation in the document
		# 	ignore_if_duplicate = True # don't insert if DuplicateEntryError is thrown
		# 	ignore_mandatory = True # insert even if mandatory fields are not set
		# }




# # doc.save method
	# def validate(self):
	# 	self.save_document()

	# def sace_document(self):
	# 	doc =frappe.new_doc("client_side_scripting")
	# 	doc.first_name = 'margii'
	# 	doc.last_name = 'Rupapra'
	# 	doc.age = 21
	# 	doc.save()

	# 	doc.save{
	# 		ignore_permissions = True # ignore write permission during insert
	# 		ignore_version = True # do not create a version record
	# 	}




# # doc.delete() method
# 	def validate(self):
# 		self.delete_document()

# 	def delete_document(self):
# 		doc =frappe.get_doc("client_side_scripting","Aa")
# 		doc.delete()




# # doc.db_set method
# 	def validate(self):
# 		self.db_set_document()

# 	def db_set_document(self):
# 		doc =frappe.get_doc("client_side_scripting","Anju")
# 		doc.db_set('age', 20)



############################################################
######                     get_list()                 ######
############################################################
# frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)


# class server_side_scripting(Document):
# 	def validate(self):
# 		self.get_list()

# 	def get_list(self):
# 		doc = frappe.db.get_list("client_side_scripting",
# 				filters={
# 					'enable': 1
# 				},
# 				fields=['first_name','age']
# 			)
# 		for d in doc:
# 			frappe.msgprint(_('The Parent First name is {0} and age is {1}').
# 			format(d.first_name, d.age))



############################################################
######            get_valu() & set_value()            ######
############################################################
# #frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype, filters, fieldname)
# class server_side_scripting(Document):
# 	def validate(self):
# 		self.get_value()
	
# 	def get_value(self):
# 		result = frappe.db.get_value('client_side_scripting','Maulik',['first_name','age'])

# 		if result:
# 			first_name, age = result
# 			frappe.msgprint(_("The first name is {0} and age is {1}").
# 			format(first_name, age))
# 		else:
# 			frappe.msgprint(_("No record found for the specified filters."))



# # frappe.db.set_value(doctype, name, fildname, value)
# class server_side_scripting(Document):
# 	def validate(self):
# 		self.set_value()

# 	def set_value(self):
# 		frappe.db.set_value("client_side_scripting",'Maulik','age',17)

# 		result = frappe.db.get_value('client_side_scripting','Maulik',['first_name','age'])

# 		if result:
# 			first_name, age = result
# 			frappe.msgprint(_("The first name is {0} and age is {1}").
# 			format(first_name, age))
# 		else:
# 			frappe.msgprint(_("No record found for the specified filters."))




# # Frappe.db.exists() = check doctype is present or not
# class server_side_scripting(Document):
# 	def validate(self):
# 		if frappe.db.exists('client_side_scripting','V'):
# 			frappe.msgprint(_('The Document is Exists in Databse'))
# 		else:
# 			frappe.msgprint(_('The Document does not exists in Database'))


# # frappe.db.count(doctype, filters) = the number of Document is prasent in specific doctype in db
# class server_side_scripting(Document):
# 	def validate(self):
# 		doc_count = frappe.db.count('client_side_scripting',{'enable' : 1})
# 		frappe.msgprint(_('The Enable document count is {0}').format(doc_count))



#######################################################################
###########                sql() method                     ###########
#######################################################################

# frappe.db.sql(query, filter, as_dict)
# class server_side_scripting(Document):

# 	def validate(self):
# 		self.sql()
	
# 	def sql(self):
# 		data = frappe.db.sql(""" 
# 								SELECT
# 									first_name,
# 									age
# 								FROM
# 									`tabclient_side_scripting`
# 								WHERE
# 									enable = 0					
# 							""", as_dict=True)
# 		for d in data:
# 			frappe.msgprint(_("The perent first name is {0} and age is {1}").
# 			format(d['first_name'], d['age']))



#######################################################################
###########                frm.call()                       ###########
#######################################################################

# class server_side_scripting(Document):
# 	@frappe.whitelist()
# 	def frm_call(self,msg):
# 		# import time
# 		# time.sleep(5)
# 		# frappe.msgprint(msg)

# 		return 'hii this message from frm_call'