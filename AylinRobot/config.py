# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "6711429"))
   API_HASH = os.getenv("API_HASH", "0bd538e224f28d8d8047d79f09a840ae")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "5318930158:AAEkLCS2D-OPj-qW0K4YgUQP4tUGCEQCS_Q")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "RahidRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "Rahid")
   OWNER_ID = int(os.environ.get("OWNER_ID", "571698989"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Rahid_7") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("mongodb+srv://rahidindi:rahidindi_1234@cluster0.ifslufs.mongodb.net/?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001864613336"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "RahidMusic")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001750384884"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001864613336"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "dbf30e04-cf9a-4e07-ac48-e4365a16362e")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Rahid")
   CHANNEL = os.environ.get("CHANNEL", "qruzdaa")
   SUPPORT = os.environ.get("SUPPORT", "FriendsAilesi")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/33c593637f4766883abed.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/aef1bdf8ef30b6ced6bbc.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())