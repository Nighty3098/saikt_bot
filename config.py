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
# ADMIN = "376442808" # "@max_bobrovskiy"
ADMIN = "1660218648"  # "@Night3098"

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

logger = loguru.logger
logger.add("SAIKT_TG.log", level="DEBUG", rotation="10 MB", retention="7 days", format="{time} {level} {message}")
#logger.add(lambda msg: print(msg), level="DEBUG", format="{time} {level} {message}, serialize: True, backtrace=True, diagnose=True")
logger.level("INFO", color="<cyan>")
