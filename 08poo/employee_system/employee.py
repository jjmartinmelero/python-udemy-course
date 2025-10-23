class Employee:

    __employee_counter = 0

    def __init__(self, name, department):
        Employee.__employee_counter += 1
        self.__name = name
        self._department = department

    @classmethod
    def get_total_employees(cls):
        print(cls.__employee_counter)
    
