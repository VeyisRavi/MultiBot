import logging, time
from io import BytesIO
from AylinRobot.config import Config
from aiohttp import ClientSession
from AylinRobot import AylinRobot as app
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

#--------------------------------------------------------------


aiohttpsession = ClientSession()


async def get_http_status_code(url: str) -> int:
    async with aiohttpsession.head(url) as resp:
        return resp.status
    

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

@app.on_message(filters.command("carbon"))
async def carbon_func(client, msg):
    await msg.delete() 
    reply = msg.reply_to_message
    if reply:
        m = await msg.reply_text("️🌀 Carbonu hazırlayıram...")
        carbon = await make_carbon(msg.reply_to_message.text)
        await m.edit("⚡ Artıq hazırdır! Göndərirəm.")
        await client.send_document(msg.chat.id, carbon, caption=f"[Aylin](https://t.me/{Config.BOT_USERNAME}) tərəfindən {msg.from_user.mention} üçün yaradıldı. ✅")
        await m.delete()
        carbon.close()
    else:
        try:
            text = msg.text.split(" ", 1)[1]
            m = await msg.reply_text("️🌀 Carbonu hazırlayıram...")
            carbon = await make_carbon(text)
            await m.edit("⚡ Artıq hazırdır! Göndərirəm.")
            await client.send_document(msg.chat.id, carbon, caption=f"[Rahid](https://t.me/{Config.BOT_USERNAME}) tərəfindən {msg.from_user.mention} üçün yaradıldı. ✅")
            await m.delete()
            carbon.close()
        except IndexError:
            await msg.reply_text("️❌ Mətn daxil etmədin...")