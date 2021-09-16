# -*- coding: utf-8 -*-

from telegram.ext import Updater , CommandHandler,CallbackQueryHandler , InlineQueryHandler ,MessageHandler , Filters

import os
import requests
from requests.utils import requote_uri


from telegram import InlineKeyboardMarkup , InlineKeyboardButton , InlineQueryResultArticle,InputTextMessageContent

from googlesearch import search
import time

from random import getrandbits


def inline (Update , context):
	
	query_id=Update.inline_query.id
	
	query=Update.inline_query.query
	
	if query == "":
		
		text = "<code>Cómo utilizar el modo en línea?❔</code>\n\nSolo escriba lo que quiera buscar después del nombre de usuario del bot separado por un espacio.\n\n<code>¿Por qué el modo en línea a veces no funciona?❔</code>\n\nEn este caso, le sugiero que use la búsqueda predeterminada."
		
		results = []
		
			
			
		consulta = InlineQueryResultArticle(id=query_id,title= "Cómo utilizar el modo en línea?",  input_message_content=InputTextMessageContent(text , parse_mode="html"),
			description="Ayuda" , thumb_url="https://yourlink.cc/miniatura-google",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="💠Desarrollador💠" , url="https://t.me/Yanco_Dev") ,InlineKeyboardButton(text="💠Repo💠", url="https://t.me/InDemocratic/114")],[InlineKeyboardButton(text="💠Más💠" , url="http://t.me/Y148Bot")]]))
			
		results.append(consulta)
		
		context.bot.answer_inline_query(query_id,
					results=results , switch_pm_text="About the bot" , switch_pm_parameter ="uno")
					
					
		
	else :
	
		
		results = google(query)
		
		answer = []
		
		for result in results[:10]:
				
			answer.append(InlineQueryResultArticle(id=hex(getrandbits(64))[2:],title= result["title"],  input_message_content=InputTextMessageContent(result["text"],"html"),description=result["description"], thumb_url="https://yourlink.cc/miniatura-google"))
			
		
		context.bot.answer_inline_query(query_id,answer , is_personal=True, cache_time=2)
						


def google(query):   
        
    r = requests.get("https://api.abirhasan.wtf/google?query=" + requote_uri(query))   
    
    informations = r.json()["results"]
    
    results = []
    
    for info in informations:
        text = f"<b>Titulo:</b> <code>{info['Titulo']}</code>"
        text += f"\n<b>Descripción:</b> <code>{info['Descripción']}</code>"
        
        results.append(
            {
                "Titulo": info['Titulo'],
                "Descripción": info['Descripción'],
                "texto": text,
                "Enlace": info['Enlace']
            }
        )
    return results


def start(Update,context):
	
	name=Update.effective_user.first_name
	
			
	boton = InlineKeyboardButton(text="inline search" , switch_inline_query_current_chat="")		
	
	
	Update.message.reply_text(text=
	f"<b>👋Hola {name}:\n\n"
	"🔍Escribe lo que quieras "
	"buscar</b>", 
	parse_mode="html",
	reply_markup=InlineKeyboardMarkup([[
	boton]]))


def messagehandler(Update,context):
	
	try:
		
		text=Update.message.text
		
		context.user_data['text']=text
		
		boton1=InlineKeyboardButton(text=
		"Si✅" ,callback_data="call_yes")
		
		
		boton2=InlineKeyboardButton(text=
		"No❌" ,callback_data="call_no")
			
		
		
		
		Update.message.reply_text(text=
		"<b>🤔Estas seguro que quieres"
		" buscar esto?"
		f"\n<u>👉{text}</u></b>",
		parse_mode="html",
		reply_markup=
		InlineKeyboardMarkup([
		[boton1 , boton2]
		]))
	
	except AttributeError:pass
	
def callback_no(Update,context):
	
	query=Update.callback_query
	
	query.edit_message_text(text=
	"<b>🙂Ok, solo reescribe lo que"
	" quieres buscar</b>",
	parse_mode="html"
	)

def callback_yes(Update,context):	
	
	
	consulta=context.user_data.get('text','not found')	
	
	id=Update.effective_user.id
	
	
	query=Update.callback_query
	
	query.edit_message_text(text=
	"<b>🤗Realizando una búsqueda..."
	"</b>",
	parse_mode="html")
	

	
	results = search(consulta, 
	stop = 10 )
	
	result=[]
	
	

	for i in results:
		result.append(i)
		
	
	query.edit_message_text(text=
	"<b>😁La búsqueda ha terminado aquí tienes👇</b>",
	parse_mode="html")	
	
	n = 1
	for i in result:
		
		text=f'<a href="{i}">🔍 Resultado # {n}</a>'	
		
		context.bot.send_message(id,text,"html",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Abrir" , url=i)]]))
		
		time.sleep(0,5)
		n += 1
		
			
def info (Update,context):
	
	Update.message.reply_text(
		text="ℹ️Información :\n\n"
		'Bot: @Y148Bot'
		
		,
		reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="💠Canal💠" , url="https://t.me/Yanco_Dev"),InlineKeyboardButton(text="💠Repo💠",url="https://github.com/inDemocratic/LinksGoogleBot")]])
		,
		
		parse_mode="html",
		disable_web_page_preview=True
		
		
		)



if __name__ == '__main__':

	updater = Updater(token=os.environ["TOKEN"])
	
	update = Updater
	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler('start', start))
	
	dp.add_handler(CommandHandler('info' , info))
	
	dp.add_handler(CallbackQueryHandler(pattern="call_yes" , callback=callback_yes))
	
	dp.add_handler(CallbackQueryHandler(pattern="call_no",callback=callback_no))		
	
	
	dp.add_handler(MessageHandler(Filters.text , messagehandler))
	
	dp.add_handler(InlineQueryHandler(inline))
	
		
	updater.start_polling()
	print("Bot google running")
	updater.idle()
	
