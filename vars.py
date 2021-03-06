import os
from os import getenv


class Config(object):
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
