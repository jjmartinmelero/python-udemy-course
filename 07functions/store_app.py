
from store_app_impl import menu_options

print("Store App")

exit = False
list_products = []

while(not exit):
    print("Select an Option:")
    print("1. - show inventory")
    print("2. - Add new Product")
    print("3. - Find product")
    print("4. - Delete product")
    print("5. - Exit")

    user_option = int(input())

    if user_option == 5:
        exit = True
    else: 
        menu_options(user_option, list_products)
        
