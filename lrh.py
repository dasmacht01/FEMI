from share import *
import telegram
# TODO:
#  select_tea
#  select_sugar
#  select_ice
#  select_toppings

# def select_tea(update, context):
#    f

def select_sugar(update: telegram.Update, context):

    # TODO:
    #  ask callback_data form of last query
    #  discuss about global variable current_item
    current_item.name = update.callback_query.data

    text = f'You have chosen {current_item.name}, please customize your product.'
    buttons = [[('No Sugar', 'sugar-0')],
               [('25%', 'sugar-25')],
               [('50%', 'sugar-50')],
               [('75%', 'sugar-75')],
               [('Full Sugar', 'sugar-100')]]
    update.callback_query.edit_message_text(text)
    update.message.reply_message('Choose sugar level:',
                                 reply_markup=inline_keyboard(buttons))

def select_ice(update, context):
    current_item.suagr = int(update.callback_query.data[6:])
    buttons = [[('Hot', 'ice-hot')],
               [('No Ice', 'ice-no')],
               [('Less Ice', 'ice-less')],
               [('Regular-ice', 'ice-regular')],
               [('More Ice', 'ice-more')]]
    update.callback_query.edit_message_text('Choose tea temperature:',
                                            reply_markup=inline_keyboard(buttons))


def select_toppings(update, context):
    current_item.ice = update.callback_query.data[4:]
    buttons = [[('Pearl', 'pearl'), ('Red Bean', 'red-bean')],
               [('Coconut', 'coconut'), ('Milk', 'milk')],
               [('That\'s all', 'rh-Done')]]
    update.callback_query.edit_message_text('choose some toppings if you want.',
                                            reply_markup=inline_keyboard(buttons))
