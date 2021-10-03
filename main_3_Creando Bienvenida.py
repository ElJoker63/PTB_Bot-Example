from telegram.ext import Updater, CommandHandler, PrefixHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

# Creando Bienvenida de Usuario
def new_member(update, callback):
    #name=update.effective_user.first_name
    update.message.reply_text(f'Bienvenido @{update.message.new_chat_members[0].username}',
    reply_markup=InlineKeyboardMarkup([                          
            [InlineKeyboardButton(text='💠Twitter💠', url='https://twitter.com/Yanco148')],
            [InlineKeyboardButton(text='💠GitHub💠', url='https://github.com/Yanco148')],                   
    ])
)




if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context=True)

    dp = updater.dispatcher
    
    dp.add_handler(MessageHandler(filters = Filters.status_update.new_chat_members, callback=new_member))


    
    updater.start_polling()
    print('Online')
    updater.idle()
