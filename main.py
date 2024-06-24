#!/usr/bin/python3

import asyncio
import json
import logging
import re

import requests
from aiogram import *
from aiogram.enums import *
from aiogram.filters import *
from aiogram.types import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import *
from requests.models import *

from config import *
from MESSAGES_TEXT import *
from kb_builders import *
from send_data import *
from send_logs import *
from handlers import *

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
