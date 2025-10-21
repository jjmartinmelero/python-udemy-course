
list = [1,2,3,4,5]

print(list[0])


list[3] = 100
print(list)

# append
list.append(6)
print(list)

# delete
del list[3]
print(list)

print(f"elements: {len(list)}")

# step 2
names = ["Karla", "Juan", "Laura"]

for name in names: 
    print(name)

# Tuples

tuple = (1,2,3,4)

print(tuple)

for element in tuple:
    print(element)

coordinates = (3, 5)

print(f"coordinate X: {coordinates[0]}, Y: {coordinates[1]}")

# unpacking tuples
product = ("P001", "T-Shirt", 20.00)

id, description, price = product

print(product)
print(id, description, price)

# tuples with list
product_list = [
    ("P001", "T-shirt-1", 20.00),
    ("P002", "T-shirt-2", 10.00),
    ("P003", "T-shirt-3", 5.00)
]

for product in product_list:
    id, description, price = product
    print(f"Id: {id}, desc: {description}, price: {price}")

# Sets
set = {1,2,3,4,5}

print(set)

# add elements
set.add(6)

print(set)

set.remove(4)
print(set)

# iterar
for element in set:
    print(element)

# if exist an element
print(2 in set)

print(len(set))

# dictionary
person = {
    "name": "juan jesus",
    "age": 30,
    "country": "Spain"
}

print(person)

# # get value
print(f"Name: {person["name"]}")

# # update value
person["age"] = 31
print(person)

# # add
person["new_key"] = "test"
print(person)

# # remove
del person["new_key"]
print(person)

# # iterate
for key, value in person.items():
    print(f"key: {key} - value: {value}")

# list with dict
list = [
    {"name": "name 1", "last_name": "lastname 1"},
    {"name": "name 2", "last_name": "lastname 2"},
]

print(list)

# # print name 
print(list[0].get("name"))

# # loop 
for index, person in enumerate(list):
    print(person.get("name"))