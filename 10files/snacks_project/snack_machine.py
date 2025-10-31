from service_snack import SnackService
from snack import Snack

class SnackMachine:

    def __init__(self):
        self.snack_service = SnackService()
        self.products = []

    def menu(self):
        exit = False
        print("Snack Machine")
        self.snack_service.show_snacks()

        while not exit:
            try:
                option = self.show_menu()
                exit = self.execute_option(option)

            except Exception as e:
                print(f'Error: {e}')


    def show_menu(self):
        print(f'''Menu:
            1. Buy snack
            2. show ticket
            3. add new snack
            4. show snacks
            5. exit''')

        return int(input("Select an option: "))

    def execute_option(self, option):
        if option == 1:
            self.buy_snack()
        elif option == 2: 
            self.show_ticket()
        elif option == 3:
            self.add_snack()
        elif option == 4:
            self.snack_service.show_snacks()
        elif option == 5:
            print('Good bye !')
            return True 
        else: 
            print(f'Option is not valid {option}')

        return False

    def buy_snack(self):
        id_snack = int(input('select an id to buy snack: '))
        snacks = self.snack_service.get_snacks()
        snack_selected = next((snack for snack in snacks if snack.id == id_snack), None)

        if snack_selected:
            self.products.append(snack_selected)
            print(f'snack found ! {snack_selected}')
        else: 
            print(f'Id snack not found: {id_snack}')

    
    def show_ticket(self):
        if not self.products:
            print("you dont have snacks")
            return

        total = sum(snack.price for snack in self.products)

        print("####### ticket #######")
        for product in self.products:
            print(f'\t- {product.name} - ${product.price:.2f}')
        print(f'\tTotal - ${total:.2f}')


    def add_snack(self):
        name = input('snack name: ')
        price = float(input('snack price: '))
        new_snack = Snack(name, price)
        self.snackService.add_snack(new_snack)
        print('Snack added')


