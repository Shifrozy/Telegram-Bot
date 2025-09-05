# crypto_bot.py
import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Fetch price from CoinGecko API
def get_price(symbol="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url).json()
    return response.get(symbol, {}).get("usd", "N/A")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /price <coin> to get real-time prices.")

# /price command
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Please enter a coin name, e.g. /price bitcoin")
        return
    
    coin = context.args[0].lower()
    price = get_price(coin)
    await update.message.reply_text(f"The price of {coin.capitalize()} is ${price}")

# Main function
def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN not found. Please set it in the .env file.")
        return
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    
    app.run_polling()

if __name__ == "__main__":
    main()
