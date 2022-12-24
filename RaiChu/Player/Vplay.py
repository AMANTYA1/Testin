from pyrogram import Client, filters
from pyrogram.enums import ParseMode

@Client.on_message(filters.command("vplay"))
async def banall(bot, m):
    await bot.send_message(text=f"Fixing Soon Please wait sir 🚏 [{m.from_user.first_name}](tg://user?id={m.from_user.id})", chat_id=m.chat.id)
