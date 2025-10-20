# vars definition
name = "Juan Jesus"
age = 31
country = "Spain"

# Show information
print("name: ", name)
print("age: ", age)
print("country: ", country)

# update vars
name = "Juan Jesus v2"
age = 100

# Show information
print("name: ", name)
print("age: ", age)
print("country: ", country)

# dynamic type
age = "30v2"
print("age: ", age)


# types

## integer
age = 31
negative = -20

## float
size = 1.75
PI = 3.1416 # constant in python

## str
name = "Juan Jesus"
name2 = 'Juan Jesus'
name3 = """Juan
Jesus
Martin
Melero"""

print(name3)
## bool
isUser = True
isWoman = False

# special characters
print("Hello \n world")
print("Hello \t world")
print("Hello ' world")
print("Hello \" world")

# concat str
str1 = "hello"
str2 = "world"

concat = str1 + " " + str2

print(concat)

# concat with join
concat = "".join([str1," ",str2])

# format str
name = "Juan Jesus"
age = 31

message = "Hi, my name is {} and {} years old".format(name, age)
print(message)

# f str
message = f'Hi, my name is {name} and {age} years old'
print(message)

# len str
print(len(message))

# upperCase lowerCase
upper = message.upper()
lower = message.lower()
print(upper)
print(lower)

# sub str
substr = message[0: 25]
print(substr)

# input fn

name = input("Your name: ")
print(f"Name: {name}")


age = int(input("Your age: "))
print(f"age: {age}")

