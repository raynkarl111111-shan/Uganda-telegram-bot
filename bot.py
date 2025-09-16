import asyncio
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔐 REPLACE THESE WITH YOUR KEYS
DMARKET_PUBLIC_KEY = "10d5c6cee610d74936b547f743d03fc0d238036f2752b9b25c324efdb6327bb8"
DMARKET_SECRET_KEY = "3da72ac597dd15d65d7b7b5535519f62b68939f2a0d547106b5a5daa699c1f1c10d5c6cee610d74936b547f743d03fc0d238036f2752b9b25c324efdb6327bb8"
TRUST_WALLET_ADDRESS = "TC2SREvrtvyNG3AexmgUkzGWWDJoAUhr8j"
TELEGRAM_BOT_TOKEN = "8148037965:AAFRY3tzYOIgL9qPm6NFpwKre36wkLFkGkc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 UGANDA AUTOBOT LIVE 🇺🇬\nReply BUY to start trading")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper().strip()
    if text == "BUY":
        await update.message.reply_text("✅ Simulated: Bought AK-47 | Redline for $100\nReply WITHDRAW to send to Steam")
    elif text == "WITHDRAW":
        await update.message.reply_text("📤 Simulated: Sent to Steam\nReply DEPOSIT to send to Skinport")
    elif text == "DEPOSIT":
        await update.message.reply_text("📥 Simulated: In Skinport\nReply SELL 120 to list at $120")
    elif text.startswith("SELL "):
        price = text.split(' ')[1]
        await update.message.reply_text(f"💰 Simulated: Listed for ${price}\nReply CASHOUT to withdraw to {TRUST_WALLET_ADDRESS[:8]}...")
    elif text == "CASHOUT":
        await update.message.reply_text(f"💵 Simulated: USDT sent to {TRUST_WALLET_ADDRESS}\nGo to Binance P2P → Sell → Get Mobile Money 🇺🇬")
    else:
        await update.message.reply_text("❓ Reply BUY to start")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot started — send /start on Telegram")
    app.run_polling()

if __name__ == "__main__":
    main()
