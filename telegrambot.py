from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8970053469:AAGl8Hpllmx-m9eRNCH8H6uCz-nG4qt2Xn4"

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, echo))

app.run_polling()