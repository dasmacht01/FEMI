
# Send a message containing the current cart content
# after completing customizing each product
# Append instructions and inline buttons under that

import telegram
# from share import cart, Tea, inline_keyboard




def so_far(update, context): # not sure what args to pass here
    text = "Tea added! \n"
                  "Let's see what's already in your cart now:")
    for i in range(len(cart)):
        text += (f'{i+1}. {cart[i]}\n') # can use html
    buttons = [[('place order', 's_place_order')],[('continue buying', 's_continue_buying')]]
    update.message.reply_message(text, reply_markup=inline_keyboard(buttons))


