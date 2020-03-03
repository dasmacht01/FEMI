from share import *


def select_tea(update, context):
    """ show teas of the catagory user chose """
    subcategory = product_dict[update.callback_query.data]
    buttons = [[(tea, tea)] for tea in categories[subcategory]]
    update.callback_query.edit_message_text('Choose what you want to drink:',
                                            reply_markup=inline_keyboard(buttons))


def select_sugar(update, context):
    """ function asking for sugar level """

    # create current_item object due to the tea the user chose
    current_item = Tea(name=update.callback_query.data)

    # send message for user to choose sugar level
    text = f'You have chosen {current_item.name}, please customize your product.\n' \
           'Choose sugar level:'
    buttons = [[('No Sugar', 'sugar-0')],
               [('25%', 'sugar-25')],
               [('50%', 'sugar-50')],
               [('75%', 'sugar-75')],
               [('Full Sugar', 'sugar-100')]]
    update.callback_query.edit_message_text(text, reply_markup=inline_keyboard(buttons))


def select_ice(update, context):
    """ function to ask for ice level """

    # record sugar level to current_item object
    current_item.suagr = int(update.callback_query.data[6:])

    # send message for user to choose ice level
    buttons = [[('Hot', 'ice-hot')],
               [('No Ice', 'ice-no')],
               [('Less Ice', 'ice-less')],
               [('Regular-ice', 'ice-regular')],
               [('More Ice', 'ice-more')]]
    update.callback_query.edit_message_text('Choose tea temperature:',
                                            reply_markup=inline_keyboard(buttons))


def select_toppings(update, context):
    """ function to ask for toppings"""

    # record ice level to current_item object
    current_item.ice = update.callback_query.data[4:]

    # send message for user to choose toppings
    buttons = [[('Pearl', 'pearl'), ('Red Bean', 'red-bean')],
               [('Coconut', 'coconut'), ('Milk', 'milk')],
               [('That\'s all', 'rh-Done')]]
    update.callback_query.edit_message_text('choose some toppings if you want.',
                                            reply_markup=inline_keyboard(buttons))
