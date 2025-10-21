# EX 1 --------------------------------

print("get coordinates")

def get_coordinates():
    x, y, z = 10, 20, 30

    # return (x,y,z)
    return x,y,z

result = get_coordinates()

print(result)

x,y,z = get_coordinates()

print(x,y,z)

# EX 2 sum with several args
def custom_sum(*args):
    total = 0
    for num in args:
        total += num
    
    return total

print(custom_sum(2,3,4,5,6))

# EX 3 kwargs to print info
def custom_fn(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key} - value: {value}")

custom_fn(name="jjmartinmelero", age=31)

def is_even_number(number):
    return number % 2 == 0

print(is_even_number(50))
print(is_even_number(51))