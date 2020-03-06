from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from share import inline_keyboard, Tea, price_dict
import random as r
import time
import pprint # ??

text = 'Here are your orders.\n' 'Tap any selection if you want to cancel it.\n'


def start(update, context):
    print(update)
    chat_id = update.message.chat_id
    update.message.reply_text(text, reply_markup=inline_keyboard(make_order_keyboard(cart)))


def delete(update, context):
    #print(update)
    global text
    choice = int(update.callback_query.data)
    try:
        # why I have to define text here again??
        text = 'You have deleted ' + str(cart.pop(choice).name) + '\n' + text
        #text = 'You have deleted ' + str(cart.pop(choice).name) + '\n' + \
         #      'Here are your orders.\n' + 'Tap any selection if you want to cancel it.\n'
        #update.callback_query.reply_action('typing')
        time.sleep(1)
        update.callback_query.edit_message_text(text)
        if cart:
            #update.callback_query.reply_action('typing')
            time.sleep(1)
            update.callback_query.edit_message_reply_markup(reply_markup=inline_keyboard(make_order_keyboard(cart)))
        else:
            update.callback_query.edit_message_text('Your cart is emtpy now!\nTap "back" to return to home page.')
            time.sleep(1)
            update.callback_query.edit_message_reply_markup(reply_markup=inline_keyboard([[('back', 'back')]]))
    except IndexError:
        # go to total_and_address page
        update.callback_query.reply_text('got to total_and_address page')



def make_order_keyboard(list_): # return a reply markup
    buttons = []
    for i in range(len(list_)):
        buttons.append([(f'{i + 1}. ' + str(list_[i]), str(i))])
    buttons.append([('set order', str(i + 1))]) # will raise IndexError
    return buttons


def main():
    updater = Updater("1121470779:AAG5F0CaZAcU9oQW34lXVzTrKMgZGoyDtNg", use_context=True)
    dp = updater.dispatcher
    #dp.add_handler(MessageHandler(Filters.text, delete))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(delete))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__': # need create test set
    selections = r.choices(list(price_dict.keys()), k=4)
    toppings_list = ['Pearl', 'Red Bean', 'Coconut', 'Milk']
    ice_list = ['hot', 'no', 'less', 'regular', 'more']
    cart = [Tea(tea, r.randint(0, 4) * 25, r.choice(ice_list),
                r.choices(toppings_list, k=r.randint(0, 3))) for tea in selections]
    print(cart)
    main()