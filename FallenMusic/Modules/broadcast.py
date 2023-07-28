import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import app, app2


@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(_, message: Message):
    brep = await message.reply_text("Köməkçi yayıma başladı...")
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Misal:**\n\n/broadcast [Mesaj] ve ya [Mesaja cavab verin]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    async for dialog in app2.get_dialogs():
        chats.append(int(dialog.chat.id))
    for i in chats:
        try:
            await app2.forward_messages(
                i, y, x
            ) if message.reply_to_message else await app2.send_message(i, text=query)
            sent += 1
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await brep.edit_text(f"**Yayımlanan mesaj {sent} söhbətlər.**")
    except:
        await message.reply_text(f"**Yayımlanan mesaj {sent} .**")
