import asyncio
import json
import logging

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

async def send_data(user_name, user_age, user_phone, cource_name):
    msg = f"Пользователь: {user_name}\nВозраст: {user_age}\nНомер телефона: {user_phone}\nНаправление: {cource_name}"

    for admin in ADMINS: 
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={admin}&text={msg}"
        logger.info((requests.get(url).json()))
