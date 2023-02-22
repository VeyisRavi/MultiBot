# @AylinRobot
#@MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """**🙋🏻 Salam {}**\n👀 Mənim Adım [{}](https://t.me/{})\n🇦🇿 Azərbaycan dilində çox özəllikli telegram botuyam bacarıqlarımı görmək üçün Kömək butonuna daxil olun\n\n👨🏻‍💻 **Bot Sahibi** @{}

"""    
    HELP_TEXT = """**🙋🏻 Salam {}\n💁🏻 ️️️️️️ [{}](https://t.me/{})-un əmrləri bunlardır aşağıdakı butonlara daxil olaraq istədiyiniz əmrləri öyrənə bilərsiniz
"""

### Bot Haqqında Ümumi Məlumat

    BH_TEXT = """
╔═════════════════
║▻ **🙋🏻 Salam {} 
║
║▻ 🙎🏻 [{}](https://t.me/{}) 🇦🇿 Azərbaycan dilində çox özəllikli telegram botudur.**
║
║▻ 🌀 Bot Versiyası: v0.7.0
║▻ 🍀 Pyrogram Versiyası: 1.4.16
║▻ ⚡ Python Versiyası: 3.11.1
║▻ ⚙️ Server [Heroku](https://heroku.com)
║▻ 📆 Botun istifadəyə verilmə tarixi `13.03.2023` 
╚═════════════════
╔═════════════════
║▻ **⚠️ Qeyd: botun qrupunuzda işləməsi üçün admin əmrlərindən sadəcə "Mesaj Silmə" yetkisi verin**
╚═════════════════
"""


    SAHIB_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /stats
║▻ 📃 Açıqlama: Bot haqqında ümumi məlumat verər.
║
║▻ 🔮 İstifadə: /block
║▻ 📃 Açıqlama: İstifadəçini və ya qrupu bloklayar.
║
║▻ 🔮 İstifadə: /unblock
║▻ 📃 Açıqlama: İstifadəçini və ya qrupun bloku açar.
║
║▻ 🔮 İstifadə: /blocklist
║▻ 📃 Açıqlama: Blok olunanların siyahısını göstərər.
║
║▻ 🔮 İstifadə: /broadcastall
║▻ 📃 Açıqlama: Qrupa və şəxsiyə yayım edər.
║
║▻ 🔮 İstifadə: /gcast
║▻ 📃 Açıqlama: Qruplarda yayım edər.
║
║▻ 🔮 İstifadə: /broadcast_pin
║▻ 📃 Açıqlama: Qruplarda yayım edər və sabitləyər.
║
║▻ 🔮 İstifadə: /dyno
║▻ 📃 Açıqlama: Heroku dyno miqdarını ölçər.
╚═════════════════
"""

    MUSIC_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /song 
║▻ 🧩 Nümunə: /song Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: Musiqi yükləyər.
║
║▻ 🔮 İstifadə: /video
║▻ 🧩  Nümunə: /video Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: Video yükləyər.
║
║▻ 🔮 İstifadə: /lyrics 
║▻ 🧩 Nümunə: /lyrics Rei - Ah Canım Sevgilim
║
║▻ 📃 Açıqlama: Musiqinin sözlərini tapar.
╚═════════════════
"""

    TELEGRAPH_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /tgm
║▻ 📃 Açıqlama: Şəkil, video və ya GIF göndərərək link ala bilərsiniz.
╚═════════════════
"""

    SEHID_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /sehid 
║▻ 📃 Açıqlama: Bu əmr vasitəsilə bot sizə **Şəhid** adları göndərəcək
╚═════════════════
╔═════════════════
║▻ 🥀 **Allah bütün Şəhidimizə rəhmət eləsin**
║▻ 🤲 Qazilərimizə şəfa versin 
║▻ 😔 Başın sağolsun Azərbaycan 🇦🇿
║▻ 🇦🇿 Bazada **2881** Şəhid adı mövcuddur
╚═════════════════
""" 
    OYUN_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /zer
║▻ 📃 Açıqlama: Zər atar
║
║▻ 🔮 İstifadə: /top
║▻ 📃 Açıqlama: Top atar
║
║▻ 🔮 İstifadə: /bowling
║▻ 📃 Açıqlama: Bowling atar
║
║▻ 🔮 İstifadə: /ox
║▻ 📃 Açıqlama: Ox atar
║
║▻ 🔮 İstifadə: /jackpot
║▻ 📃 Açıqlama: Jackpot atar
║
║▻ 🔮 İstifadə: /basket
║▻ 📃 Açıqlama: Basket atar
╚═════════════════
"""

    EYLENCE_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /soxri 
║▻ 📃 Açıqlama: 16+ şəkillər atar.
║
║▻ 🔮 İstifadə: /pisik
║▻ 📃 Açıqlama: Pişik şəkili atar.
║
║▻ 🔮 İstifadə: /anime
║▻ 📃 Açıqlama: Anime şəkilər atar.
║
║▻ 🔮 İstifadə: /masin
║▻ 📃 Açıqlama: Maşın şəkilər atar.
║
║▻ 🔮 İstifadə: /masin2
║▻ 📃 Açıqlama: Maşın videolar atar.
║
║▻ 🔮 İstifadə: /tema
║▻ 📃 Açıqlama: Telegram temalar atar.
║
║▻ 🔮 İstifadə: /pp
║▻ 📃 Açıqlama: Profil şəkillər atar.
║
║▻ 🔮 İstifadə: /sevgi
║▻ 📃 Açıqlama: Sevgi sözlər atar.
║
║▻ 🔮 İstifadə: /bio
║▻ 📃 Açıqlama: Bio sözlər atar.
╚═════════════════
"""


    ELAVELER_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /carbon
║▻ 📃 Açıqlama: Yazdığınız mesajı şəkilə çevirər.
║
║▻ 🔮 İstifadə: /id
║▻ 📃 Açıqlama: İstifadəçi ID atar.
║
║▻ 🔮 İstifadə: /info
║▻ 📃 Açıqlama: İstifadəçi haqqında məlumat atar.
║
║▻ 🔮 İstifadə: /alive
║▻ 📃 Açıqlama: Botun işlək olduğunu yoxlayar.
╚═════════════════
"""


    AXTARIS_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /github 
║▻ 🧩 Nümunə: /github Rahid2003
║▻ 📃 Açıqlama: Github axtarışı edər.
║
║▻ 🔮 İstifadə: /search
║▻ 🧩 Nümunə: /search Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: YouTube axtarış üçün istifadə edə bilərsiniz.
╚═════════════════
"""

    TAGGER_TEXT = """
╔═════════════════
║▻ 🔮 İstifadə: /tag
║▻ 👥 Açıqlama: 5-li tağ edər.
║
║▻ 🔮 İstifadə: /tektag
║▻ 👤 Açıqlama: Təkli tağ edər.
║
║▻ 🔮 İstifadə: /stag
║▻ 📜 Açıqlama: Maraqlı sözlərlə tağ edər.
║
║▻ 🔮 İstifadə: /etag
║▻ 🥰 Açıqlama: Emoji ilə tağ edər.
║
║▻ 🔮 İstifadə: /btag
║▻ 🏴 Açıqlama: Bayraqlarla tağ edər.
║
║▻ 🔮 İstifadə: /admin
║▻ 👨‍⚖️ Açıqlama: Qrup adminlərin siyahısı atar.
╚═════════════════
"""



##### Broadcast Mesajları


class LAN(object):


    BILDIRIM = """**🆕 Yeni İstifadəçi bota start etdi**\n\n👤: {}\n🆔 `{}`\n🔗 [{}](tg://user?id={})"""
    GRUP_BILDIRIM = """**🆕 Yeni İstifdəçi bota qrupda start etdi**\n\n👤 Qrupa əlavə edən: `{}`\n🆔 Qrupa əlavə edən istifadəçi id: `{}`\n🔗 Profil linki: [{}](tg://user?id={})\nQrupun Adı: {}\nQrupun ID: {}\nQrupun mesaj linki (Sadəcə açıq qruplar): [Bura Toxun](https://t.me/c/{}/{})

"""
    SAHIBIME = """
sahibimə
"""
    PRIVATE_BAN = """
Məyusam, əngəlləndiniz! Bunun bir xəta olduğunu düşünürsünüzsə {} yazın.
 """
    GROUP_BAN = """
Məyusam, qrupunuz qara siyahıya əlavə olundu! Artıq burada qala bilmərəm! Bunun bir xəta olduğunu düşünürsünüzsə {} yazın.'
"""
    NOT_ONLINE = """
aktiv deyil
"""
    BOT_BLOCKED = """
botu əngəlləyib
"""
    USER_ID_FALSE = """
istifadəçi id'i yanlışdır.
"""
    BROADCAST_STARTED = """
```📤 BroadCast başladıldı! Bitəndə mesaj göndərəcəm.
"""
    BROADCAST_STOPPED = """
✅ ```Broadcast uğurla tamamlandı.```\n\n**Bu qədər vaxtda tamamlandı** `{}`\n\n**Ümumi istifadəçilər:** `{}`\n\n**Ümumi göndərmə cəhdləri:** `{}`\n\n**Uğurla göndərilən:** `{}`\n\n**Ümumi xəta:** `{}`
"""
    STATS_STARTED = """
{} **Zəhmət olmasa gözləyin, bilgiləri gətirirəm!**
"""
    STATS = """
**@{} Məlumatları**\n\n**İstifadəçiləri;**\n» Ümumi Söhbətlər: `{}`\n» Ümumi Qruplar: `{}`\n» Ümumi PM's: `{}`\n\n**Disk İstifadəsi;**\n» Disk'in Sahəsi: `{}`\n» İstifadə Edilən: `{} ({}%)`\n» Boş Qalan: `{}`\n\n**🎛 Ən yüksək istifadə dəyərləri;**\n» CPU: `{}%`\n» RAM: `{}%`\n» Pyrogram: {}
"""
    BAN_REASON = """
Bu səbəbdən qadağan olundunuz @{} tərəfindən avtomatik olaraq yaradılmışdır."""
    NEED_USER = """
**Zəhmət olmasa istifadəçi ID'si yazın.**
"""
    BANNED_GROUP = """
🚷 **Qadağan olundu!\n\nQadağan edən:** {}\n**Qrup ID:** `{}`\n**Vaxt:** `{}`\n**Səbəb:** `{}`
"""
    AFTER_BAN_GROUP = """
**Məyusam, qrupunuz qara siyahıya əlavə edildi!\n\nSəbəb:** `{}`\n\n**Artıq burada qala bilmərəm. Bunun bir xəta olduğunu düşünürsünüzsə, dəstək qrupuna gəlin.**
"""
    GROUP_BILGILENDIRILDI = """\n\n✅ **Qrupu bilgiləndirdim və qrupdan çıxdım.**
"""
    GRUP_BILGILENDIRILEMEDI = """\n\n❌ **Qrupu məlumatlandırarkən xəta yarandı:**\n\n`{}`
"""
    USER_BANNED = """
🚷 **Qadağan olundu\n\nQadağan edən:** {}\n **İstifadəçi ID:** `{}`\n**Vaxt:** `{}`\n**Səbəb:** `{}`
"""
    AFTER_BAN_USER = """
**Məyusam, qara siyahıya əlavə edildiniz! \n\nSəbəb:** `{}`\n\n**Bundan sonra sizə xidmət etməyəcəyəm.**
"""
    KULLANICI_BILGILENDIRME = """\n\n✅ İstifadəçini məlumatlandırdım.
"""
    KULLANICI_BILGILENDIRMEME = """\n\n❌ **İstifadəçini məlumatlandırarkən xəta yarandı:**\n\n`{}`
"""
    UNBANNED_USER = """
🆓 **İstifadəçinin qadağası qaldırıldı!** \nQadağanı qaldıran: {}\n**İstifadəçi ID:**{}
"""
    USER_UNBAN_NOTIFY = """
🎊 Sizə gözəl bir xəbərim var! Artıq əngəliniz qaldırıldı!
"""
    BLOCKS = """
🆔 **İstifadəçi ID**: `{}`\n⏱ **Vaxt**: `{}`\n🗓 **Qadağan edildiyi tarix**: `{}`\n💬 **Səbəb**: `{}`\n\n"""
    TOTAL_BLOCK = """
🚷 **Ümumi əngəllənən:** `{}`\n\n{}
"""