from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 0))
        self.API_HASH = getenv("API_HASH")

        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.MONGO_URL = getenv("MONGO_URL")

        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = int(getenv("OWNER_ID", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", None)
        self.SESSION2 = getenv("SESSION2", BQCZzqEAZqgaNTCW8YUJIah_1kF4N861t9RSgK1og4cU-ayuxxcreoFTlPhO3TJjCAbjejnsFEN5bDU9o21rIG8oea89GgUBvXuzTChrWiCLoRpJvjf6CMtSmjX_9GUepN7noS57bZe_9fdz-t2MyX7YRy2cIMMtYuxDc6m1pGPwLxRYwIaGPki9U990UFSebzGd1wfM45G-U-UxtjBHX6Lq2J3DL_ClMHLtcFkX9NkNa8tNySQrBocQDwC3C7gyNDtj8RDCtFvu7kRBbiSNykfqV-p8sBDljlRBJIE4-xdqtaHopTkoTSogXQzPv-rvHF6B6XQkgBjhDAeM_109Z70_hkBnWAAAAAFTJMFHAA)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/basiiupdates")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/basiimusicchat")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://files.catbox.moe/50oamq.png")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/cq46wa.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/kye3nt.png")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
