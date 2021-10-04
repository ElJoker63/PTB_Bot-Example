from telegram.ext import Updater, CommandHandler, PrefixHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup



def start(update, context):
    name=update.effective_user.first_name
    update.message.reply_text(f'Hola {name}',
    reply_markup=ReplyKeyboardMarkup([ 
            [KeyboardButton(text='Contacto'),  
            KeyboardButton(text='Canal')], 
            [KeyboardButton(text='Proyectos')],       
    ])                               
)

def Contacto(update, context):
    update.message.reply_text('@Yanco148')

def Canal(update, context):
    update.message.reply_text('https://t.me/Yanco_Bits')    

def Proyectos(update, context):
    update.message.reply_text('https://t.me/Yanco_Bits_Projects')     

if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(PrefixHandler('', 'Contacto', Contacto))
    dp.add_handler(PrefixHandler('', 'Canal', Canal))
    dp.add_handler(PrefixHandler('', 'Proyectos', Proyectos))

    updater.start_polling()
    print('ONLINE')
    updater.idle()