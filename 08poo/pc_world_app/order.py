class Order:
    __order_counter = 0

    def __init__(self, computers):
        Order.__order_counter += 1
        self._order_id = Order.__order_counter
        self._computers_list = computers

    def add_computers(self, computer):
        self._computers_list.append(computer)

    def __str__(self):
        str_computers = ""

        for computer in self._computers_list:
            str_computers += "\n" + computer.__str__()

        return f''' Order
        id: {self._order_id}
        computers: {str_computers}'''