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


async def is_phone_valid(phone):
    return re.match(r"^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$", phone)


@dp.message(CommandStart())
async def hello_message(message: Message) -> None:
    global user_id

    user_id = message.from_user.id
    logger.info(f"{user_id} started the bot")
    
    await message.answer(HELLO_MESSAGE, reply_markup=await main_menu())

@dp.callback_query(F.data == "to_menu")
async def to_main_menu(callback: types.CallbackQuery):
    logger.info(f"User: {user_id} opened main page")
    await callback.message.edit_text(HELLO_MESSAGE, reply_markup=await main_menu())

@dp.callback_query(F.data == "branches")
async def branches(callback: types.CallbackQuery):
    logger.info(f"User: {user_id} opened branches page")
    await callback.message.edit_text(BRANCHES_INFO, reply_markup=await back_button())

@dp.callback_query(F.data == "contacts")
async def branches(callback: types.CallbackQuery):
    logger.info(f"User: {user_id} opened contacts page")
    await callback.message.edit_text(CONTACTS_INFO, reply_markup=await back_button())


@dp.callback_query(F.data == "register")
async def register(callback: types.CallbackQuery):
    logger.info("Senging courses list to user")
    await callback.message.edit_text("Выберите интересующее направление: ", reply_markup=await courses_list())

@dp.callback_query()
async def get_course_name(callback: types.CallbackQuery):
    global course_name, isRegister

    logger.info("Senging question to user")
    await callback.answer()
    course_name = callback.data

    logger.info(f"User: {user_id} selected: {course_name}")
    isRegister = True
    logger.info(f"isRegister: {isRegister}")

    await callback.message.answer(f"Вы выбрали направление {course_name}\n{REGISTER_MESSAGE}")


@dp.message()
async def get_data(message: Message):
    logger.info(f"User: {user_id} sending his data")
    logger.info(f"isRegister: {isRegister}")
    if isRegister == True:
        data = message.text
        split_data = data.split(" ")

        if  await is_phone_valid(split_data[1]):
            if len(split_data) == 3:
                user_name = split_data[0]
                user_phone = split_data[1]
                user_age = split_data[2]
                
                await send_data(user_name, user_age, user_phone, course_name)

                await message.answer(AFTER_MESSAGE)
                
            else:
                await message.answer("Неправильный формат ввода.\nПопробуйте заново")
        else:
            await message.answer("Неправильно введён номер телефона.\nПопробуйте заново")
    else:
        await message.answer(HELLO_MESSAGE, reply_markup=await main_menu())
