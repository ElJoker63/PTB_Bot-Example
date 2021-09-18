from telegram.ext import Updater, CommandHandler
from telegram import ChatAction


# Enviando una foto
def photo(update, context):
    update.message.reply_chat_action(ChatAction.UPLOAD_PHOTO)
    update.message.reply_photo(open('photo.jpg', 'rb'),
    caption='mi foto'
)

# Enviando Audio
def audio(update, context):
    update.message.reply_chat_action(ChatAction.UPLOAD_AUDIO)
    update.message.reply_audio(open('audio.mp3', 'rb'),
    caption= 'mi audio'
    )

# Enviando Video
def video(update, context):
    update.message.reply_chat_action(ChatAction.UPLOAD_VIDEO)
    update.message.reply_audio(open('video.mp4', 'rb'),
    caption= 'mi video'
    )

# Enviando Documento
def archivo(update, context):
    update.message.reply_chat_action(ChatAction.UPLOAD_DOCUMENT)
    update.message.reply_document(open('photo.jpg', 'rb'),
    caption= 'mi archivo'
    )    



if __name__ == '__main__':

    updater = Updater(token='1977097417:AAExMd699E7HJt7ZUSbRiieXNbxtaYhHuEs', use_context=True)

    dp = updater.dispatcher
# Comando Foto
    dp.add_handler(CommandHandler('photo', photo))
# Comando Audio
    dp.add_handler(CommandHandler('audio', audio))
# Comando Audio
    dp.add_handler(CommandHandler('video', video))
# Comando Audio
    dp.add_handler(CommandHandler('archivo', archivo))

    updater.start_polling()
    print('Online')
    updater.idle()