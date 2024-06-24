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


async def back_button():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="На главную страницу", callback_data="to_menu"))
    builder.adjust(1)
    return builder.as_markup()

async def main_menu():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Записаться на курс", callback_data="register"))
    builder.add(types.InlineKeyboardButton(text="Наши филиалы", callback_data="branches"))
    builder.add(types.InlineKeyboardButton(text="Связаться с нами", callback_data="contacts"))
    builder.adjust(1)

    return builder.as_markup()

async def courses_list():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Компьютерная грамотность", callback_data="Компьютерная грамотность"))
    builder.add(types.InlineKeyboardButton(text="Web технологии", callback_data="Web технологии"))
    builder.add(types.InlineKeyboardButton(text="Дизайн и 3D", callback_data="Дизайн и 3D"))
    builder.add(types.InlineKeyboardButton(text="Программирование", callback_data="Программирование"))
    builder.add(types.InlineKeyboardButton(text="Интернет предпринимательство", callback_data="Интернет предпринимательство"))
    builder.add(types.InlineKeyboardButton(text="Искуственный интеллект", callback_data="Искуственный интеллект"))
    builder.add(types.InlineKeyboardButton(text="Разработка игр", callback_data="Разработка игр"))
    builder.add(types.InlineKeyboardButton(text="На главную страницу", callback_data="to_menu"))

    builder.adjust(1)

    return builder.as_markup()