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
    await message.reply(f"{user_name}, sizin mal varlığınızın %{wealth_percent} olduğunu tahmin ediyorum.")



@app.on_message(filters.command("sevgi"))
async def calculate_wealth(client, message):
    # Rastgele bir mal varlığı yüzdesi belirleyin
    wealth_percent = random.randint(50, 100)
    # Kullanıcının adını alın
    user = message.reply_to_message.from_user
    user_name = user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
    # Tahmin edilen mal varlığı yüzdesini mesaj olarak gönderin
    await message.reply(f"{user_name}, sizin mal varlığınızın %{wealth_percent} olduğunu tahmin ediyorum.")
