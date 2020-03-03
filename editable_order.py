from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from share import inline_keyboard, Tea

from share import price_dict, Tea
import random as r


def reply(update, context):
    text = 'Here are your orders.\n' 'Tap any selection if you want to cancel it.\n'
    buttons = []
    for i in range(len(cart)):
        buttons.append([(f'{i + 1}. '+str(cart[i]), str(i))])
    update.message.reply_text(text, reply_markup=inline_keyboard(buttons))


def main():
    updater = Updater("1121470779:AAG5F0CaZAcU9oQW34lXVzTrKMgZGoyDtNg", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__': # need create test set
    selections = r.choices(list(price_dict.keys()), k=4)
    toppings_list = ['Pearl', 'Red Bean', 'Coconut', 'Milk']
    ice_list = ['hot', 'no', 'less', 'regular', 'more']
    cart = [Tea(tea, r.randint(0, 5) * 25, r.choice(ice_list), r.choices(toppings_list, k=r.randint(0, 3))) for tea in
            selections]
    print(cart)
    main()