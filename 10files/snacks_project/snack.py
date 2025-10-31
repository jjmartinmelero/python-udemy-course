class Snack:
    snack_counter = 0

    def __init__(self, name = "", price = 0.0):
        Snack.snack_counter += 1
        self.id = Snack.snack_counter
        self.name = name
        self.price = price

    def __str__(self):
        return (f'Snack: id: {self.id}, name={self.name}, '
                f'price: {self.price}')

    def write_snack(self):
        return f'{self.id},{self.name},{self.price}'
