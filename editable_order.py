from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from share import inline_keyboard, Tea


def reply(update, context):
    text = 'Here are your orders.\n' 'Tap any selection if you want to cancel it.\n'
    buttons = []
    for i in range(len(cart)):
        buttons.append([(f'{i + 1}. '+str(cart[i]), str(i))])
    print(buttons)
    update.message.reply_text(text, reply_markup=inline_keyboard(buttons))


def main():
    updater = Updater("TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__': # need create test set
    tea1 = Tea('yolo')
    tea2 = Tea('yes')
    tea3 = Tea('haha')
    cart = [tea1, tea2, tea3]
    main()