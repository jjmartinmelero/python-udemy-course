class Person: 

    # var in class
    __people_counter = 0
    
    def __init__(self, name, last_name):
        Person.__people_counter += 1
        self.name = name
        self.last_name = last_name

    @staticmethod
    def get_people_counter_static():
        print("static method")
        return Person.__people_counter
    
    @classmethod
    def get_people_counter_class(cls):
        print("class method")
        return cls.__people_counter

    def show_contact(self):
        print(f"Name: {self.name}, last name: {self.last_name}")



