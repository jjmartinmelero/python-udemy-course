
def add_product(list):
    product = {"id": int(input("Id: ")), "name": input("Name: "), "price": float(input("Price: ")), "ammount": int(input("Amount: "))}
    list.append(product)
    print("Product added successfully")

def find_by_id(list):
    
    user_id = int(input('Id: '))
    
    for product in list:
        if product["id"] == user_id:
            print(product)
            return
        
    print("Product not found :(")


def delete_product(list):
    id_delete = int(input("Id to delete: "))
    for i, product in enumerate(list):
        if product["id"] == id_delete:
            list.pop(i)
            print("Product deleted successfully")
            return
    print("product not found")


def menu_options(user_option, list_products):
     match user_option:
        case 1:
            print(list_products)
        case 2:
            add_product(list_products)
        case 3:
            find_by_id(list_products)
        case 4:
            delete_product(list_products)