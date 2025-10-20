
# EX 1 --------------------------------------
# print("Discount market")

# NO_PRODUCTS_DISCOUNT = 10

# n_products = int(input("number of products: "))
# membership = input("are you a partner ? Y/N: ").upper()[:1]
# is_discount = (membership == "Y") and (n_products >= NO_PRODUCTS_DISCOUNT)

# if is_discount: 
#     print("you have discount !")
# else:
#     print("oh...")

# EX 2 --------------------------------------

# print("library")

# student_credential = input("Do u have studen credential ? Y / N: ").upper()[:1]
# near_the_library = input("Do you live near the library? ? Y/N: ").upper()[:1]

# if student_credential == "Y" or near_the_library == "Y": 
#     print("You can access to the library")
# else:
#     print("oh...")

# EX 3 --------------------------------------

# print("supermarket")

# milk_price = float(input("milk price: "))
# bread_price = float(input("Bread price: "))
# coffe_price = float(input("Coffe price: "))

# total = milk_price + bread_price + coffe_price

# print("impuesto: ", total * .21)
# print("total: ", total + total * .21)


# EX 4 --------------------------------------


USER_NAME = "jjmartinmelero"
USER_PASSWORD = "123456"

print("Authenticator")

user_name = input("Username: ")
user_password = input("password: ")

if user_name == USER_NAME and user_password == USER_PASSWORD:
    print("Hello user !")
else :
    print("Credentials are not valid :(")