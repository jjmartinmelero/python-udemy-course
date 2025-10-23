class Car:

    def __init__(self, brand, model, color):
        self._brand = brand
        self._model = model # atr protected
        self.__color = color # atr private

    def drive(self):
        print(f"driving {self._brand}, model: {self._model} with {self.__color} color")

    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        self._brand = brand

    def get_model(self):
        return self._model
    
    def set__model(self, model):
        self._model = model
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

    
