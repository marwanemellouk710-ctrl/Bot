import  telebot

bot = telebot.TeleBot("7966251243:AAE2_d6Ei3n0N1ZBKvHKSj1meV6dof_YwvU")

@bot.message_handler(commands=['start'])

def start(message):
    bot.reply_to(message, "السلام عليكم أنا اسمي بط بوط يمكنك إضافتي في المجموعة اسم المطور مروان ملوك هذه هي قناته على اليوتوب https://www.youtube.com/@sites_google-y8i")

bot.polling()
          