from share import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time
import logging
from io import BytesIO

text = 'Here are your orders.\n' 'Tap any selection if you want to cancel it.\n'
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# 0. -------start--------
def start(update, context):
    text_start_1 = "Hello, Welcome to Femi's Tea."
    text_start_2 = "Today's special is {0}.".format(special)
    text_start_over = 'Just choose what you want please!'
    buttons=[[InlineKeyboardButton(text='YOLO', callback_data='YOLO'),
              InlineKeyboardButton(text='Fruits_burst', callback_data='Fruits_burst')],
             [InlineKeyboardButton(text='Flavoured_tea', callback_data='Flavoured_tea'),
              InlineKeyboardButton(text='Cheezy', callback_data='Cheezy')],
             [InlineKeyboardButton(text='Diet_tea', callback_data='Diet_tea'),
              InlineKeyboardButton(text="Today's special", callback_data="Today's special")]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.message.reply_text(text=text_start_1)

    with open('1.jpg', 'rb') as f:
        bot.send_photo(chat_id=update.effective_chat.id, photo=f, timeout=50)
    with open('2.jpg', 'rb') as p:
        bot.send_photo(chat_id=update.effective_chat.id, photo=p, timeout=50)

    update.message.reply_text(text=text_start_2, reply_markup=keyboard)
    return 'SELECT_TEA'

# 1. ---------start_over----------
def start_over(update, context):
    text_start_1 = "Hello, Welcome to Femi's Tea."
    text_start_2 = "Today's special is {0}.".format(special)
    text_start_over = 'Just choose what you want please!'

    buttons = [[InlineKeyboardButton(text='YOLO', callback_data='YOLO'),
                InlineKeyboardButton(text='Fruits_burst', callback_data='Fruits_burst')],
               [InlineKeyboardButton(text='Flavoured_tea', callback_data='Flavoured_tea'),
                InlineKeyboardButton(text='Cheezy', callback_data='Cheezy')],
               [InlineKeyboardButton(text='Diet_tea', callback_data='Diet_tea'),
                InlineKeyboardButton(text="Today's special",
                                     callback_data="Today's special")]]

    buttons.append([InlineKeyboardButton(text='check_out', callback_data='check_out')])
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text_start_over, reply_markup=keyboard)


# 2. ---------select_tea----------
def select_tea(update, context):
    """ show teas of the catagory user chose """
    # subcategory = product_dict[update.callback_query.data]
    # use in test
    subcategory = update.callback_query.data
    buttons = [[(tea, 'name-' + tea)] for tea in product_dict[subcategory]]
    send_message(update, 'Choose what you want to drink:',
                 reply_markup=inline_keyboard(buttons))


# 3. ----------select_sugar----------
def select_sugar(update, context):
    """ function asking for sugar level """

    # create current_item object due to the tea the user chose
    if context.user_data.get('current_item'):
        del context.user_data['current_item']
    context.user_data['current_item'] = Tea(name=update.callback_query.data[5:])
    current_item = context.user_data['current_item']
    logger.info(f'{current_item} is selected.')

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


# 4. ----------select_ice----------
def select_ice(update, context):
    """ function to ask for ice level """

    current_item = context.user_data['current_item']
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


# 5. ---------select_toppings----------
def select_toppings(update, context):
    """ function to ask for toppings"""

    # record ice level to current_item object
    # or append topping to topping list
    data: str = update.callback_query.data
    current_item = context.user_data["current_item"]
    if data.startswith('ice-'):
        current_item.ice = data[4:]
        logger.info(f'ice level: {current_item.ice}')
    elif data.startswith('topping-'):
        current_item.toppings.append(data[8:])

    # send message for user to choose toppings
    text = 'choose some toppings if you want.'
    if added_toppings := current_item.toppings:
        text += '\nYou have chosen the following topping(s):\n'
        text += '\n'.join(
            [f'{i + 1}: {topping}'for i, topping in enumerate(added_toppings)]
        )

    buttons = [[(topping, 'topping-' + topping)] for topping in toppings]
    buttons.append([('That\'s all', 'back-6')])

    send_message(update, text, inline_keyboard(buttons))


