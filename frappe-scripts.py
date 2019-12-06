def make_user_permissions():
    salary_slips = frappe.get_all("Salary Slips", fields= ["owner", "name"])
	for slip in salary_slips:
		user_permission = frappe.new_doc("User Permission")
		user_permission.user = slip.owner
		user_permission.for_value = slip.name
		user_permission.allow = "Salary Slip"
		user_permission.apply_to_all_doctypes = 1
		user_permission.save
	frappe.db.commit()