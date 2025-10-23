class Employee:

    employee_counter = 0

    def __init__(self, name, department):
        self._name = name
        self._department = department
        Employee.employee_counter += 1
        self.id = Employee.employee_counter

    @classmethod
    def get_total_employees(cls):
        return cls.employee_counter
    
