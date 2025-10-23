from employee import Employee

class Company:

    def __init__(self, name):
        self.name = name
        self.__employees = []

    def add_employee(self, name, department):
        employee = Employee(name, department)
        self.__employees.append(employee)

    def get_employees_by_department(self, department):
        n_employees = 0

        for employee in self.__employees:
            if employee._department == department:
                n_employees += 1
                
        return n_employees