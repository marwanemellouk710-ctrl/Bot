import telebot

bot = telebot.TeleBot("7966251243:"اكتب هنا توكن البوت الخاص بك")
MY_LINK = "https://marwanemellouk710-ctrl.github.io/black-coffee-/"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"مرحبا بك في البوت الخاص المرجوا زيارة موقعي الرسمي هنا انشر جميع التحديثات: {MY_LINK}")

bot.polling()
