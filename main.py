from femis_functions import *
from telegram.ext import (ConversationHandler, CommandHandler, MessageHandler,
                          CallbackQueryHandler, Updater, Filters)
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            'SELECT_TEA': [
                CallbackQueryHandler(select_toppings, pattern='topping'),
                CallbackQueryHandler(select_sugar, pattern='^name-'),
                CallbackQueryHandler(select_ice, pattern='^sugar-'),
                CallbackQueryHandler(select_toppings, pattern='^ice-'),
                CallbackQueryHandler(select_tea, pattern='(?!back)')
            ],
            'EDIT_ORDER': [
                CallbackQueryHandler(delete, pattern='(?!back)')
            ],
            'ADDRESS': [
                MessageHandler(Filters.text, save_address)
            ]
        },
        fallbacks=[CallbackQueryHandler(back, pattern='back-')]
    )

    u = Updater(token, use_context=True)
    dp = u.dispatcher
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('cancel', cancel))

    u.start_polling()
    u.idle()


if __name__ == '__main__':
    main()