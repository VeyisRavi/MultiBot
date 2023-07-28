from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from youtubesearchpython.__future__ import VideosSearch

import config
from FallenMusic import BOT_MENTION, BOT_NAME, app
from FallenMusic.Helpers import gp_buttons, pm_buttons
from FallenMusic.Helpers.dossier import *


@app.on_message(filters.command(["start"]) & ~filters.forwarded)
@app.on_edited_message(filters.command(["start"]) & ~filters.forwarded)
async def fallen_st(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        if len(message.text.split()) > 1:
            cmd = message.text.split(None, 1)[1]
            if cmd[0:3] == "inf":
                m = await message.reply_text("🔎")
                query = (str(cmd)).replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                for result in (await results.next())["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["channel"]["link"]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                searched_text = f"""
➻ **ᴍƏʟᴜᴍᴀᴛɪ ɪᴢʟƏʏɪɴ** 

📌 **ʙᴀŞʟɪQ :** {title}

⏳ **ᴍÜᴅᴅƏᴛ :** {duration} ᴍɪɴᴜᴛᴇs
👀 **ʙᴀxɪŞʟᴀʀ :** `{views}`
⏰ **ᴅƏʀᴄ ᴏʟᴜɴᴜʙ :** {published}
🔗 **ʟɪɴᴋ :** [Youtube-da izləyin]({link})
🎥 **ᴋᴀɴᴀʟ :** [{channel}]({channellink})

📡 ᴀxᴛᴀʀɪŞ ᴅƏꜱᴛƏᴋʟƏɴɪʀ {BOT_NAME}"""
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="You Tube", url=link),
                            InlineKeyboardButton(
                                text="Dəstək", url=config.SUPPORT_CHAT
                            ),
                        ],
                    ]
                )
                await m.delete()
                return await app.send_photo(
                    message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=key,
                )
        else:
            await message.reply_text( #reply_photo
               # photo=config.START_IMG,
               # caption=
                PM_START_TEXT.format(
                    message.from_user.first_name,
                    BOT_MENTION,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
            )
    else:
        await message.reply_text( #reply_photo
           # photo=config.START_IMG,
           # caption=
            START_TEXT.format(
                message.from_user.first_name,
                BOT_MENTION,
                message.chat.title,
                config.SUPPORT_CHAT,
            ),
            reply_markup=InlineKeyboardMarkup(gp_buttons),
)

@app.on_callback_query(filters.regex("tagbutton"))
async def tagbutton(_, query: CallbackQuery):
    await query.edit_message_text(TAG_MSJ, 
    reply_markup=InlineKeyboardMarkup([
    [
    InlineKeyboardButton("◄◐ ɢᴇʀɪ", callback_data="fallen_home"),
    InlineKeyboardButton("📢 ᴋᴀɴᴀʟ", url=config.SUPPORT_CHANNEL)
    ]]))
