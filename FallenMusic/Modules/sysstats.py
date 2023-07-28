import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from FallenMusic import BOT_NAME, SUDOERS, app
from FallenMusic.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"Almaq {BOT_NAME} Sistem statistikası, bir az vaxt aparacaq..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "Almaq alınmadı"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
➻ <u>**{BOT_NAME} Sistem Statistikası**</u>

**Python :** {pyver.split()[0]}
**Piroqram :** {pyrover}
**py-tg zəngləri :** {pytgver}
**Sudoçular :** `{sudoers}`
**Modullar :** `{mod}`

**ip :** {ip_address}
**Makintoş :** {mac_address}
**Host adı :** {hostname}
**Platforma :** {sp}
**Prosessor :** {processor}
**Memarlıq :** {architecture}
**Platformanın buraxılışı :** {platform_release}
**Platforma versiyası :** {platform_version}

        <b><u>Saxlama</b><u/>
**Mövcuddur :** {total[:4]} ɢɪʙ
**İstifadə edir :** {used[:4]} ɢɪʙ
**Pulsuz :** {free[:4]} ɢɪʙ

**Ram :** {ram}
**Fiziki nüvələr :** {p_core}
**Ümumi nüvələr :** {t_core}
**CPU Tezliyi :** {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Bağlayın",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )
