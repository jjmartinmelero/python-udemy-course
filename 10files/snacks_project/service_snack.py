import os.path
from snack import Snack


class SnackService:
    FILE_NAME = "snacks.txt"

    def __init__(self):
        self.snacks = []

        if os.path.isfile(self.FILE_NAME):
            self.snacks = self.load_snacks()
        else: 
            self.load_initial_snacks()

    def load_initial_snacks(self):
        initial_snacks = [
            Snack("Papas", 1.20),
            Snack("Cocacola", 1.90),
            Snack("Sandwich", 2.50)
        ]

        self.snacks.extend(initial_snacks)
        self.save_snacks_file(initial_snacks)
 
    def save_snacks_file(self, snacks):
        try:
            with open(self.FILE_NAME, 'a') as file:
                for snack in snacks:
                    file.write(f'{snack.write_snack()}\n')
        except Exception as e:
            print(f'Error {e}')

    def load_snacks(self):
        snacks = []

        print("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOAD")

        try:
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    id, name, price = line.strip().split(',')
                    snack = Snack(name, float(price))
                    snacks.append(snack)
        except Exception as e:
            print(f'Error to read file {e}')

        return snacks

    def add_snack(self, snack):
        self.snacks.append(snack)
        self.save_snacks_file([snack])


    def show_snacks(self):
        print('***** snacks *****')
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks
