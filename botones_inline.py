from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(update, context):
    update.message.reply_text(
        text="Ejemplo de Botones inline",
        reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton(text='💬 Canal 💬', url='http://t.me/YancoBits')],        
            [InlineKeyboardButton(text='Callback_Data', callback_data='callback_data')],                                
    ])
)

def callback_data(update, context):
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(
        text='Esto es el resultado del botón Callback_Data')



if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))


    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('callback_data', callback_data),
            CallbackQueryHandler(pattern='callback_data', callback= callback_data)
        ],
        states={
            callback_data: [MessageHandler(Filters.text, callback_data)]
        },

        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()