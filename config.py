import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token from @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7484214225:AAHFIKFIFXpSk2Tojm7Kkqvso2B487mVMXA")

# API ID and Hash from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21534788"))
API_HASH = os.environ.get("API_HASH", "b7b0c58e32c725914c2c1483a621c57a")

# Channel and owner IDs
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002474023462"))
OWNER_ID = int(os.environ.get("OWNER_ID", "5749343005"))

# Port configuration
PORT = os.environ.get("PORT", "8080")

# Database configuration
DB_URI = "mongodb+srv://ANDHAKA:ANDHAKA@test.fhbrg.mongodb.net/?retryWrites=true&w=majority&appName=test"
DB_NAME = os.environ.get("DATABASE_NAME", "ANDHAKA")

# Shortlink service
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "modijiurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "ce697224b36537a120f9beb25af240c55c5ade97")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200))  # seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "gojfsi/2")

# Force subscribe channel
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002382423357"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start and force subscription messages
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in the specified channel and other users can access it from a special link.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me.\n\nKindly please join the Channel.</b>")

# Custom caption and content protection settings
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Admin management
ADMINS = []
try:
    for x in os.environ.get("ADMINS", "5749343005").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER_ID)
ADMINS.append(6852649461)  # Add additional admin ID

# Logging setup
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
