from person import Person
from arithmetic import Arithmetic
from car import Car

person = Person("Juan", "Martín")
person2 = Person("test1", "test2")

person.show_contact()
person2.show_contact()

arth = Arithmetic(4,2)

print(arth.sum())
print(arth.multiplication())

car1 = Car("Toyota", "Yaris", "Blue")
car1.drive()
print(car1.get_color())
car1.set_color("Yellow")
print(car1.get_color())


print(f"show car attributes: {car1.__dict__}")

# show person class counter
# print(Person.people_counter)
print(Person.get_people_counter_static())

# recommended
print(Person.get_people_counter_class())

