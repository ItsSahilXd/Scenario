import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from scenario import dispatcher
from scenario.modules.disable import DisableAbleCommandHandler

ROMANTIC_STRINGS = [
                     'Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...',
                     'Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...',
                     'Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...',
                     'Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...',
                     'Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...',
                     'Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...',
                   ]

"""
    Hello kangers, 
    How are you all??
    So if you want to add more shyari add it between '', example 'Yes I'm kanging your codes', 
    I hope it's clear to you!

    So if you're really kanging this atleast don't remove this line it takes a lot of time to code things.
"""

# If you upgrade ptb version it'll show TelegramDeprecationWarning: The @run_async decorator is deprecated. Use the `run_async` parameter of your Handler or `Dispatcher.run_async` instead.
# I suggest don't upgrade ptb
                   
@run_async
def romantic(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(ROMANTIC_STRINGS))
    else:
      message.reply_text(random.choice(ROMANTIC_STRINGS))


ROMANTIC_HANDLER = DisableAbleCommandHandler("romantic", romantic)

dispatcher.add_handler(ROMANTIC_HANDLER)
