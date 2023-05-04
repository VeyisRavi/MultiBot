from AylinRobot import AylinRobot as app
import time
from pyrogram import filters
from AylinRobot.config import Config
from pyrogram import Client, filters, types
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
import os
import asyncio
from pyrogram.errors import FloodWait
from pyrogram import filters
from helpers.filters import command



@app.on_message(filters.command(["admins", "staff"]))
async def admins(client, message):
    try:
        adminList = []
        ownerList = []
        chat_members = await client.get_chat_members(message.chat.id)
        for admin in chat_members:
            if admin.user is not None:
                if admin.user.is_bot:
                    continue
                elif admin.status == "creator":
                    ownerList.append(admin.user)
                else:
                    adminList.append(admin.user)
        lenAdminList = len(ownerList) + len(adminList)
        text2 = f"**{message.chat.title} qrupun idarəçiləri**\n\n"
        try:
            owner = ownerList[0]
            if owner.username is None:
                text2 += f"👑 Yaradıcı\n└ {owner.first_name}\n\n👥 İdarəçilər\n"
            else:
                text2 += f"👑 Yaradıcı\n└ @{owner.username}\n\n👥 İdarəçilər\n"
        except IndexError:
            text2 += f"👑 Yaradıcı\n└ <i>Gizlənib</i>\n\n👥 İdarəçilər\n"
        if len(adminList) == 0:
            text2 += "└ <i>İdarəçilər gizlənib</i>"
            await message.reply_text(text2)
        else:
            for admin in adminList:
                if admin.username is None:
                    text2 += f"├ {admin.first_name}\n"
                else:
                    text2 += f"├ @{admin.username}\n"
            owner = ownerList[0]
            if owner.username is None:
                text2 += f"└ {owner.first_name}\n\n"
            else:
                text2 += f"└ @{owner.username}\n\n"
            text2 += f"✅ | **İdarəçi sayı:** {lenAdminList}\n❌ | Botlar və gizlənmiş idarəçilər qəbul edilmir."
            await message.reply_text(text2)
    except FloodWait as e:
        await asyncio.sleep(e.x)


@app.on_message(filters.command("bots"))
async def bots(client, message):
    try:
        botList = []
        chat_members = await client.get_chat_members(message.chat.id)
        for member in chat_members:
            if member.user.is_bot:
                botList.append(member.user)
        lenBotList = len(botList)
        text3 = f"**{message.chat.title} qrupundakı botlar 🤖**\n\n"
        for bot in botList:
            text3 += f"├ @{bot.username}\n\n"
        text3 += f"✅ | **Bot sayı:** {lenBotList}"
        await message.reply_text(text3)
    except FloodWait as e:
        await asyncio.sleep(e.x)


@app.on_message(command("banlist"))
async def banlist(client, message):
    chat_id = message.chat.id
    chat = await client.get_chat(chat_id)
    banned_users = await client.get_chat_members(chat_id, filter="banned")
    if len(banned_users) == 0:
        await message.reply("Bu qrupda qadağan olunmuş istifadəçi yoxdur.")
    else:
        ban_list_str = "\n".join([f"{i+1}. @{user.user.username}" for i, user in enumerate(banned_users)])
        await message.reply(f"Bu qrupda qadağan olunmuş istifadəçilər:\n{ban_list_str}")

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client, message: types.Message):
    for user in message.new_chat_members:
        if user.id == Config.OWNER_ID:
            bot_name = (await client.get_me()).username
            reply_text = f"Sahibim indicə qrupumuza qoşuldu. Xoş gəldin aramıza🤩"
            reply_gif_url = "https://telegra.ph/file/128e99d265d5dc7807a13.mp4"
            await message.reply_animation(reply_gif_url, caption=reply_text)