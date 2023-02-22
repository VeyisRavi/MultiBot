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
   BOT_TOKEN = os.getenv("BOT_TOKEN", "5318930158:AAEzgLBqsu5UI9hCf_GLWB08N_Cz2dFKG9s")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "RahidRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "Rahid")
   OWNER_ID = int(os.environ.get("OWNER_ID", "571698989"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Rahid_7") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001864613336"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "RahidMusic")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001750384884"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1001864613336"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05a017d5-e3e5-424d-941f-3e60645e3141")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "RAHİD")
   CHANNEL = os.environ.get("CHANNEL", "Rahid_44")
   SUPPORT = os.environ.get("SUPPORT", "Cenublar")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/425d1e4790954b3d29e87.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b2c2ed59a89933a384ae3.jpg")
