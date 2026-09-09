import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN_YAHAN_DALO"
CHANNEL_ID = "@xauusdmarketanalysis"
MARKET_NAME = "XAUUSD-Market-Analysis-Beep"

votes = {"buy": 0, "sell": 0}

async def send_gold_ad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_url = "https://i.imgur.com/8Km9tLL.png"
    caption = f"🏆 {MARKET_NAME} 🏆\n\n📈 Daily Gold Free Signals\nBUY NOW - TP 2650 - SL 2630\nJoin: {CHANNEL_ID}"
    keyboard = [[
        InlineKeyboardButton(f"BUY 👍 {votes['buy']}", callback_data='vote_buy'),
        InlineKeyboardButton(f"SELL 👎 {votes['sell']}", callback_data='vote_sell')
    ]]
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=InlineKeyboardMarkup(keyboard))

async def vote_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'vote_buy': votes['buy'] += 1
    else: votes['sell'] += 1
    keyboard = [[
        InlineKeyboardButton(f"BUY 👍 {votes['buy']}", callback_data='vote_buy'),
        InlineKeyboardButton(f"SELL 👎 {votes['sell']}", callback_data='vote_sell')
    ]]
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Welcome to {MARKET_NAME} Bot! /ad likho")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ad", send_gold_ad))
app.add_handler(CallbackQueryHandler(vote_button))
app.run_polling()
