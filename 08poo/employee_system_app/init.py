from company import Company
from employee import Employee


company = Company("Company 1")

company.add_employee("JJ", "dp1")
company.add_employee("TT", "dp1")
company.add_employee("FF", "dp2")

print(company.get_employees_by_department("dp1"))
print(f"employees: {Employee.get_total_employees()}")

# Show all employees:
company.show_all_employees()