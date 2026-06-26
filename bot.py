from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import (
    BOT_TOKEN,
    API_ID,
    API_HASH,
    CHANNEL_USERNAME
)

app = Client(
    "TelegramFileBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    try:
        member = await client.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:
            await message.reply_text(
                "✅ Welcome!\n\nYou have joined the channel successfully."
            )

        else:
            raise Exception

    except Exception:
        buttons = InlineKeyboardMarkup(
            [
                [
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
