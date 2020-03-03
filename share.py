from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)

# "inline_keyboard" in a convinient function that
# convert List[List[Tuple[Any, Any]]] to InlineKeyboardMarkup object
# you can see how to use it in lrh.py
def inline_keyboard(primative_buttons):
    """ a convenient function which help to write an InlineKeyboardMarkup object """
    buttons = [[InlineKeyboardButton(button[0], callback_data=button[1]) for button in row]
               for row in primative_buttons]
    return InlineKeyboardMarkup(buttons)


class Tea:
    def __init__(self, name=None, price=None, sugar=None, ice=None, toppings=None):
        self.name = name
        self.price = price
        self.sugar = sugar
        self.ice = ice
        self.toppings = toppings

    def __repr__(self):
        text = f'{self.name}:\n'\
               f'sugar level: {self.sugar}, ice level: {self.ice}\n'\
               f'Toppings: {", ".join(self.toppings) if self.toppings else "None"}'
        return text


current_item = None
cart = []

# Tea Menu
categories = ['YOLO', 'Fruits_burst', 'Flavoured_tea', 'Cheezy', 'Diet_tea']
YOLO = ['YOLO Strawberry', 'YOLO Mango', 'YOLO Advocado', 'YOLO Dragon Fruit']
Fruits_burst = ['Cheezy Rambutan', 'Fruits BOOM', 'Cheezy Pineapple',
                'Cheezy Watermelon', 'Passion Lemon Tea', 'Coconut Mango']
Flavoured_tea = ['Ice Cream Taro Latte', 'Cheezy Roasted Latte', 'Femi\'s Special Latte',
                 'Purple Taro Latte', 'Black Sugar Fresh Milk', 'Yakult Passion Fruit',
                 'Yakult Lemon Lime', 'Fujiyama Latte', 'Fresh Milk Tea']
Cheezy = ['Cheezy Peach Oolong', 'Cheezy Matcha', 'Cheezy Osmanthus Oolong',
          'Cheezy Jinfeng Oolong', 'Cheezy Jasmine']
Diet_tea = ['Peach Oolong', 'Osmanthus Oolong', 'Jinfeng Oolong', 'Jasmine']
product_dict = {category: eval(category) for category in categories}
