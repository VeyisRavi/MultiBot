import os
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from helpers.filters import command

@app.on_message(command("zer"))
async def roll_dice(bot, message):
    await app.send_dice(message.chat.id, "🎲")


@app.on_message(command("ox"))                                      
async def roll_arrow(bot, message):
    await app.send_dice(message.chat.id, "🎯")

@app.on_message(command("top"))
async def roll_goal(bot, message):
    await app.send_dice(message.chat.id, "⚽️")

@app.on_message(command("jackpot"))
async def roll_luck(bot, message):
    await app.send_dice(message.chat.id, "🎰")

@app.on_message(command("basket"))
async def roll_throw(bot, message):
    await app.send_dice(message.chat.id, "🏀")

@app.on_message(command(["bowling"]))
async def roll_bowling(bot, message):
    await app.send_dice(message.chat.id, "🎳")