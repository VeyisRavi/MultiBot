from os import getenv
from dotenv import load_dotenv

load_dotenv()
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
OWNER_ID = int(getenv("OWNER_ID"))
PING_IMG = getenv("PING_IMG")
SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))


FAILED = "https://graph.org/file/35444b7d40fff28719e62.jpg"
