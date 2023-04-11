from AylinRobot import AylinRobot as app
import random
from pyrogram import Client, filters

# Pyrogram istemcisini başlat

# "/mal" komutuna yanıt veren bir işlev tanımlayın
@app.on_message(filters.command("mal"))
async def calculate_wealth(client, message):
    # Rastgele bir mal varlığı yüzdesi belirleyin
    wealth_percent = random.randint(50, 100)
    # Kullanıcının adını alın
    user = message.reply_to_message.from_user
    user_name = user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
    # Tahmin edilen mal varlığı yüzdesini mesaj olarak gönderin
    await message.reply(f"{user_name} sən %{wealth_percent} malsan😹")



@app.on_message(filters.command("esq"))
async def calculate_wealth(client, message):
    # Rastgele bir mal varlığı yüzdesi belirleyin
    wealth_percent = random.randint(50, 100)
    # Kullanıcının adını alın
    user = message.reply_to_message.from_user
    user_name = user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
    # Tahmin edilen mal varlığı yüzdesini mesaj olarak gönderin
    await message.reply(f"{user_name} ilə sənin eşq faizin❤️ %{wealth_percent}")
