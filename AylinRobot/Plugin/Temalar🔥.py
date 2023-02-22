# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Mamana Salam De 

import random
from random import choice
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from AylinRobot.config import Config



temalar = [" [Aylin](https://t.me/addtheme/sf158WSw7LWOtpvV) ",
" [Aylin](https://t.me/addtheme/bpcrFtP4qYu0DdnJ) " ,
" [Aylin](https://t.me/addtheme/aUFKCX7AQ3aQpDjp) " ,
" [Aylin](https://t.me/addtheme/L7HVQjC4UUyOfL9y) " ,
" [Aylin](https://t.me/addtheme/Qd4eBWTIOH4Ai3Zv) " ,
" [Aylin](https://t.me/addtheme/NightWolf) " ,
" [Aylin](https://t.me/addtheme/GreenBlack) " ,
" [Aylin](https://t.me/addtheme/TvldPzYmpG8LqkY3) " ,
" [Aylin](https://t.me/addtheme/Q4GuvNPpMvG59G6V) " ,
" [Aylin](https://t.me/addtheme/kGQaW0HHsjc7oFOv) " ,
" [Aylin](https://t.me/addtheme/z3E6vkceX0pfmo5P) " ,
" [Aylin](https://t.me/addtheme/poMW3amfnwUwOefI) " ,
" [Aylin](https://t.me/addtheme/l1felAbEVNQCN3NW) " ,
" [Aylin](https://t.me/addtheme/y6xMaSuBOmuGekHj) " ,
" [Aylin](https://t.me/addtheme/Fp6h6JpzXrWnjF9y) " ,
" [Aylin](https://t.me/addtheme/Purple_Grapes) " ,
" [Aylin](https://t.me/addtheme/xQNP1Jp2aklmldNx) " ,
" [Aylin](https://t.me/addtheme/ry0AgHsISs439fxi) " ,
" [Aylin](https://t.me/addtheme/ZHl93FYO9ja7hN81) " ,
" [Aylin](https://t.me/addtheme/gc2MlPyKHMBjw5WS) " ,
" [Aylin](https://t.me/addtheme/ciNZt5N6QCFjsrQI) " ,
" [Aylin](https://t.me/addtheme/bEKOF0v8XuLAFZ6P) " ,
" [Aylin](https://t.me/addtheme/IOSTelegramThemes2020_11july) " ,
" [Aylin](https://t.me/addtheme/DarkPink_1) " ,
" [Aylin](https://t.me/addtheme/Halloween_04) " ,
" [Aylin](https://t.me/addtheme/BlackBlue_ByYamila) " ,
" [Aylin](https://t.me/addtheme/NewYorkNyVK) " ,
" [Aylin](https://t.me/addtheme/blackcircles_ByYamila) " ,
" [Aylin](https://t.me/addtheme/KINGByVK) " ,
" [Aylin](https://t.me/addtheme/MRPERFECTBYVK) " ,
" [Aylin](https://t.me/addtheme/ChanchiNeonByVK) " ,
" [Aylin](https://t.me/addtheme/SamurayByVK) " ,
" [Aylin](https://t.me/addtheme/NeonRocks_ByYamila) " ,
" [Aylin](https://t.me/addtheme/StichOhanaByVK) " ,
" [Aylin](https://t.me/addtheme/SkullDarkByVK) " ,
" [Aylin](https://t.me/addtheme/RedGirlByVK) " ,
" [Aylin](https://t.me/addtheme/SpidermanByVK) " ,
" [Aylin](https://t.me/addtheme/CuteMelodyByVK) " ,
" [Aylin](https://t.me/addtheme/YouAreBeautifulStichByVK) " ,
" [Aylin](https://t.me/addtheme/ManchesterUnitedByVK) "]



@app.on_message(filters.command("tema"))
async def tema(app: Client, msg: Message):
    await msg.reply(random.choice(temalar))