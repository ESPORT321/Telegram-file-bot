from pyrogram import Client, filters
from config import ADMIN_ID
from database import users

@Client.on_message(filters.command("stats") & filters.user(ADMIN_ID))
async def stats(client, message):
    total = await users.count_documents({})
    await message.reply_text(
        f"📊 Total Users: {total}"
    )
