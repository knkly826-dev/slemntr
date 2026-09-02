import os
import io
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from gtts import gTTS

TOKEN = os.environ.get("8824254463:AAFSitssn-jK0LKOtkoR1fWmIp-DmAgY-og")  # التوكن من Render

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎙️ أرسل لي نصاً وسأحوله إلى صوت!")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text("⏳ جارٍ التحويل...")
    
    tts = gTTS(text=text, lang="ar")
    audio = io.BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)
    
    await update.message.reply_voice(voice=audio, filename="voice.ogg")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("🤖 البوت يعمل...")
    app.run_polling()

if __name__ == "__main__":
    main()
