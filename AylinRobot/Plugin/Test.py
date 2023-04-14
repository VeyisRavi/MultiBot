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
    await message.reply(f"{user_name} bu şəxsin %{wealth_percent} mal olduğunu bilirəm😹")



@app.on_message(filters.command("esq"))
async def calculate_wealth(client, message):
    # Rastgele bir mal varlığı yüzdesi belirleyin
    wealth_percent = random.randint(50, 100)
    # Kullanıcının adını alın
    user = message.reply_to_message.from_user
    user_name = user.first_name if not user.last_name else f"{user.first_name} {user.last_name}"
    # Tahmin edilen mal varlığı yüzdesini mesaj olarak gönderin
    await message.reply(f"{user_name} ilə sənin eşq faizin %{wealth_percent} 💕")




from pyrogram import Client, filters

# Kaba kelimeler listesi
bad_words = ['göt', 'sik', 'peysər', 'cındır', 'qehbe', 'qəhbə', 'cindir', 'peyser', 'küçük', 'suka', 'blət', 'blet', 'pidr', 'dalbayok', 'sirtiq', 'porno', 'xnxx', 'küçüy', 'kucuy', 'sırtıq', 'gic', 'dalyok', 'qehbə', 'qəhbe', 'amcığ', 'amcıq', 'bləd', 'bled', 'amk', 'ostur', 'dumsuk', 'dumsuy', 'pox', 'slk', 'qehebe', 'qehbbe', 'qot', 'gəhbə', 'amcıg', 'siik', 'gehbe', 'sg', 'gij', 'qəhi', 'qehi', 'meki', 'məki', 'amciq', 'amcig']


users = {}

# Mesajları filtreleme işlemi
@app.on_message(filters.text & ~filters.private)
async def filter_bad_words(client, message):
    for word in bad_words:
        if word in message.text.lower():
            # Mesajı atan kişinin kimliğini alın
            user_id = message.from_user.id
            # Küfür sayısını arttırın veya yeni bir kullanıcı ekleyin
            if user_id in users:
                users[user_id] += 1
            else:
                users[user_id] = 1
            # Küfür eden kişiye özel mesaj gönderin
            await client.send_message(chat_id=user_id, text="🔞 Qrupda söyüş yazdığına görə mesajını sildim!\n\n🗑️ Silinən mesajların ümumi sayı: {}".format(users[user_id]))
            # Küfür içeren mesajı silin
            await message.delete()
            # Küfür eden kişiye qrupda sildiğini bildirin
            await client.send_message(chat_id=message.chat.id, text="{} İstifadəçi söyüş yazdığına görə mesajı sildim.".format(message.from_user.first_name))