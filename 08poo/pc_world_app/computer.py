class Computer:
    __computer_counter = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.__computer_counter += 1
        self._computer_id = Computer.__computer_counter
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    def __str__(self):
        return f''' Computer Class
        name: {self._name}
        monitor: {self._monitor}
        keyboard: {self._keyboard}
        mouse: {self._mouse}
        '''