def approve_lop():
       leaves = frappe.get_all("Leave Application", filters=[["status", "!=", "Approved"]])
       for leave in leaves:
               doc = frappe.get_doc("Leave Application", leave['name'])
               if doc.status == "Draft":
                       doc.status = 'Open'
                       doc.save()
               doc.docstatus = 1
               doc.status = 'Approved'
               doc.save()
       frappe.db.commit()

def approve_declrations():
       declrations = frappe.get_all("Employee Tax Exemption Declaration", filters=[["form_status", "!=", "Approved"]])
       for declration in declrations:
               print(declration)
               try:
                       doc = frappe.get_doc("Employee Tax Exemption Declaration", declration['name'])
                       if doc.form_status == "Pending":
                               doc.form_status = 'Submit'
                               doc.save()
                       doc.docstatus = 1
                       doc.form_status = 'Approved'
                       doc.save()
               except Exception:
                       pass
       frappe.db.commit()

def save_slips():
       slips = frappe.get_all("Salary Slip", [["status", "=", "Draft"],["payroll_entry","=", "HR-PRUN-2019-00003"]])
       for slip in slips:
               doc = frappe.get_doc("Salary Slip", slip['name'])
               if frappe.get_value("Employee", doc.employee, "status") != "Left":

                       doc.save()
       frappe.db.commit()
