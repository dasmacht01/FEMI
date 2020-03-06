import unittest
from lrh import (select_ice, select_sugar, select_tea, select_toppings)
from share import *
from telegram import (Bot, InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, CallbackQueryHandler, ConversationHandler)


class LrhTestCase(unittest.TestCase):

    from os import environ
    token = environ['teletoken']
    bot = Bot(token=token)
    u = Updater(token=token, use_context=True)
    dp = u.dispatcher

    def test_lrh(self):
        handlers = [
            CommandHandler('start', select_tea),
            CallbackQueryHandler(select_sugar, pattern='^name-'),
            CallbackQueryHandler(select_ice, pattern='^sugar-'),
            CallbackQueryHandler(select_toppings, pattern='^ice-')
        ]
        for handler in handlers:
            self.dp.add_handler(handler)
        self.u.start_polling()
        self.u.idle()


if __name__ == '__main__':
    unittest.main()
