from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH

app = Client(
    "TelegramFileBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def all_messages(client, message):
    if message.text == "/start":
        await message.reply_text(
            "🤖 Bot Online!\n\nWelcome to Telegram File Store Bot."
        )

print("Bot Started...")
app.run()                [
                    InlineKeyboardButton(
                        "📢 Join Channel",
                        url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✅ Try Again",
                        callback_data="check_join"
                    )
                ]
            ]
        )

        await message.reply_text(
            "⚠️ Pehle channel join karo.",
            reply_markup=buttons
        )


app.run()
