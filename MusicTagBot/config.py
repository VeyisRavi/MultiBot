from os import getenv
from dotenv import load_dotenv

load_dotenv()
API_ID = int(getenv("API_ID", "16157584"))
API_HASH = getenv("API_HASH", "2167d4e6007a79eed91d084bf5b8966a")
BOT_TOKEN = getenv("BOT_TOKEN", "6152708456:AAF2xfhqFeUEVzB01pHVWKbzyTmewczaUys")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
OWNER_ID = int(getenv("OWNER_ID", "1280040987"))
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/9e5822e1e12f953f9a69c.jpg")
SESSION = getenv("SESSION", "AgBspnt1U3uV7wAjCSVAg_bJeDmRmCb1FPyz8LLQBWfUGJhEV4PcR91PhX9NSS7YrFhF1AKpTTOsocdsjr1RN1rOwEvROT6Y75w2QKHNJvnd7Z5FxReYYLXc1xZ8yEiSQzTPi_eakjg4dIMwOY2Vm_tmqEC9OguBv1dpKr-8Fm_wt7QiL6jJ10wOKg_gB1A5-F9eCGMM2SO4r_qfsrD8usX1TBzOoH-G5Jg2Clx0TRvHkG6fbonIhHedbEvuyPEYczg7STCN8iKzRh1ufNO9JoJiwgk9ER288a0D6qVdZIWjRb1MWTyjAeDhMKqSDIoGePYQpKcXqWubn6YNR_phsGYfAAAAAT-zwaUA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DejavuTeam")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DejavuSupport")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1280040987").split()))


FAILED = "https://graph.org/file/35444b7d40fff28719e62.jpg"
