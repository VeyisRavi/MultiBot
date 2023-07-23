import os

class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    #>>> https://t.me/BotFather
  
    API_ID = int(os.environ.get("API_ID", "16157584")
    API_HASH = os.environ.get("API_HASH", "2167d4e6007a79eed91d084bf5b8966a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6152708456:AAF2xfhqFeUEVzB01pHVWKbzyTmewczaUys")
    OWNER_ID = int(os.environ.get("OWNER_ID", "1280040987"))
