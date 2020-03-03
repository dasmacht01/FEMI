# can use html
# can elaborate with 'typing' status

current_item = None
cart = []


def menu_construct(categories):
    for subcategory in categories:
        product_dict[subcategory] = eval(subcategory)

from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)

def inline_keyboard(primative_buttons):
    buttons = [[InlineKeyboardButton(button[0], callback_data=button[1]) for button in row]
               for row in primative_buttons]
    return InlineKeyboardMarkup(buttons)


class Tea: # edited
    def __init__(self, name, sugar=50, ice=50, toppings=[]): # toppings is a list
        self.name = name
        self.sugar = sugar
        self.ice = ice
        self.toppings = toppings
        self.price = price_dict[self.name]

    def __repr__(self):
        text = f'{self.name}:\nsugar: {self.sugar}, ice: {self.ice};'
        if self.toppings:
            text += f'\n{", ".join(self.toppings)}'
        return text


# ---Tea Menu--- #
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

'''product_dict = {'Cheezy': ['Cheezy Peach Oolong',
            'Cheezy Matcha',
            'Cheezy Osmanthus Oolong',
            'Cheezy Jinfeng Oolong',
            'Cheezy Jasmine'],
 'Diet_tea': ['Peach Oolong', 'Osmanthus Oolong', 'Jinfeng Oolong', 'Jasmine'],
 'Flavoured_tea': ['Ice Cream Taro Latte',
                   'Cheezy Roasted Latte',
                   "Femi's Special Latte",
                   'Purple Taro Latte',
                   'Black Sugar Fresh Milk',
                   'Yakult Passion Fruit',
                   'Yakult Lemon Lime',
                   'Fujiyama Latte',
                   'Fresh Milk Tea'],
 'Fruits_burst': ['Cheezy Rambutan',
                  'Fruits BOOM',
                  'Cheezy Pineapple',
                  'Cheezy Watermelon',
                  'Passion Lemon Tea',
                  'Coconut Mango'],
 'YOLO': ['YOLO Strawberry',
          'YOLO Mango',
          'YOLO Advocado',
          'YOLO Dragon Fruit']}'''

# ---Price--- #
'''import random
for sub in product_dict:
    price_dict.update(temp := {tea: random.randint(5,15) for tea in eval(sub)})'''

price_dict = {'Black Sugar Fresh Milk': 13,
 'Cheezy Jasmine': 15,
 'Cheezy Jinfeng Oolong': 15,
 'Cheezy Matcha': 12,
 'Cheezy Osmanthus Oolong': 5,
 'Cheezy Peach Oolong': 14,
 'Cheezy Pineapple': 8,
 'Cheezy Rambutan': 7,
 'Cheezy Roasted Latte': 9,
 'Cheezy Watermelon': 5,
 'Coconut Mango': 14,
 "Femi's Special Latte": 10,
 'Fresh Milk Tea': 12,
 'Fruits BOOM': 9,
 'Fujiyama Latte': 7,
 'Ice Cream Taro Latte': 5,
 'Jasmine': 5,
 'Jinfeng Oolong': 10,
 'Osmanthus Oolong': 9,
 'Passion Lemon Tea': 7,
 'Peach Oolong': 13,
 'Purple Taro Latte': 5,
 'YOLO Advocado': 9,
 'YOLO Dragon Fruit': 7,
 'YOLO Mango': 5,
 'YOLO Strawberry': 10,
 'Yakult Lemon Lime': 15,
 'Yakult Passion Fruit': 13}
