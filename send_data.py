import asyncio
import json
import logging
import datetime

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

async def send_data(user_name, user_age, user_phone, cource_name):
    now = datetime.datetime.now()
    current_date = now.strftime("%d.%m.%Y %H:%M")

    msg = f"====== Новая заявка ======\n\nПользователь: {user_name}\nВозраст: {user_age}\nНомер телефона: {user_phone}\nНаправление: {cource_name}\n\nДата подачи:\n{current_date}"

    for admin in ADMINS:
        try:
            logger.debug(await bot.send_message(admin, msg))
        except Exception as err:
            logger.error(f"{err}")