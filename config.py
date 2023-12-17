# (©)Codexbotz
# Recode By Dappa @mahadappa
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Token bot from @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# Your Hash API from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@Farooq_is_KING")

PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "True"))

HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")


# Database
DB_URI = os.environ.get("DATABASE_URL", "")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Opleech")
GROUP = os.environ.get("GROUP", "WD_Topic_Group")

# ID of the Channel or Group for which you must subscribe
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Prefix Message /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>🦋 Hello {first}</b>\n\n<b>I can save private files in Specific Channels and other users can access them from special links.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Your Admin list does not contain a valid Telegram User ID.")

# Message When Forcing to Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>🦋 Hello {first}\n\nYou must join my Channel/Group first to see the files I share\n\nPlease Join The Channel & Group First</b>",
)

# Set your Custom Text here, Save (None) to Disable Custom Text
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True if you want to Disable the Share Your Channel Posts button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(5827766615)


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
