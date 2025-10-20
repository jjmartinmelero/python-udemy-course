
#  **************************************** operations
a , b = 10, 5

sum = a + b
print(sum)

# subtract
subtract = a - b
print(subtract)

# multiplication
multiplication = a * b
print(multiplication)

# division
division = a / b
print(division)

# module 
module = a % b
print(module)

# full subtract 
full_subtact = a // b
print(full_subtact)

# potency
potency = a ** b
print(potency)

# **************************************** assignment operators

# several values
a, b, c = 10, "hello world", 14.5

print(f"value a: {a}, value b: {b}, value c: {c}")

# same value to several vars
a = b = c = 10

print(a, b, c)


# **************************************** compound assignment

print("compound assignment")
a, b = 10, 5

print(a, b)

a += b
print(a)

a -= b
print(a)

a *= b
print(a)

a //= b
print(a)


# **************************************** comparation

a , b = 10, 5

result = a == b
print(result)

result = a != b
print(result)

result = a > b
print(result)

result = a < b
print(result)


# **************************************** comparation
print("Comparation and")
condition1 = False
condition2 = False
result = condition1 and condition2
print(result)

condition1 = False
condition2 = True
result = condition1 and condition2
print(result)

print("Comparation or")
condition1 = False
condition2 = False
result = condition1 or condition2
print(result)

condition1 = False
result = condition1 or condition2
print(result)

print("Comparation not")
condition1 = False

print(not condition1)

