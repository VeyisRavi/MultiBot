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



temalar = [" [Rahid](https://t.me/addtheme/sf158WSw7LWOtpvV) ",
" [Rahid](https://t.me/addtheme/bpcrFtP4qYu0DdnJ) " ,
" [Rahid](https://t.me/addtheme/aUFKCX7AQ3aQpDjp) " ,
" [Rahid](https://t.me/addtheme/L7HVQjC4UUyOfL9y) " ,
" [Rahid](https://t.me/addtheme/Qd4eBWTIOH4Ai3Zv) " ,
" [Rahid](https://t.me/addtheme/NightWolf) " ,
" [Rahid](https://t.me/addtheme/GreenBlack) " ,
" [Rahid](https://t.me/addtheme/TvldPzYmpG8LqkY3) " ,
" [Rahid](https://t.me/addtheme/Q4GuvNPpMvG59G6V) " ,
" [Rahid](https://t.me/addtheme/kGQaW0HHsjc7oFOv) " ,
" [Rahid](https://t.me/addtheme/z3E6vkceX0pfmo5P) " ,
" [Rahid](https://t.me/addtheme/poMW3amfnwUwOefI) " ,
" [Rahid](https://t.me/addtheme/l1felAbEVNQCN3NW) " ,
" [Rahid](https://t.me/addtheme/y6xMaSuBOmuGekHj) " ,
" [Rahid](https://t.me/addtheme/Fp6h6JpzXrWnjF9y) " ,
" [Rahid](https://t.me/addtheme/Purple_Grapes) " ,
" [Rahid](https://t.me/addtheme/xQNP1Jp2aklmldNx) " ,
" [Rahid](https://t.me/addtheme/ry0AgHsISs439fxi) " ,
" [Rahid](https://t.me/addtheme/ZHl93FYO9ja7hN81) " ,
" [Rahid](https://t.me/addtheme/gc2MlPyKHMBjw5WS) " ,
" [Rahid](https://t.me/addtheme/ciNZt5N6QCFjsrQI) " ,
" [Rahid](https://t.me/addtheme/bEKOF0v8XuLAFZ6P) " ,
" [Rahid](https://t.me/addtheme/IOSTelegramThemes2020_11july) " ,
" [Rahid](https://t.me/addtheme/DarkPink_1) " ,
" [Rahid](https://t.me/addtheme/Halloween_04) " ,
" [Rahid](https://t.me/addtheme/BlackBlue_ByYamila) " ,
" [Rahid](https://t.me/addtheme/NewYorkNyVK) " ,
" [Rahid](https://t.me/addtheme/blackcircles_ByYamila) " ,
" [Rahid](https://t.me/addtheme/KINGByVK) " ,
" [Rahid](https://t.me/addtheme/MRPERFECTBYVK) " ,
" [Rahid](https://t.me/addtheme/ChanchiNeonByVK) " ,
" [Rahid](https://t.me/addtheme/SamurayByVK) " ,
" [Rahid](https://t.me/addtheme/NeonRocks_ByYamila) " ,
" [Rahid](https://t.me/addtheme/StichOhanaByVK) " ,
" [Rahid](https://t.me/addtheme/SkullDarkByVK) " ,
" [Rahid](https://t.me/addtheme/RedGirlByVK) " ,
" [Rahid](https://t.me/addtheme/SpidermanByVK) " ,
" [Rahid](https://t.me/addtheme/CuteMelodyByVK) " ,
" [Rahid](https://t.me/addtheme/YouAreBeautifulStichByVK) " ,
" [Rahid](https://t.me/addtheme/ManchesterUnitedByVK) "]



@app.on_message(filters.command("tema"))
async def tema(app: Client, msg: Message):
    await msg.reply(random.choice(temalar))