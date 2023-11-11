from os import getenv  # Added import statement for getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", ""))
    SUDO = list(map(int, getenv("SUDO", "").split()))  # Added split() with delimiter
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
