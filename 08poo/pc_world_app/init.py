from mouse import Mouse
from keyboard import Keyboard
from monitor import Monitor
from computer import Computer
from order import Order

print("PC WORLD APP")

mouse1 = Mouse("brand1", "input type 1")
mouse2 = Mouse("brand2", "input type 2")
mouse3 = Mouse("brand3", "input type 3")

print(mouse3)

keyboard1 = Keyboard("brand1", "input type 1")
keyboard2 = Keyboard("brand2", "input type 2")
keyboard3 = Keyboard("brand3", "input type 3")

print(keyboard3)

monitor1 = Monitor("brand1", "size 1")
monitor2 = Monitor("brand2", "size 2")
monitor3 = Monitor("brand3", "size 3")

print(monitor3)

computer1 = Computer("name1", monitor1, keyboard1, mouse1 )
computer2 = Computer("name2", monitor2, keyboard2, mouse2 )
computer3 = Computer("name3", monitor3, keyboard3, mouse3 )

print(computer3)


order = Order([computer1, computer2])
print(order)
order.add_computers(computer3)
print(order)