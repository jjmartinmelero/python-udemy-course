from input_device import InputDevice

class Mouse(InputDevice):
    # counter
    __mouse_counter = 0

    def __init__(self, brand, input_type):
        Mouse.__mouse_counter += 1
        self._mouse_id = Mouse.__mouse_counter
        super().__init__(brand, input_type)

    def __str__(self):
        return f'''Mouse Class:
        id: {self._mouse_id}
        brand: {self._brand}
        input type: {self._input_type}
        '''