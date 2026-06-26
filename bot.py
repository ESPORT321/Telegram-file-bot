from pyrogram import Client
from pyrogram import filters
from config import BOT_TOKEN, API_ID, API_HASH

app = Client(
    "TelegramFileBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🤖 Bot Online!\n\nWelcome to Telegram File Store Bot."
    )

print("Bot Started...")
app.run()
