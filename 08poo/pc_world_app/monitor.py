class Monitor():
    __monitor_counter = 0

    def __init__(self, brand, size):
        Monitor.__monitor_counter += 1
        self._monitor_id = Monitor.__monitor_counter
        self._brand = brand
        self._size = size

    def __str__(self):
        return f'''Monitor Class:
        id: {self._monitor_id}
        brand: {self._brand}
        size: {self._size}
        '''