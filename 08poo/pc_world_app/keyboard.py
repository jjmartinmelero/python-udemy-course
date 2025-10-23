from input_device import InputDevice

class Keyboard(InputDevice):
    # counter
    __keyboard_counter = 0

    def __init__(self, brand, input_type):
        Keyboard.__keyboard_counter += 1
        self._keyboard_id = Keyboard.__keyboard_counter
        super().__init__(brand, input_type)

    def __str__(self):
        return f'''Keyboard Class:
        id: {self._keyboard_id}
        brand: {self._brand}
        input type: {self._input_type}
        '''