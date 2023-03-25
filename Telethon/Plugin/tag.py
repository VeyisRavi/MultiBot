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
    "**🚷 Ban Olundun !**\nSəbəb: Sahibimi tağ etdiyin üçün 🙄\n\nŞaka ya korkma 😂",
    "/ban çox tağ edirsən Sahibimi🙄",
    "/mute az tağ elə Sahibimi😑",
    "/warn birdə Sahibimi tağ eləsən ban verəcəm sənə!",
    "/fban Sahibimi çox tağ edirsiz!",
    "Sahibim dedi birazdan gələcəm👀",
    "Az tağ edin onu zəhmət olmasa🙄",
    "Onun başı qarışıqdı birazdan gələcək",
    ""
)
