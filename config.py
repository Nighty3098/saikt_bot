import os
import sys
import pretty_errors
import loguru

from aiogram import *
from aiogram.enums import *
from aiogram.filters import *
from aiogram.types import *
from aiogram.utils.markdown import *
from loguru import *

TOKEN = os.getenv("SAIKT_BOT_TOKEN")
# ADMINS = ["376442808", "5122606203", "1660218648"] # saikt admins
ADMINS = ["1660218648"] # saikt admins
DEV = "1660218648" # developer

LOG_FILE = "SAIKT_TG.log"

bot = Bot(TOKEN)
dp = Dispatcher()

logger = loguru.logger
logger.add(LOG_FILE, level="DEBUG", rotation="10 MB", retention="14 days", format="{time} {level} {message}")
logger.level("INFO", color="<cyan>")
