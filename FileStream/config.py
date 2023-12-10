from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = 27885485
    API_HASH = "7dd9974c713787410beae4a295cc1e2d"
    BOT_TOKEN = "5814606535:AAHMKvgSMunxFpVqT8cu3icMnkux7H5bFlY"
    OWNER_ID = 6360808740
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = "mongodb+srv://sanmart02:sanmart02@cluster0.mwmbwqz.mongodb.net/?retryWrites=true&w=majority"
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Telegram"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_UPDATES_CHANNEL = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_UPDATES_CHANNEL = True if str(FORCE_UPDATES_CHANNEL).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    IMAGE_FILEID = env.get('IMAGE_FILEID', "https://telegra.ph/file/5bb9935be0229adf98b73.jpg")
    MULTI_CLIENT = False
    LOG_CHANNEL = -1001712664367
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = "6360808740 6069809284 6238111690 5872654872"

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = "true"
    NO_PORT = 443
    FQDN = "app-assistirvideos.koyeb.app"
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
    KEEP_ALIVE = str(env.get("KEEP_ALIVE", "0").lower()) in ("1", "true", "t", "yes", "y")


