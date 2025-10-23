class Person:
    def __init__(self, name, last_name):
        self.__name = name
        self.__last_name = last_name

    # override __str__
    def __str__(self):
        return f''' Person
        name = {self.__name}
        last name = {self.__last_name}
        memory dir: {super.__str__(self)}
'''



# test class

person1 = Person("juan jesus", "martin melero")
print(person1)

