from pyrogram import Client
from pyrogram.types import CallbackQuery

from config import CHANNEL_USERNAME

@Client.on_callback_query()
async def check_join(client, query: CallbackQuery):

    if query.data != "check_join":
        return

    user_id = query.from_user.id

    try:
        member = await client.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "owner"]:
            await query.message.edit_text(
                "✅ Verification successful!\n\n📂 Your file will be sent shortly."
            )

            # Yahan baad me auto file send ka code add karenge.

        else:
            raise Exception

    except Exception:
        await query.answer(
            "❌ Pehle channel join karo!",
            show_alert=True
        )
