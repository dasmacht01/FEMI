# can use html
# can elaborate with 'typing' status

from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)

__all__ = [
    'Tea', 'current_item', 
    'cart', 'inline_keyboard', 
    'send_message', 'product_dict', 
    'price_dict', 
]


current_item = None
cart = []


def inline_keyboard(primative_buttons):
    """ 'inline_keyboard' is a convinient function
         to write InlineKeyboardMarkup object """
    buttons = [[InlineKeyboardButton(button[0], callback_data=button[1]) for button in row]
               for row in primative_buttons]
    return InlineKeyboardMarkup(buttons)
    # example of inline_keyboard:
    # >>> primative_button = [[('1', '1')], [('2', '2')]]
    # >>> keyboard = inline_keyboard(primative_button)
    # >>> bot.send_message(chat_id, text, reply_markup=keyboard


def send_message(update, text, reply_markup=None, **kwargs):
    """ a simple function to send telegram message """
    try:
        update.callback_query.edit_message_text(
            text, reply_markup=reply_markup, **kwargs
        )
    except AttributeError:
        update.message.reply_text(
            text, reply_markup=reply_markup, **kwargs
        )


class Tea:  # simplified version
    def __init__(self, name, sugar=50, ice=50, toppings=[]):  # toppings is a list!
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


# ----------Tea Menu--------- #
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
toppings = ['Pearl', 'Red Bean', 'Coconut', 'Milk']

# product_dict = {category: eval(category) for category in categories}'''
product_dict = {
    'Cheezy': [
        'Cheezy Peach Oolong',
        'Cheezy Matcha',
        'Cheezy Osmanthus Oolong',
        'Cheezy Jinfeng Oolong',
        'Cheezy Jasmine'
    ],
    'Diet_tea': [
        'Peach Oolong',
        'Osmanthus Oolong',
        'Jinfeng Oolong',
        'Jasmine'
    ],
    'Flavoured_tea': [
        'Ice Cream Taro Latte',
        'Cheezy Roasted Latte',
        "Femi's Special Latte",
        'Purple Taro Latte',
        'Black Sugar Fresh Milk',
        'Yakult Passion Fruit',
        'Yakult Lemon Lime',
        'Fujiyama Latte',
        'Fresh Milk Tea'
    ],
    'Fruits_burst': [
        'Cheezy Rambutan',
        'Fruits BOOM',
        'Cheezy Pineapple',
        'Cheezy Watermelon',
        'Passion Lemon Tea',
        'Coconut Mango'
    ],
    'YOLO': [
        'YOLO Strawberry',
        'YOLO Mango',
        'YOLO Advocado',
        'YOLO Dragon Fruit'
    ]}
# ---------Price--------- #
price_dict = {
    'Black Sugar Fresh Milk': 13,
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
    'Yakult Passion Fruit': 13
}
