# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from pyrogram import Client, filters
import heroku3, requests, time, math, os
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from AylinRobot.config import Config

BOT_START_TIME = time.time()

@app.on_message(filters.command(["dyno"]) & filters.user(Config.OWNER_ID))  
async def bot_status(client,message):
    if Config.HEROKU_API_KEY:
        try:
            server = heroku3.from_key(Config.HEROKU_API_KEY)

            user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
            accountid = server.account().id
            headers = {
            'User-Agent': user_agent,
            'Authorization': f'Bearer {Config.HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
            }

            path = "/accounts/" + accountid + "/actions/get-quota"

            request = requests.get("https://api.heroku.com" + path, headers=headers)

            if request.status_code == 200:
                result = request.json()

                total_quota = result['account_quota']
                quota_used = result['quota_used']

                quota_left = total_quota - quota_used
                
                total = math.floor(total_quota/3600)
                used = math.floor(quota_used/3600)
                hours = math.floor(quota_left/3600)
                minutes = math.floor(quota_left/60 % 60)
                days = math.floor(hours/24)

                usedperc = math.floor(quota_used / total_quota * 100)
                leftperc = math.floor(quota_left / total_quota * 100)

                quota_details = f"""
💫 SERVER STATUSU 💫
💠 Toplam dyno ➪ {total} saat !
 
💠 Dyno istifadə olunub ➪ {used} Saat ( {usedperc}%)
        
💠 Dyno qalıb ➪ {hours} Saat ( {leftperc}% )
        
💠 Təxmini günlər ➪ {days} gün qaldı."""

            else:
                quota_details = ""
        except:
            print("Heroku API açarınızı yoxlayın")
            quota_details = ""
    else:
        quota_details = ""

    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - BOT_START_TIME))

    try:
        t, u, f = shutil.disk_usage(".")
        total = humanbytes(t)
        used = humanbytes(u)
        free = humanbytes(f)

        disk = "\n**Disk Details**\n\n" \
            f"> USED  :  {used} / {total}\n" \
            f"> FREE  :  {free}\n\n"
    except:
        disk = ""

    await message.reply_text(
        "Bot DB Statusunuzun Cari Vəziyyəti\n"
        f"➪ Botun işləmə müddəti: {uptime}\n"
        f"{quota_details}"
        f"{disk}",
        quote=True,
        parse_mode="md"
    )

