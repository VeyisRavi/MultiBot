from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from FallenMusic import BOT_USERNAME
import config

close_key = InlineKeyboardMarkup([[InlineKeyboardButton(text="🎵 ʙᴀĞʟᴀʏɪʀ 🎵", callback_data="close")]])

buttons = InlineKeyboardMarkup(
          [[
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
          ]])

gp_buttons = [
    [
     InlineKeyboardButton(text="🗂 ƏᴍʀʟƏʀ ᴠƏ ᴋÖᴍƏᴋʟƏʀ 🗂", callback_data="fallen_help")
    ],[
     InlineKeyboardButton(text="📢 ᴋᴀɴᴀʟ", url=config.SUPPORT_CHANNEL),
     InlineKeyboardButton(text="💻 ᴅƏꜱᴛƏᴋ", url=config.SUPPORT_CHAT),
    ],[
     InlineKeyboardButton(text="🔸️ Qʀᴜᴘᴀ ƏʟᴀᴠƏ ᴇᴛ 🔸️",url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)
    ],[
     InlineKeyboardButton(text="👨‍💻 ʙᴏᴛ ꜱᴀʜɪʙɪ", user_id=config.OWNER_ID),
    ],]

pm_buttons = [
    [
     InlineKeyboardButton(text="🗂 ƏᴍʀʟƏʀ ᴠƏ ᴋÖᴍƏᴋʟƏʀ 🗂", callback_data="fallen_help")
    ],[
     InlineKeyboardButton(text="📢 ᴋᴀɴᴀʟ", url=config.SUPPORT_CHANNEL),
     InlineKeyboardButton(text="💻 Dəstək", url=config.SUPPORT_CHAT),
    ],[
     InlineKeyboardButton(text="🔸️ Qʀᴜᴘᴀ ƏʟᴀᴠƏ ᴇᴛ 🔸️",url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)
    ],[
     InlineKeyboardButton(text="👨‍💻 ʙᴏᴛ ꜱᴀʜɪʙɪ", user_id=config.OWNER_ID),
    ],]

helpmenu = [
    [
    InlineKeyboardButton(text="📚 ꜱƏꜱʟɪ ƏᴍʀʟƏʀ",callback_data="fallen_cb help",),
    InlineKeyboardButton(text="🔊 ᴛᴀĞ ƏᴍʀʟƏʀɪ ",callback_data="tagbutton",)
    ],[
    InlineKeyboardButton(text="📋 ʙᴏᴛ ᴀᴅᴍɪɴʟƏʀ", callback_data="fallen_cb sudo"),
    InlineKeyboardButton(text="👨‍💻 ʙᴏᴛ ꜱᴀʜɪʙɪ", callback_data="fallen_cb owner"),
    ],[
    InlineKeyboardButton(text="◄◐ ɢᴇʀɪ", callback_data="fallen_home"),
    InlineKeyboardButton(text="🗑 ᴍᴇɴʏᴜɴᴜ ʙᴀĞʟᴀʏɪʀ", callback_data="close"),
    ],]

help_back = [
    [
    InlineKeyboardButton(text="◄◐ ɢᴇʀɪ", callback_data="fallen_help"),
    InlineKeyboardButton(text="🗑 ᴍᴇɴʏᴜɴᴜ ʙᴀĞʟᴀʏɪʀ", callback_data="close"),
    ],]
