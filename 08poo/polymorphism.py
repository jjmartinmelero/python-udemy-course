class Animal:
    def make_sound(self):
        print("animal sound !")

class Dog(Animal):
    def make_sound(self):
        print("wof !")

class Cat(Animal):
    def make_sound(self):
        print("miau !")

print("Polymorphism ------------------ ")
animal1 = Animal()
animal1.make_sound()

print("dog")
dog1 = Dog()
dog1.make_sound()

print("cat")
cat1 = Cat()
cat1.make_sound()
