from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def join_button(channel):
    return InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "📢 Join Channel",
                url=f"https://t.me/{channel.replace('@', '')}"
            )
        ]]
    )
