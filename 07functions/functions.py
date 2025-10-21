
def greetings(): 
    print("Hello world")

def greetings2(message): 
    print(f"Message: {message}")

def greetings3(message): 
    print(f"Message: {message}")
    return "value from fn"

def sum_fn(number1, number2):
    return number1 + number2



greetings()
greetings2("Hello world !")
value = greetings3("Hello world !")
print(value)
print(sum_fn(5,5))

# from module
from module import custom_sum

num1, num2 = 3, 3
result = custom_sum(num1, num2)

print(result)


# arguments by name
def create_person(name, last_name = "", age = 0):
    print(name)

create_person("juan jesus", "martin melero", 31)
# # create_person(name = "juan jesus", last_name="martin melero", age=31)

# # with other order
create_person(age=31,name = "juan jesus", last_name="martin melero")

# Return tuple from fn
def create_person_upper(name, last_name, age):
    return name.upper(), last_name.upper(), age


name, last_name, age = create_person_upper(age=31,name = "juan jesus", last_name="martin melero")

print(f"name uppercase with unpacking: {name}")

# Several args
def hero(name, *args):
    print(f"name: {name} - args: {args}")
    for power in args:
        print(power)

hero("superman", "test1", "test2", "test3")
hero("spidernab", "test1")


# kwargs - keyword arguments

def hero2(name, *args, **kwargs):
    print(f"name: {name} - args: {args} - kwargs: {kwargs}")

hero2("superman", "test1", age=20, company="marvel")


# recursive
def recursive(number):
    if number == 1:
        print(number)
    else:
        recursive(number -1)

recursive(5)