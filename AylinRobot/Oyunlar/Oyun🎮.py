import os
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from helpers.filters import command
from pyrogram import Client, filters
import random

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
    
  

games = [
    {"name": "dice", "emoji": "🎲"},
    {"name": "darts", "emoji": "🎯"},
    {"name": "soccer", "emoji": "⚽️"},
    {"name": "slot machine", "emoji": "🎰"},
    {"name": "basketball", "emoji": "🏀"},
    {"name": "bowling", "emoji": "🎳"}
]

def play_game(game_name):
    for game in games:
        if game["name"].lower() == game_name.lower():
            emoji = game["emoji"]
            break
    else:
        emoji = games[0]["emoji"]
    return emoji, random.randint(1, 6)

@app.on_message(command(["zar"]))
async def handle_play_command(bot, message):
    if len(message.command) == 1:
        await message.reply("Which game do you want to play? Available games: " + ", ".join([game["name"] for game in games]))
        return
    emoji, number = play_game(message.command[1])
    await bot.send_dice(message.chat.id, emoji)
    await bot.send_message(message.chat.id, f"You rolled a {number}!")
    