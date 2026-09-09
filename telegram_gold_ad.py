import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# === APNI DETAILS YAHAN DALO ===
TOKEN = "YOUR_BOT_TOKEN_YAHAN_DALO"
CHANNEL_USERNAME = "@xauusdmarketanalysis"
# =================================

votes = {"buy": 0, "sell": 0}

# 1. PROFILE SHOW HOGA /start se
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logo_url = "https://i.imgur.com/8Km9tLL.jpg"
    text = (
        "🏆 **XAUUSD Market Analysis** 🏆\n\n"
        "👑 Premium Gold Signals Provider\n"
        "📊 Daily Analysis | 90% Accuracy\n"
        "💰 XAUUSD | Gold Trading Expert\n\n"
        "👇 Neeche se Ad Dekho ya Vote Karo:"
    )
    keyboard = [
        [InlineKeyboardButton("📢 GOLD KA AD DEKHO", callback_data='show_ad')],
        [InlineKeyboardButton("📈 JOIN CHANNEL", url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}")]
    ]
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=logo_url,
        caption=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

# 2. GOLD AD WITH VOTING
async def send_gold_ad_logic(chat_id, context):
    photo_url = "https://i.imgur.com/8Km9tLL.jpg"
    caption = (
        f"🔥 **XAUUSD-Market-Analysis-Beep** 🔥\n\n"
        f"📊 **TODAY'S GOLD SIGNAL**\n"
        f"💵 GOLD (XAUUSD)\n"
        f"⏰ Time: London Session\n\n"
        f"👇 Aapka Kya Khayal Hai? Vote Karo:"
    )
    keyboard = [[
        InlineKeyboardButton(f"BUY 👍 {votes['buy']}", callback_data='vote_buy'),
        InlineKeyboardButton(f"SELL 👎 {votes['sell']}", callback_data='vote_sell')
    ]]
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def ad_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_gold_ad_logic(update.effective_chat.id, context)

# 3. VOTE LOGIC
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'show_ad':
        await send_gold_ad_logic(query.message.chat_id, context)
        return
    if query.data == 'vote_buy':
        votes['buy'] += 1
    elif query.data == 'vote_sell':
        votes['sell'] += 1
    keyboard = [[
        InlineKeyboardButton(f"BUY 👍 {votes['buy']}", callback_data='vote_buy'),
        InlineKeyboardButton(f"SELL 👎 {votes['sell']}", callback_data='vote_sell')
    ]]
    try:
        await query.edit_message_caption(
            caption=query.message.caption,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    except:
        pass

# 4. LAUNCH APP
def main():
    print("Bot Starting... XAUUSD Market Analysis")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("ad", ad_command))
    app.add_handler(CommandHandler("profile", start_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()
