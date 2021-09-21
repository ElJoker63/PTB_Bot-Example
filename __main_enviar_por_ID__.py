from telegram.ext import Updater, CommandHandler
from telegram import ParseMode
CHAT_ID= 

def start(update, context):
  updater.bot.send_message(CHAT_ID, "Hola que tal, soy proactivo?")

if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    

    updater.start_polling()
    print('Online')
    updater.idle()
