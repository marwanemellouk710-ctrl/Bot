import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# نجيب التوكن من Secrets
BOT_TOKEN = os.environ["BOT_TOKEN"]


# أمر البداية /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 مرحبا! البوت ديالك خدام بنجاح!")


# إنشاء التطبيق
app = ApplicationBuilder().token(BOT_TOKEN).build()

# إضافة أمر /start
app.add_handler(CommandHandler("start", start))

# تشغيل البوت
print("✅ البوت شغال الآن...")
app.run_polling()