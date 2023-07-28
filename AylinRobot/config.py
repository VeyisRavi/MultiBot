import os

class Config:

   API_ID = int(os.getenv("API_ID"))
   API_HASH = os.getenv("API_HASH")
   BOT_TOKEN = os.getenv("BOT_TOKEN")
   BOT_USERNAME = os.environ.get("BOT_USERNAME")
   BOT_NAME = os.environ.get("BOT_NAME")
   OWNER_ID = int(os.environ.get("OWNER_ID"))
   OWNER_NAME = os.environ.get("OWNER_NAME") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGO_DB_URI")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
   ALIVE_NAME = os.environ.get("ALIVE_NAME")
   CHANNEL = os.environ.get("SUPPORT_CHANNEL")
   SUPPORT = os.environ.get("SUPPORT_CHAT")
   ALIVE_IMG = os.environ.get("ALIVE_IMG") 
   START_IMG = os.environ.get("START_IMG")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
