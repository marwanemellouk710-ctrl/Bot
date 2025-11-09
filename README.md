import  telebot

bot = telebot.TeleBot("7966251243:AAGEgU0IF5Wb-tiOIUmnfRjqOACJIuE4qXo")

@bot.message_handler(commands=['start'])

def start(message):
    bot.reply_to(message, "السلام عليكم أنا اسمي بط بوط يمكنك إضافتي في المجموعة اسم المطور مروان ملوك هذه هي قناته على اليوتوب https://www.youtube.com/@sites_google-y8i")

bot.polling()
          
