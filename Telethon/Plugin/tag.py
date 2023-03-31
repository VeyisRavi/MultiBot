## Sahib HuseynH Satış Qadağandır

import logging, asyncio, random
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from AylinRobot.config import Config
from Telethon.Mesajlar import soz,  emoji, bayrag

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)
 
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []
 
ozel_list = [2074934667]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
	
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
	
	
	
@client.on(events.NewMessage(pattern="^.tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ etmək üçün bir mesaj yazın**\n**ℹ️ Misal:** `/tag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
		
		
		
		
		
		
@client.on(events.NewMessage(pattern="^.tektag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün üserlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/tektag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 	
	
	
@client.on(events.NewMessage(pattern="^.htag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/htag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(heyvan)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(heyvan)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
	
	
@client.on(events.NewMessage(pattern="^.sehidler ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
 
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə meesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/etag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(sehidler)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(sehidler)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 Prosesi başladan:**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
@client.on(events.NewMessage(pattern="^.stag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir")
  
  admins = []
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
 
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 Prosesi başladan:**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
@client.on(events.NewMessage(pattern="^.mtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün mesaj yazın**")
  else:
    return await event.respond("**✅ Tağ edə bilməyim üçün bir mesaj yaın**\n**ℹ️ Misal:** `/mtag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
 
 
 
@client.on(events.NewMessage(pattern="^.etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/etag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
@client.on(events.NewMessage(pattern="^.rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**✅ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**✅ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın\n**ℹ️ Misal:** `/rtag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
@client.on(events.NewMessage(pattern="^.btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/btag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
		


@client.on(events.NewMessage(pattern="^.admin ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "Qrup Adminlərin Siyahısı 👤\n"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n[{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation
    
    
    
    
SAHIB = Config.OWNER_ID

@client.on(events.NewMessage(pattern="^.pin ?(.*)"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Zəhmət olmasa bir mesaja yanıt ver ❗")
        await event.reply("Mesajı sabitlədım 📌")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} bota sahib deyilsən ❗")
 

@client.on(events.NewMessage(pattern="^.unpin ?(.*)"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Zəhmət olmasa sabitlənmiş bir mesaja yanıt ver ❗")
        await event.reply("Sabitlənmiş mesaj qaldırıldı ❗")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} bota sahib deyilsən ❗")    
        





@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


@client.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Səni tanımaq çox xoş idi",)

userjoin = (

    "Xoş gəldiniz",
    "Salamm əyləncə dolu qrupumuza xoş gəlmisiniz🥰",
    "Salam xoş gəldin👀🙊",
    "Salam xoş gəlmisən @qruzdaa kanalımada abunə ol🙈",
    "Xoş gəldin balam😂❤️",
    "Xoş gəldin nəfəsss😂❤️",
    "Xoş gəldin vətəndaş🤓",
    "Xoş gəldin aramıza😌❤️",
    "Salam xoş gəldin səni burda görmək çox xoşdur😍",
    "Salam xoş gəldin gözəl insan🥰",
    "Salam xoş gəldin necəsən?🥰",
    "Salamm xanım xoş gəldin tanış olmaq olar?👀😂",
    "Bayaqdan səni gözləyirəme gəl çıxda😒",
    ""
)




@client.on(events.NewMessage(pattern='@Rahid_7'))
async def handler(event):
    await event.reply(random.choice(Aylin))



Aylin = (
    "Az tağ elə sahibimi😒",
    "İşi var birazdan gələcək😇",
    "Ay bala nolub mənə de o yoxdu",
    "Az tağ elədə sahibimi",
    "Sahibim burda deyil mənə deyə bilərsən👀",
    "Evdə deyil",
    "Nolub mənə deyə bilərsən",
    "Burda deyil yəqin başqa qrupdadı😂",
    "Sahibim burda olmasada qəlbi sizinlədir😌",
    "Burda yoxdur kömək üçün mənə deyə bilərsən😇",
    "@Rahid_7 səni çağırır qaqaş👀",
    "🚷 Ban Olundun !\nSəbəb: Sahibimi tağ etdiyin üçün 🙄\n\nŞaka ya korkma 😂",
    "/ban çox tağ edirsən Sahibimi🙄",
    "/mute az tağ elə Sahibimi😑",
    "/warn birdə Sahibimi tağ eləsən ban verəcəm sənə!",
    "/fban Sahibimi çox tağ edirsiz!",
    "Sahibim dedi birazdan gələcəm👀",
    "Az tağ edin onu zəhmət olmasa🙄",
    "Onun başı qarışıqdı birazdan gələcək",
    "O daha qrupa gəlməyəcək onu mən əvəz edəcəyəm 🤖",
    "Nə istəyirsən ondan?",
    ""
)


@client.on(events.NewMessage(pattern='(?i)sikim+'))
@client.on(events.NewMessage(pattern='(?i)peysər+'))
@client.on(events.NewMessage(pattern='(?i)qəhbə+'))
@client.on(events.NewMessage(pattern='(?i)sikdir+'))
@client.on(events.NewMessage(pattern='(?i)siktir+'))
@client.on(events.NewMessage(pattern='(?i)göt+'))
@client.on(events.NewMessage(pattern='(?i)cındır+'))
@client.on(events.NewMessage(pattern='(?i)peyser+'))
@client.on(events.NewMessage(pattern='(?i)qehbe+'))
@client.on(events.NewMessage(pattern='(?i)gijdilax+'))
@client.on(events.NewMessage(pattern='(?i)suka+'))
@client.on(events.NewMessage(pattern='(?i)küçük+'))
@client.on(events.NewMessage(pattern='(?i)sik+'))
@client.on(events.NewMessage(pattern='(?i)skm+'))
@client.on(events.NewMessage(pattern='(?i)götüş+'))
@client.on(events.NewMessage(pattern='(?i)götün+'))
@client.on(events.NewMessage(pattern='(?i)sikm+'))
@client.on(events.NewMessage(pattern='(?i)blet+'))
@client.on(events.NewMessage(pattern='(?i)blət+'))
@client.on(events.NewMessage(pattern='(?i)sikərəm+'))
@client.on(events.NewMessage(pattern='(?i)sikecem+'))
@client.on(events.NewMessage(pattern='(?i)sikəcəm+'))
@client.on(events.NewMessage(pattern='(?i)sikerem+'))
@client.on(events.NewMessage(pattern='(?i)siktr+'))
@client.on(events.NewMessage(pattern='(?i)sikdr+'))
@client.on(events.NewMessage(pattern='(?i)sikir+'))
@client.on(events.NewMessage(pattern='(?i)sikib+'))
@client.on(events.NewMessage(pattern='(?i)dalbayok+'))
@client.on(events.NewMessage(pattern='(?i)pidr+'))
@client.on(events.NewMessage(pattern='(?i)siksinlər+'))
@client.on(events.NewMessage(pattern='(?i)sukalar+'))
@client.on(events.NewMessage(pattern='(?i)siksinlər+'))
@client.on(events.NewMessage(pattern='(?i)siksin+'))
@client.on(events.NewMessage(pattern='(?i)sikaram+'))
@client.on(events.NewMessage(pattern='(?i)xnxx+'))
@client.on(events.NewMessage(pattern='(?i)porno+'))
@client.on(events.NewMessage(pattern='(?i)gijdılax+'))
@client.on(events.NewMessage(pattern='(?i)vayoxuna+'))
@client.on(events.NewMessage(pattern='(?i)varyoxsuz+'))
@client.on(events.NewMessage(pattern='(?i)varyoxunu+'))
@client.on(events.NewMessage(pattern='(?i)vayoxuna+'))
@client.on(events.NewMessage(pattern='(?i)peysərrr+'))
@client.on(events.NewMessage(pattern='(?i)peysərr+'))
@client.on(events.NewMessage(pattern='(?i)skdr+'))
@client.on(events.NewMessage(pattern='(?i)skdir+'))
@client.on(events.NewMessage(pattern='(?i)sirtiq+'))
@client.on(events.NewMessage(pattern='(?i)sırtıq+'))
@client.on(events.NewMessage(pattern='(?i)peyserr+'))
@client.on(events.NewMessage(pattern='(?i)kucuy+'))
@client.on(events.NewMessage(pattern='(?i)küçüy+'))
@client.on(events.NewMessage(pattern='(?i)gotunu+'))
@client.on(events.NewMessage(pattern='(?i)götünü+'))
@client.on(events.NewMessage(pattern='(?i)blett+'))
@client.on(events.NewMessage(pattern='(?i)blətt+'))
@client.on(events.NewMessage(pattern='(?i)götu+'))
@client.on(events.NewMessage(pattern='(?i)götü+'))
@client.on(events.NewMessage(pattern='(?i)götun+'))
@client.on(events.NewMessage(pattern='(?i)sikdiyine+'))
@client.on(events.NewMessage(pattern='(?i)sikdiyinə+'))
@client.on(events.NewMessage(pattern='(?i)sikdilere+'))
@client.on(events.NewMessage(pattern='(?i)sikdiləre+'))
@client.on(events.NewMessage(pattern='(?i)sikdilər+'))
@client.on(events.NewMessage(pattern='(?i)sikdide+'))
@client.on(events.NewMessage(pattern='(?i)sikdidə+'))
@client.on(events.NewMessage(pattern='(?i)skkdirdə+'))
@client.on(events.NewMessage(pattern='(?i)skkdirde+'))
@client.on(events.NewMessage(pattern='(?i)sikdiyime+'))
@client.on(events.NewMessage(pattern='(?i)sikdiyimə+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdee+'))
@client.on(events.NewMessage(pattern='(?i)sikereme+'))
@client.on(events.NewMessage(pattern='(?i)sikərəme+'))
@client.on(events.NewMessage(pattern='(?i)peysere+'))
@client.on(events.NewMessage(pattern='(?i)peysərə+'))
@client.on(events.NewMessage(pattern='(?i)pic+'))
@client.on(events.NewMessage(pattern='(?i)petuxlar+'))
@client.on(events.NewMessage(pattern='(?i)petuxsan+'))
@client.on(events.NewMessage(pattern='(?i)peysersen+'))
@client.on(events.NewMessage(pattern='(?i)peysərsən+'))
@client.on(events.NewMessage(pattern='(?i)gicsen+'))
@client.on(events.NewMessage(pattern='(?i)gicsən+'))
@client.on(events.NewMessage(pattern='(?i)gicdırlax+'))
@client.on(events.NewMessage(pattern='(?i)qehbeni+'))
@client.on(events.NewMessage(pattern='(?i)qəhbəni+'))
@client.on(events.NewMessage(pattern='(?i)sykdir+'))
@client.on(events.NewMessage(pattern='(?i)varyox+'))
@client.on(events.NewMessage(pattern='(?i)qehbedie+'))
@client.on(events.NewMessage(pattern='(?i)qehbediye+'))
@client.on(events.NewMessage(pattern='(?i)qəhbədie+'))
@client.on(events.NewMessage(pattern='(?i)qehbeni+'))
@client.on(events.NewMessage(pattern='(?i)qəhbəni+'))
@client.on(events.NewMessage(pattern='(?i)sikdrbe+'))
@client.on(events.NewMessage(pattern='(?i)qehbedi+'))
@client.on(events.NewMessage(pattern='(?i)qəhbədi+'))
@client.on(events.NewMessage(pattern='(?i)peyserdi+'))
@client.on(events.NewMessage(pattern='(?i)peysərdi+'))
@client.on(events.NewMessage(pattern='(?i)skerəm+'))
@client.on(events.NewMessage(pattern='(?i)skərem+'))
@client.on(events.NewMessage(pattern='(?i)sikərem+'))
@client.on(events.NewMessage(pattern='(?i)sikerəm+'))
@client.on(events.NewMessage(pattern='(?i)skerem+'))
@client.on(events.NewMessage(pattern='(?i)petox+'))
@client.on(events.NewMessage(pattern='(?i)osturaq+'))
@client.on(events.NewMessage(pattern='(?i)soxaram+'))
@client.on(events.NewMessage(pattern='(?i)soxacam+'))
@client.on(events.NewMessage(pattern='(?i)soxum+'))
@client.on(events.NewMessage(pattern='(?i)skdır+'))
@client.on(events.NewMessage(pattern='(?i)sktir+'))
@client.on(events.NewMessage(pattern='(?i)sihtır+'))
@client.on(events.NewMessage(pattern='(?i)sihtir+'))
@client.on(events.NewMessage(pattern='(?i)sihdir+'))
@client.on(events.NewMessage(pattern='(?i)dalyok+'))
@client.on(events.NewMessage(pattern='(?i)sikhtir+'))
@client.on(events.NewMessage(pattern='(?i)sikhtır+'))
@client.on(events.NewMessage(pattern='(?i)sikhdir+'))
@client.on(events.NewMessage(pattern='(?i)sikhdır+'))
@client.on(events.NewMessage(pattern='(?i)sikdirim+'))
@client.on(events.NewMessage(pattern='(?i)sikere+'))
@client.on(events.NewMessage(pattern='(?i)siker+'))
@client.on(events.NewMessage(pattern='(?i)sikəre+'))
@client.on(events.NewMessage(pattern='(?i)sikər+'))
@client.on(events.NewMessage(pattern='(?i)skdirim+'))
@client.on(events.NewMessage(pattern='(?i)sikdırım+'))
@client.on(events.NewMessage(pattern='(?i)sikdirım+'))
@client.on(events.NewMessage(pattern='(?i)oruspo+'))
@client.on(events.NewMessage(pattern='(?i)orosponun+'))
@client.on(events.NewMessage(pattern='(?i)qehbə+'))
@client.on(events.NewMessage(pattern='(?i)qəhbe+'))
@client.on(events.NewMessage(pattern='(?i)peyesər+'))
@client.on(events.NewMessage(pattern='(?i)peyəser+'))
@client.on(events.NewMessage(pattern='(?i)peyeser+'))
@client.on(events.NewMessage(pattern='(?i)qəybə+'))
@client.on(events.NewMessage(pattern='(?i)amcığ+'))
@client.on(events.NewMessage(pattern='(?i)sikdirde+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdeee+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdeeee+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdeeeeee+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdeeeee+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdəəəəə+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdəəəə+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdəəə+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdəə+'))
@client.on(events.NewMessage(pattern='(?i)sikdirdə+'))
@client.on(events.NewMessage(pattern='(?i)skımm+'))
@client.on(events.NewMessage(pattern='(?i)skimm+'))
@client.on(events.NewMessage(pattern='(?i)skım+'))
@client.on(events.NewMessage(pattern='(?i)skim+'))
@client.on(events.NewMessage(pattern='(?i)amk+'))
@client.on(events.NewMessage(pattern='(?i)bled+'))
@client.on(events.NewMessage(pattern='(?i)bləd+'))
@client.on(events.NewMessage(pattern='(?i)cindirsan+'))
@client.on(events.NewMessage(pattern='(?i)ostur+'))
@client.on(events.NewMessage(pattern='(?i)gotum+'))
@client.on(events.NewMessage(pattern='(?i)gijdillaq+'))
@client.on(events.NewMessage(pattern='(?i)gotun+'))
@client.on(events.NewMessage(pattern='(?i)petuxun+'))
@client.on(events.NewMessage(pattern='(?i)qəhbələrə+'))
@client.on(events.NewMessage(pattern='(?i)götüm+'))
@client.on(events.NewMessage(pattern='(?i)götum+'))
@client.on(events.NewMessage(pattern='(?i)blətt+'))
@client.on(events.NewMessage(pattern='(?i)bləttt+'))
@client.on(events.NewMessage(pattern='(?i)blətttt+'))
@client.on(events.NewMessage(pattern='(?i)bləttttt+'))
@client.on(events.NewMessage(pattern='(?i)biləəttt+'))
@client.on(events.NewMessage(pattern='(?i)dumsuyukk+'))
@client.on(events.NewMessage(pattern='(?i)qehbelik+'))
@client.on(events.NewMessage(pattern='(?i)qəhbəlik+'))
@client.on(events.NewMessage(pattern='(?i)sktr+'))
@client.on(events.NewMessage(pattern='(?i)gijdilaq+'))
@client.on(events.NewMessage(pattern='(?i)dumsukk+'))
@client.on(events.NewMessage(pattern='(?i)slk+'))
@client.on(events.NewMessage(pattern='(?i)skimsen+'))
@client.on(events.NewMessage(pattern='(?i)skimsən+'))
@client.on(events.NewMessage(pattern='(?i)poooooox+'))
@client.on(events.NewMessage(pattern='(?i)pooooox+'))
@client.on(events.NewMessage(pattern='(?i)poooox+'))
@client.on(events.NewMessage(pattern='(?i)pooox+'))
@client.on(events.NewMessage(pattern='(?i)poox+'))
@client.on(events.NewMessage(pattern='(?i)siki+'))
@client.on(events.NewMessage(pattern='(?i)sikeyim+'))
@client.on(events.NewMessage(pattern='(?i)gijdillaxx+'))
@client.on(events.NewMessage(pattern='(?i)gijdillaxxx+'))
@client.on(events.NewMessage(pattern='(?i)gijdillaxxxx+'))
@client.on(events.NewMessage(pattern='(?i)qehbeleriii+'))
@client.on(events.NewMessage(pattern='(?i)qehbelerrr+'))
@client.on(events.NewMessage(pattern='(?i)sikimmm+'))
@client.on(events.NewMessage(pattern='(?i)skimmmm+'))
@client.on(events.NewMessage(pattern='(?i)skimmm+'))
@client.on(events.NewMessage(pattern='(?i)peyserdiiii+'))
@client.on(events.NewMessage(pattern='(?i)qehbediiiiii+'))
@client.on(events.NewMessage(pattern='(?i)qehbedennn+'))
@client.on(events.NewMessage(pattern='(?i)sikdrnnn+'))
@client.on(events.NewMessage(pattern='(?i)sikdirinnn+'))
@client.on(events.NewMessage(pattern='(?i)osduraqqq+'))
@client.on(events.NewMessage(pattern='(?i)poxuuu+'))
@client.on(events.NewMessage(pattern='(?i)sikkimmm+'))
@client.on(events.NewMessage(pattern='(?i)qehbbediii+'))
@client.on(events.NewMessage(pattern='(?i)qehbbeninnn+'))
@client.on(events.NewMessage(pattern='(?i)qehebbbedennnnnn+'))
@client.on(events.NewMessage(pattern='(?i)qehbbedilerdeeee+'))
@client.on(events.NewMessage(pattern='(?i)sikimmm+'))
@client.on(events.NewMessage(pattern='(?i)sikmeyyyy+'))
@client.on(events.NewMessage(pattern='(?i)qehbbbbeeeelerrrrr+'))
@client.on(events.NewMessage(pattern='(?i)sikkim+'))
@client.on(events.NewMessage(pattern='(?i)qehbbbesen+'))
@client.on(events.NewMessage(pattern='(?i)qehbbedilerdeeee+'))
@client.on(events.NewMessage(pattern='(?i)siki‌i‌mmm+'))
@client.on(events.NewMessage(pattern='(?i)qot+'))
@client.on(events.NewMessage(pattern='(?i)skmm+'))
@client.on(events.NewMessage(pattern='(?i)sikilir+'))
@client.on(events.NewMessage(pattern='(?i)sikkkim+'))
@client.on(events.NewMessage(pattern='(?i)anasinesikim+'))
@client.on(events.NewMessage(pattern='(?i)anasinesikimm+'))
@client.on(events.NewMessage(pattern='(?i)sikdirecem+'))
@client.on(events.NewMessage(pattern='(?i)sukalarr+'))
@client.on(events.NewMessage(pattern='(?i)qehbesi+'))
@client.on(events.NewMessage(pattern='(?i)sikdiren+'))
@client.on(events.NewMessage(pattern='(?i)gehbedi+'))
@client.on(events.NewMessage(pattern='(?i)qotvu+'))
@client.on(events.NewMessage(pattern='(?i)bləəət+'))
@client.on(events.NewMessage(pattern='(?i)sic+'))
@client.on(events.NewMessage(pattern='(?i)gijdillah+'))
@client.on(events.NewMessage(pattern='(?i)qehbeliyi+'))
@client.on(events.NewMessage(pattern='(?i)sg+'))
@client.on(events.NewMessage(pattern='(?i)sikdimdə+'))
@client.on(events.NewMessage(pattern='(?i)sikdimde+'))
@client.on(events.NewMessage(pattern='(?i)poxla+'))
@client.on(events.NewMessage(pattern='(?i)sikdirsinlər+'))
@client.on(events.NewMessage(pattern='(?i)sikdirsinler+'))
async def mesaj(event: events.NewMessage.Event):
    await event.delete()  
    await event.reply(f"**🔞 Söyüş yazdığına görə mesajı sildim.**")
