from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from share import inline_keyboard, Tea, price_dict
from test import delete
import random as r
import time


def start(update, context):
    buttons = []
    for i in range(len(cart)):
        buttons.append([(f'{i + 1}. '+str(cart[i]), str(i))])
    buttons.append([('set order', str(i + 1))]) # will raise IndexError
    update.message.reply_text(text, reply_markup=inline_keyboard(buttons))


def delete(update, context):
    choice = update.callback_query.data
    if cart:
        try:
            # why I have to define text here again??
            text = 'You have deleted ' + str(cart.pop(int(choice)).name) + '\n' + \
                   'Here are your orders.\n' + 'Tap any selection if you want to cancel it.\n'

            buttons = []
            for i in range(len(cart)):
                buttons.append([(f'{i + 1}. ' + str(cart[i]), str(i))])
            buttons.append([('set order', str(i + 1))])

            update.callback_query.edit_message_text(text)
            time.sleep(1)
            update.callback_query.edit_message_reply_markup(reply_markup=inline_keyboard(buttons))
        except IndexError:
            print('go to total_and_address page')
            # go to total_and_address page
    else:
        update.callback_query.edit_message_text('Your cart is emtpy now!\nTap "back" to return to home page.')
        time.sleep(2)
        update.callback_query.edit_message_reply_markup(reply_markup=inline_keyboard([[('back', 'back')]]))

def main():
    updater = Updater("1121470779:AAG5F0CaZAcU9oQW34lXVzTrKMgZGoyDtNg", use_context=True)
    dp = updater.dispatcher
    #dp.add_handler(MessageHandler(Filters.text, delete))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(delete))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__': # need create test set
    '''global text
    text = 'Here are your orders.\n' 'Tap any selection if you want to cancel it.\n''''
    selections = r.choices(list(price_dict.keys()), k=4)
    toppings_list = ['Pearl', 'Red Bean', 'Coconut', 'Milk']
    ice_list = ['hot', 'no', 'less', 'regular', 'more']
    cart = [Tea(tea, r.randint(0, 4) * 25, r.choice(ice_list), r.choices(toppings_list, k=r.randint(0, 3))) for tea in
            selections]
    print(cart)
    main()