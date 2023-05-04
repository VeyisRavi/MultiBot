# @AylinRobot
#@MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """**🙋🏻 Salam {}**\n👀 Mənim Adım [{}](https://t.me/{})\n🇦🇿 Azərbaycan dilində çox özəllikli telegram botuyam bacarıqlarımı görmək üçün Bot Əmrlərinə daxil olun"""  
    
    HELP_TEXT = """**🙋🏻 Salam {}\n💁🏻 [{}](https://t.me/{}) Əmrləri bunlardır aşağıdakı butonlara daxil olaraq istədiyiniz əmrləri öyrənə bilərsiniz"""

### Bot Haqqında Ümumi Məlumat

    BH_TEXT = """**🙋🏻 Salam {}\n🤖 [{}](https://t.me/{}) Azərbaycan dilində çox özəllikli telegram botudur**\n\n🌀 Bot Versiyası: `v0.7.0`\n🍀 Pyrogram Versiyası: `1.4.16`\n⚡ Python Versiyası: `3.11.1`\n⚙️ Server: [Heroku](https://heroku.com)\n📆 Botun istifadəyə verilmə tarixi: `13.03.2023`\n\n**⚠️ Qeyd: Botun qrupunuzda işləməsi üçün admin əmrlərindən sadəcə (Mesaj Silmə) yetkisi verin**"""


    SAHIB_TEXT = """🔮 İstifadə: /stats\n💁 Açıqlama: Bot haqqında ümumi məlumat verər\n\n🔮 İstifadə: /block\n🚧 Açıqlama: İstifadəçini və ya qrupu bloklayar\n\n🔮 İstifadə: /unblock\n🗝️ Açıqlama: İstifadəçini və ya qrupun bloku açar\n\n🔮 İstifadə: /blocklist\n🗒️ Açıqlama: Blok olunanların siyahısını göstərər\n\n🔮 İstifadə: /broadcastall\n📢 Açıqlama: Qrupa və şəxsiyə yayım edər\n\n🔮 İstifadə: /gcast\n💬 Açıqlama: Qruplarda yayım edər\n\n🔮 İstifadə: /broadcast_pin\n🗣️ Açıqlama: Qruplarda yayım edər və sabitləyər\n\n🔮 İstifadə: /dyno\n🌐 Açıqlama: Heroku dyno miqdarını ölçər\n\n🔮 İstifadə: /pin\n📌 Açıqlama: Mesajı sabitləyər\n\n🔮 İstifadə: /unpin\n♦️ Açıqlama: Sabitləməni qaldırar"""

    MUSIC_TEXT = """📀 İstifadə: /song\n➡️ Nümunə: `/song Balaeli & Nefes - Gizli Esq`\n🎧 Açıqlama: Musiqi yükləyər\n\n📀 İstifadə: /video\n➡️ Nümunə: `/video Balaeli & Nefes - Gizli Esq`\n🎧 Açıqlama: Video yükləyər\n\n📀 İstifadə: /lyrics\n➡️ Nümunə: `/lyrics Balaeli & Nefes - Gizli Esq`\n🎧 Açıqlama: Musiqinin sözlərini tapar"""

    TELEGRAPH_TEXT = """🔮 İstifadə: /tgm\n🔗 Açıqlama: Şəkil, Video və ya GIF göndərərək link ala bilərsiniz"""

    SEHID_TEXT = """🔮 İstifadə: /sehid\n🇦🇿 Açıqlama: Bu əmr vasitəsilə bot sizə **Şəhid** adları göndərəcək\n\n🥀 **Allah bütün Şəhidlərimizə rəhmət eləsin**\n🤲 Qazilərimizə şəfa versin\n😔 Başın sağolsun Azərbaycan 🇦🇿\n🇦🇿 Bazada **2881** Şəhid adı mövcuddur""" 
    OYUN_TEXT = """🔮 İstifadə: /oyna\n➔ Açıqlama: Oyunu başladar\n\n🔮 İstifadə: /kec\n➔ Açıqlama: Sözü keçər\n\n🔮 İstifadə: /dayan\n➔ Açıqlama: Oyunu dayandırar\n\n🔮 İstifadə: /reytinq\n➔ Açıqlama: Qruplar üzrə sıralaması göstərər\n\n═════════════════\n\n🔮 İstifadə: /zer\n🎲 Açıqlama: Zər atar\n\n🔮 İstifadə: /top\n⚽ Açıqlama: Top atar\n\n🔮 İstifadə: /bowling\n🎳 Açıqlama: Bowling atar\n\n🔮 İstifadə: /ox\n🎯 Açıqlama: Ox atar\n\n🔮 İstifadə: /jackpot\n🕹️ Açıqlama: Jackpot atar\n\n🔮 İstifadə: /basket\n🏀 Açıqlama: Basket atar"""

    EYLENCE_TEXT = """🔮 İstifadə: /ship\n💕 Açıqlama: Qrupda cütlük seçər\n\n🔮 İstifadə: /mal\n💹 Açıqlama: Mal faizini yoxlayar\n\n🔮 İstifadə: /esq\n💕 Açıqlama: Eşq faizini yoxlayar\n\n🔮 İstifadə: /soxri\n🖼️ Açıqlama: 16+ şəkillər atar\n\n🔮 İstifadə: /pisik\n🐈 Açıqlama: Pişik şəkillər atar\n\n🔮 İstifadə: /anime\n💢️ Açıqlama: Anime şəkillər atar\n\n🔮 İstifadə: /masin\n🚘 Açıqlama: Maşın şəkillər atar\n\n🔮 İstifadə: /masin2\n🚗 Açıqlama: Maşın videolar atar\n\n🔮 İstifadə: /tema\n🌈 Açıqlama: Telegram temalar atar\n\n🔮 İstifadə: /pp\n🦄 Açıqlama: Profil şəkillər atar\n\n🔮 İstifadə: /sevgi\n💞 ️Açıqlama: Sevgi sözlər atar\n\n🔮 İstifadə: /bio\n✍️ Açıqlama: Bio sözlər atar"""


    ELAVELER_TEXT = """🔮 İstifadə: /carbon\n🖼️ Açıqlama: Yazdığınız mesajı şəkilə çevirər\n\n🔮 İstifadə: /id\n🆔 Açıqlama: İstifadəçi ID atar\n\n🔮 İstifadə: /info\nℹ️ Açıqlama: İstifadəçi haqqında məlumat atar\n\n🔮 İstifadə: /alive\n⚡ Açıqlama: Botun işlək olduğunu yoxlayar"""


    AXTARIS_TEXT = """🔮 İstifadə: /github\n🧩 Nümunə: `/github Rahid2003`\n🕵️ Açıqlama: Github axtarışı edər\n\n🔮 İstifadə: /search\n🧩 Nümunə: `/search Balaeli & Nefes - Gizli Esq`\n🔍 Açıqlama: YouTube axtarış üçün istifadə edə bilərsiniz"""

    TAGGER_TEXT = """🔮 İstifadə: /tag\n👥 Açıqlama: 5-li tağ edər\n\n🔮 İstifadə: /tektag\n👤 Açıqlama: Təkli tağ edər\n\n🔮 İstifadə: /stag\n📜 Açıqlama: Maraqlı sözlərlə tağ edər\n\n🔮 İstifadə: /etag\n🥰 Açıqlama: Emoji ilə tağ edər\n\n🔮 İstifadə: /btag\n🏴 Açıqlama: Bayraqlarla tağ edər\n\n🔮 İstifadə: /admin\n👨‍⚖️ Açıqlama: Qrup adminlərin siyahısı atar\n\n🔮 İstifadə: /cancel\n🛑 Açıqlama: Tağ prosesi dayandırar"""



