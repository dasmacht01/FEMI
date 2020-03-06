from share import *
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def select_tea(update, context):
    """ show teas of the catagory user chose """
    # subcategory = product_dict[update.callback_query.data]
    # use in test
    subcategory = 'YOLO'
    buttons = [[(tea, 'name-' + tea)] for tea in product_dict[subcategory]]
    send_message(update, 'Choose what you want to drink:',
                 reply_markup=inline_keyboard(buttons))


# noinspection PyGlobalUndefined
def select_sugar(update, context):
    """ function asking for sugar level """

    # create current_item object due to the tea the user chose
    global current_item
    current_item = Tea(name=update.callback_query.data[5:])
    logger.info(f'{current_item.name} is selected.')
    
    # send message for user to choose sugar level
    text = f'You have chosen {current_item.name}, please customize your product.\n' \
           'Choose sugar level:'
    buttons = [
        [('No Sugar', 'sugar-0')],
        [('25%', 'sugar-25')],
        [('50%', 'sugar-50')],
        [('75%', 'sugar-75')],
        [('Full Sugar', 'sugar-100')]
    ]
    send_message(update, text, inline_keyboard(buttons))


def select_ice(update, context):
    """ function to ask for ice level """

    # record sugar level to current_item object
    current_item.sugar = int(update.callback_query.data[6:])
    logger.info(f'sugar level: {current_item.sugar}')
    
    # send message for user to choose ice level
    buttons = [
        [('Hot', 'ice-hot')],
        [('No Ice', 'ice-no')],
        [('Less Ice', 'ice-less')],
        [('Regular Ice', 'ice-regular')],
        [('More Ice', 'ice-more')]
    ]
    send_message(
        update, 'Choose tea temperature:', inline_keyboard(buttons)
    )


def select_toppings(update, context):
    """ function to ask for toppings"""

    # record ice level to current_item object
    current_item.ice = update.callback_query.data[4:]
    logger.info(f'ice level: {current_item.ice}')

    # send message for user to choose toppings
    buttons = [[(topping, 'topping-' + topping)] for topping in toppings]
    send_message(
        update, 'choose some toppings if you want.',
        inline_keyboard(buttons)
    )


def end(update, context):
    logger.info(update.callback_query.data)