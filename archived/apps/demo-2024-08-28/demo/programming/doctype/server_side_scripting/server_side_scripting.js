// Copyright (c) 2024, anju and contributors
// For license information, please see license.txt

// frappe.ui.form.on("server_side_scripting", {
// 	refresh(frm) {

// 	},
// });


// // Frppe frm_call method
// frappe.ui.form.on("server_side_scripting", {
//     enable: function(frm) {
//         frm.call({
//         doc: frm.doc,
//         method : 'frm_call',
//         args : {
//             msg: 'Hello'
//         },
//         freeze : true,
//         freeze_message : __('Calling frm_call Method'),
//         callback: function(r) {
//             frappe.msgprint(r.message)

//             // frappe.msgprint('Server side calling compleated')
//             // frm.refresh_field('madication_order')

//         }
//         });
//     }

// });






// //  frappe.call() method
frappe.ui.form.on("server_side_scripting", {
    enable: function(frm) {
        frappe.call({
        // doc: frm.doc,/
        method : 'demo.programming.doctype.client_side_scripting.client_side_scripting.frappe_call',
        args : {
            msg: 'Hello'
        },
        freeze : true,
        freeze_message : __('Calling frm_call Method'),
        callback: function(r) {
            frappe.msgprint(r.message)

        }
        });
    }

});