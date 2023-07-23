import asyncio

import speedtest
from pyrogram import filters

from FallenMusic import SUDOERS, app


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ Yükləmə sürət testi işləyir...**")
        test.download()
        m = m.edit("**⇆ Yükləmə sürət testi işləyir...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ Speedtest nəticələrinin paylaşılması...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spt"]) & SUDOERS)
async def speedtest_function(_, message):
    m = await message.reply_text("**» Sürət testi...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **Speedtest nəticələri** ✯
    
<u>**❥͜͡Müştəri :**</u>
**» __isp :__** {result['client']['isp']}
**» __ölkə :__** {result['client']['country']}
  
<u>**❥Server :**</u>
**» __Ad :__** {result['server']['name']}
**» __ölkə :__** {result['server']['country']}, {result['server']['cc']}
**» __Sponsor :__** {result['server']['sponsor']}
**» __Gecikmə :__** {result['server']['latency']}  
**» __Ping :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
