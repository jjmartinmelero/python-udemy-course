# EX 1
name = input("Your name:")
age = int(input("age: "))
country = input("Country: ")
print(f'Hi {name}, {age} from {country}')

# EX 2
# generate uid 
import random
# from random import randint

name = input("Your name:")
last_name = input("Last name: ")
year_of_birth = input("Year of birth YYYY: ")

# build base uid
uid_base = f"{name[:2].upper()}{last_name[:2].upper()}{year_of_birth[2:]}"
# append a random 4-digit number
random_suffix = random.randint(1000, 9999)
print(f"{uid_base}{random_suffix}")
