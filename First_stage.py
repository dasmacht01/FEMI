import logging
import telegram
from telegram import (InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters)

# Test
bot= telegram.Bot(token='963449057:AAHIO6AWfT9SoM6davoXBr2Y1TdRd9eROnQ')
START_OVER = False
cart=[{'name': 'yolo', 'sugar': '25', 'ice': 'no', 'topping': 'no'}]
price_dict= {'yolo': 10}
context.user_data['personal_file']= "SUTD"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Start_data
special= 'Fruits BOOM'
photo_address_1 = "file:///Users/linyutian/Desktop/pycharm/FEMI/IMG_2522.JPG"
photo_address_2 = "file:///Users/linyutian/Desktop/pycharm/FEMI/IMG_2521%202.JPG"


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

    if context.user_data.get(START_OVER):
        buttons.append([InlineKeyboardButton(text='check_out', callback_data='check_out')])
        keyboard = InlineKeyboardMarkup(buttons)
        update.callback_query.edit_message_text(text=text_start_over, reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(buttons)
        update.message.reply_text(text=text_start_1)
        with open('IMG_2522.JPG', 'rb') as f:
            bot.send_photo(chat_id=update.effective_chat.id, photo=f, timeout=50)
        with open('IMG_2521.JPG', 'rb') as p:
            bot.send_photo(chat_id=update.effective_chat.id, photo=p, timeout=50)
        update.message.reply_text(text=text_start_2, reply_markup=keyboard)

    context.user_data[START_OVER]= False


def ask_address(update, context):
    text="Since you have confirmed your order, could you tell me your address and contact number?"
    try:
        update.callback_query.edit_message_text(text=text)
    except:
        update.message.reply_text(text=text)


def save_address(update, context):
    context.user_data['personal_file'] = update.message.text
    logger.info("address and contact number: {} ".format(context.user_data['personal_file']))
    update.message.reply_text('Ok I see!\n'\
                              'We will contact you by: {0}'.format(context.user_data['personal_file']))


def confirm_bill(update, context):
    tot=0
    for product in cart:
        tot+=price_dict[product['name']]
    text= 'This is your order information! \n'\
          'Please check your order and address.\n'\
          "If all is right, just click 'confirm' to complete your payment.\n"\
          "Otherwise, click 'back' to edit your order.\n \n"
    for product in cart:
        text += '{0}: \n'.format(product['name'])
        text += '(Ice Level: {0}, Sugar Level: {1}, Toppings: {2})\n'.format(product['sugar'], product['ice'], product['topping'])
    text += '\n Total: {0} \n'. format(tot)
    text += '\n Address and Contact number: {0}'.format(context.user_data['personal_file'])
    buttons=[[InlineKeyboardButton(text='Confirm', callback_data='Confirm'),
              InlineKeyboardButton(text='Back', callback_data='Back')]]
    keyboard= InlineKeyboardMarkup(buttons)
    update.message.reply_text(text=text, reply_markup=keyboard)

