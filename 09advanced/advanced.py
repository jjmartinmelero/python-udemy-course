from functools import reduce


# zip FN
names = ["name1", "name2", "name3"]
age = ["age1", "age2", "age3"]
countries = ['country1', 'country2', 'country3']


people = zip(names, age, countries)

print(people)


for person in people:
    print(person) 


# strings
##  Split fn
string = "Hello world"
words = string.split() 

## default split -> " "
print(words)

## find and replace
indexWCharacter = string.find("world") # -2 not found
print(indexWCharacter)

string2 = string.replace("world", "mundo")
print(string2)

## multiplicate
string = "Hello "
result = string * 3

print(result)

## strip - clear string - start and end of string
string = "    Hello world   "
striptString = string.strip()

string = ".......Hello world..."
striptString2 = string.strip(".")

print(striptString, striptString2)



# lambda

def square(x):
    return x ** 2

print(square(5))

square_lambda = lambda x: x ** 2

print(square_lambda(3))


# map and filter

numbers_list = [1,2,3,4,5]
square_numbers = list(map(lambda x: x**2, numbers_list))
print(square_numbers)

pares = list(filter(lambda x: x % 2 == 0, numbers_list))
print(pares)


# reduce and map
acumulative = reduce(lambda x, y: x + y, numbers_list)
print(acumulative)


# sorter 
employees = ["Juan", "Pedro", "Maria"]
# employees_order = sorted(employees, reverse=True)
employees_order = sorted(employees)
print(employees_order)

# order a dictionary
employees_dict = [
    {"name": "Juan", "salary": 3000},
    {"name": "Maria", "salary": 3500},
    {"name": "Pedro", "salary": 1500},
]

employees_dict_salary = sorted(employees_dict, reverse=True, key=lambda x: x["salary"])
print(employees_dict_salary) 


# generators