##### Broadcast Mesajları


class LAN(object):


    BILDIRIM = """**🆕 Yeni istifadəçi bota start etdi**\n\n👤 {}\n🆔 `{}`\n🔗 [{}](tg://user?id={})"""
    GRUP_BILDIRIM = """**🆕 Yeni istifdəçi bota qrupda start etdi**\n\n👤 Qrupa əlavə edən: `{}`\n🆔 Qrupa əlavə edən istifadəçi id: `{}`\n🔗 Profil linki: [{}](tg://user?id={})\nQrupun Adı: {}\nQrupun ID: {}\nQrupun mesaj linki (Sadəcə açıq qruplar): [Bura Toxun](https://t.me/c/{}/{})

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
istifadəçi ID yanlışdır.
"""
    BROADCAST_STARTED = """
```📥 Reklam yayımı başladı!\nBitəndə mesaj göndərəcəm
"""
    BROADCAST_STOPPED = """
```✅ Reklam yayımı uğurla tamamlandı.```\n\n**Bu qədər vaxtda tamamlandı** `{}`\n\n**Ümumi istifadəçilər:** `{}`\n\n**Ümumi göndərmə cəhdləri:** `{}`\n\n**Uğurla göndərilən:** `{}`\n\n**Ümumi xəta:** `{}`
"""
    STATS_STARTED = """
{} **Zəhmət olmasa gözləyin, bilgiləri gətirirəm!**
"""
    STATS = """
**@{} Məlumatları**\n\n**İstifadəçiləri;**\n» Ümumi: `{}`\n» Qruplar: `{}`\n» Şəxsi: `{}`\n\n**Disk İstifadəsi;**\n» Disk'in Sahəsi: `{}`\n» İstifadə Edilən: `{} ({}%)`\n» Boş Qalan: `{}`\n\n**🎛 Ən yüksək istifadə dəyərləri;**\n» CPU: `{}%`\n» RAM: `{}%`\n» Pyrogram: {}
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
🆓 **İstifadəçinin qadağası qaldırıldı!** \nQadağanı qaldıran: {}\n**İstifadəçi ID:** `{}`
"""
    USER_UNBAN_NOTIFY = """
🎊 Sizə gözəl bir xəbərim var! Artıq əngəliniz qaldırıldı!
"""
    BLOCKS = """
🆔 **İstifadəçi ID:** `{}`\n⏱ **Vaxt:** `{}`\n🗓 **Qadağan edildiyi tarix:** `{}`\n💬 **Səbəb:** `{}`\n\n"""
    TOTAL_BLOCK = """
🚷 **Ümumi əngəllənən:** `{}`\n\n{}
"""