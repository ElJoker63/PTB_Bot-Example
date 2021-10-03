from telegram.ext import Updater, CommandHandler, Filters

MY_ID= 940342995
#MY_ID= 2030496387

def  alert(update , context):
	
	update.message.reply_text('Bloqueado')

def start(update, context):
    
    user_id=update.effective_user.id
    
    name=update.effective_user.first_name
    
    if user_id==MY_ID:
        update.message.reply_text(f'Hola {name}')
    	
    else :
    	alert(update,context)

if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context=True) 
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    print('ONLINE')
    updater.idle()