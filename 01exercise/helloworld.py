# first program
from person import Person  # Importamos la clase Person desde el módulo person

print("Hello world!")

# Crear una nueva persona
person1 = Person("Juan Jesus", 31, "España")

# Show information
print("\nInformación de la persona:")
print(person1)
print(person1.present_yourself())