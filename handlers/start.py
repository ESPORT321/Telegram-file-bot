from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import CHANNEL_USERNAME
from database import users


@Client.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user

    # Save user
    if not await users.find_one({"_id": user.id}):
        await users.insert_one({
            "_id": user.id,
            "name": user.first_name
        })

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Join Channel",
                    url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}"
                )
            ],
            [
                InlineKeyboardButton(
                    "✅ Verify",
                    callback_data="check_join"
                )
            ]
        ]
    )

    await message.reply_text(
        "👋 Welcome!\n\n"
        "📌 Pehle hamara channel join karo.\n"
        "Uske baad **Verify** button dabao.",
        reply_markup=buttons
    )
