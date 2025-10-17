class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age}, country='{self.country}')"
    
    def present_yourself(self):
        return f"¡Hola! Me llamo {self.name}, tengo {self.age} años y soy de {self.country}."
