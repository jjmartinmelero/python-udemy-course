
is_raining = False

if is_raining: 
    print("is raining !")
else:
    print("is not raining")



is_cloudy = True

if is_raining:
    print("is raining !")
elif is_cloudy: 
    print("The weather is bad")
else: 
    print("have a good day !")



# ternary operator
number1 = 10
number2 = 40

result = number1 if (number1 > number2) else number2

print(result)