# 6. ---------so_far--------
def so_far(update, context):  # not sure what args to pass here
    current_item = context.user_data['current_item']
    cart.append(current_item)
    text = "Tea added! \n"\
           "Let's see what's already in your cart now:"
    for i in range(len(cart)):
        text += f'{i + 1}. {cart[i]}\n'  # can use html
    buttons = [
        [('place order', 'back-7')],
        [('continue buying', 'back-1')]
    ]
    update.callback_query.edit_message_text(
        text, reply_markup=inline_keyboard(buttons)
    )


# 7. --------view_cart----------
def make_order_keyboard(list_):  # return a reply markup
    buttons = []
    for i in range(len(list_)):
        buttons.append([(f'{i + 1}. ' + str(list_[i]), str(i))])
    buttons.append([('set order', 'back-9')])
    return buttons

def view_cart(update, context):
    text = 'Here are your orders.\n' 'Tap any selection if you want to cancel it.\n'
    # chat_id = update.message.chat_id
    update.callback_query.edit_message_text(
        text, reply_markup=inline_keyboard(make_order_keyboard(cart)))
    return 'EDIT_ORDER'

# 8. -------delete----------
def delete(update, context):

    #print(update)
    global text
    choice = int(update.callback_query.data)
    text = 'You have deleted ' + str(cart.pop(choice).name) + '\n' + text
    # text = 'You have deleted ' + str(cart.pop(choice).name) + '\n' + \
    #      'Here are your orders.\n' + 'Tap any selection if you want to cancel it.\n'
    # update.callback_query.reply_action('typing')
    # time.sleep(1)
    update.callback_query.edit_message_text(text)
    if cart:
        # update.callback_query.reply_action('typing')
        # time.sleep(1)
        update.callback_query.edit_message_reply_markup(
            reply_markup=inline_keyboard(make_order_keyboard(cart)))
    else:
        update.callback_query.edit_message_text('Your cart is emtpy now!\n'
                                                'Tap "back" to return to home page.')
        # time.sleep(1)
        update.callback_query.edit_message_reply_markup(
            reply_markup=inline_keyboard([[('back', 'back-1')]]))


# 9. ------------ask_address----------
def ask_address(update, context):
    text = "Since you have confirmed your order, " \
           "could you tell me your address and contact number?"
    try:
        update.callback_query.edit_message_text(text=text)
    except AttributeError:
        update.message.reply_text(text=text)
    return 'ADDRESS'


# 10. ---------save_address--------
def save_address(update, context):
    context.user_data['personal_file'] = update.message.text
    logger.info("address and contact number: {} ".format(context.user_data['personal_file']))
    update.message.reply_text('Ok I see!\n'\
                              'We will contact you by: {0}'.format(context.user_data['personal_file']))
    return confirm_bill(update, context)


# 11. --------confirm_bill----------
def confirm_bill(update, context):
    tot=0
    for product in cart:
        tot+=price_dict[product.name]
    text= 'This is your order information! \n'\
          'Please check your order and address.\n'\
          "If all is right, just click 'confirm' to complete your payment.\n"\
          "Otherwise, click 'back' to edit your order.\n \n"
    for product in cart:
        text += '{0}: \n'.format(product.name)
        text += '(Ice Level: {0}, Sugar Level: {1}, Toppings: {2})\n'.format(product.sugar, product.ice, product.toppings)
    text += '\n Total: {0} \n'. format(tot)
    text += '\n Address and Contact number: {0}'.format(context.user_data['personal_file'])
    buttons=[[InlineKeyboardButton(text='Confirm', callback_data='Confirm'),
              InlineKeyboardButton(text='Back', callback_data='back-7')]]
    keyboard= InlineKeyboardMarkup(buttons)
    update.message.reply_text(text=text, reply_markup=keyboard)


def back(update, context):
    number = int(update.callback_query.data[5:])
    return eval(function_list[number])(update, context)


def cancel(update, context):
    update.message.reply_text("Ok, Bye^_^")
