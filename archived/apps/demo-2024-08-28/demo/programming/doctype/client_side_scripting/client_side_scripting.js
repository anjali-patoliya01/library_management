// Copyright (c) 2024, anju and contributors
// For license information, please see license.txt

// frappe.ui.form.on("client_side_scripting", {
        ///////////////////////////////////////////////////////////
        //                        EVENTS                        //
        //////////////////////////////////////////////////////////

        /* refresh message */
	// refresh(frm) {
        // frappe.msgprint("Hello from 'refresh' event")
	// },

        // onload(frm){
        //         frappe.msgprint("Hello from 'onload' event")
        // },

        // validate(frm){
        //         frappe.throw("Hello from 'validate' event")
        // },

        // before_save(frm){
        //         frappe.throw("Hello from 'Before save' event")
        // },

        // after_save(frm){
        //         frappe.throw("Hello from 'after save' event")
        // },

        // enable(frm){
        //         frappe.msgprint("Hello from  'enable' fieldname event")
        // },

        // age: function(frm){
        //         frappe.msgprint("Hello from  'age' fieldname event")
        // },



        // ---------------------------------------------------------------
        // family_members_on_from_rendered: function(frm){
        //         frappe.msgprint("Hello from 'family members' child table rendered event")
        // },
         // ---------------------------------------------------------------

         

        // before_submit: function(frm){
        //         frappe.throw("Hello from  'before_submit' event")
        // },

        // on_submit: function(frm){
        //         frappe.msgprint("Hello from  'on_submit'  event")
        // },

        // before_cancel: function(frm){
        //         frappe.throw("Hello from  'before_cancel' event")
        // },

        // after_cancel: function(frm){
        //         frappe.msgprint("Hello from  'after_cancel' event")
        // },

// });

///////////////////////////////////////////////////////////
//                 Child Table EVENTS                   //
//////////////////////////////////////////////////////////

// frappe.ui.form.on('family_members', {

//         name1(frm){
//                 frappe.msgprint("Hello from Child DocType 'name1' event")
//         },

//         /* cdt = Child DocType name i.e Family_members
//            cdn = row name   
//         */

//         age(frm,cdt, cdn){
//                 frappe.msgprint("Hello from 'age' Child DocType fieldname event")
//         }
// });



// /////////////////////////////////////////////////////////
//                 Fetching Value                       //
// ////////////////////////////////////////////////////////
// frappe.ui.form.on('client_side_scripting', {
//         after_save: function(frm) {
//             // Display the full name of the client
//             frappe.msgprint(__("The full name is '{0}'", 
//                 [frm.doc.first_name + " " + (frm.doc.middle_name || "") + " " + frm.doc.last_name]
//             ));
            
//             // Check if the family_members field exists and is an array
//             if (frm.doc.family_members && frm.doc.family_members.length > 0) {
//                 frm.doc.family_members.forEach(row => {
//                     frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}'", 
//                         [row.idx, row.name1, row.relation]
//                     ));
//                 });
//             } else {
//                 frappe.msgprint(__('No family members found.'));
//             }
//         }
//     });
    


// ///////////////////////////////////////////////////////////
// //                 frm.set_intro & frm.is_new()          //
// //////////////////////////////////////////////////////////
// frappe.ui.form.on("client_side_scripting",{
//         refresh:function(frm){
//         //      rm.set_intro("How you can create a new Client side Scripting doctype")  
        
//                 if(frm.is_new()){
//                         frm.set_intro("How you can create a new Client side Scripting doctype")       
//                 }
//         }
       
        
// });


// ///////////////////////////////////////////////////////////
// //                 frm.set_value & frm.add_child         //
// //////////////////////////////////////////////////////////
// frappe.ui.form.on("client_side_scripting",{
//         validate:function(frm){
//         //      frm.set_value("full_name",frm.doc.first_name +" "+ frm.doc.middle_name +" "+ frm.doc.last_name) 
        
//                 let row = frm.add_child('family_members', {
//                         name1: 'kantibhai patel',
//                         age:50,
//                         relation:'father'
//                 })
//         }
       
        
// });





// ///////////////////////////////////////////////////////////
// //                   frm.set_df_property                 //
// //////////////////////////////////////////////////////////
// frappe.ui.form.on("client_side_scripting",{
//         enable:function(frm){
//                 frm.set_df_property('first_name','reqd', 1)

//                 frm.set_df_property('middle_name','read_only', 1)

//                 frm.toggle_reqd('age',true)
//         }
       
        
// });




// ///////////////////////////////////////////////////////////
// //                          Button                      //
// //////////////////////////////////////////////////////////
// frappe.ui.form.on("client_side_scripting",{
//         refresh:function(frm){
//                 /*frm.add_custom_button('Click Me Button',() =>{
//                         frappe.msgprint(__("You Clicked Me!!"))
//                 }) */
               
//                 frm.add_custom_button("Click me1", () =>{
//                         frappe.msgprint(__('You Clicked 1 !!'))
//                 }, 'click me')

//                 frm.add_custom_button("Click me2", () =>{
//                         frappe.msgprint(__('You Clicked 2 !!'))
//                 }, 'click me')

//         }
       
        
// });