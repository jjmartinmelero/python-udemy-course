class Animal:

    def eat(self):
        print("eating !")

    def sleep(self):
        print("sleeping !")

class Dog(Animal):
    def make_sound(self):
        print("wof !")

    #override() 
    def sleep(self):
        print("Dog sleeping")


print("Testing heredity:")
animal1 = Animal()


print("Animal class ------------------ : ")
animal1.eat()
animal1.sleep()

print("Dog class --------------------- : ")
dog = Dog()
dog.eat()
dog.sleep()
dog.make_sound()