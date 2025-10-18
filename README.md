1
👇🏻
import telebot

bot = telebot.TeleBot(":"اكتب هنا توكن البوت الخاص بك")
MY_LINK = "https://marwanemellouk710-ctrl.github.io/black-coffee-/"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"مرحبا بك في البوت الخاص المرجوا زيارة موقعي الرسمي هنا انشر جميع التحديثات: {MY_LINK}")
    2
    👇🏻
bot.polling()
import telebot
import re

# توكن البوت
TOKEN = "اكتب توكن هنا "
bot = telebot.TeleBot(TOKEN)

# تعبير لاكتشاف الروابط
link_pattern = re.compile(r'http[s]?://|www\.')

# كلمات حسب المشاعر
happy_words = ["فرح", "سعيد", "😄", "😀"]
sad_words = ["حزن", "حزين", "😢", "😭"]
surprise_words = ["مفاجأة", "😲", "😮"]
funny_words = ["هههه", "lol", "ضحك", "😂", "🤣"]

# الردود
happy_reply = "😄 واو! يبدو أنك سعيد!"
sad_reply = "😢 لا تحزن، كل شيء سيكون بخير."
surprise_reply = "😲 ياااه! مفاجأة!"
funny_reply = "😂 ههه، مضحك!"
default_reply = "👍 تمام!"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.chat.type in ["group", "supergroup"]:
        text = message.text.lower() if message.text else ""

        # حذف الروابط
        if text and link_pattern.search(text):
            try:
                bot.delete_message(message.chat.id, message.message_id)
                bot.reply_to(message, "تم حذف الرسالة لأنها تحتوي على رابط")
            except Exception as e:
                print(f"خطأ عند حذف الرسالة: {e}")
        else:
            # الرد حسب نوع الرسالة
            reply_text = default_reply
            if any(word in text for word in funny_words):
                reply_text = funny_reply
            elif any(word in text for word in happy_words):
                reply_text = happy_reply
            elif any(word in text for word in sad_words):
                reply_text = sad_reply
            elif any(word in text for word in surprise_words):
                reply_text = surprise_reply

            try:
                bot.reply_to(message, reply_text)
            except Exception as e:
                print(f"خطأ عند الرد على الرسالة: {e}")

bot.polling()
