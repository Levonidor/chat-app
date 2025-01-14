from .token import BOT_TOKEN, ADMIN_ID
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import *
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
router = Router()
default = ['Привет', 'Пока']
'''kb = ReplyKeyboardBuilder()
        kb.button(text="Таблица пользователей")
        kb.button(text="Очистить таблицу")
        kb.button(text="Ответить пользователю")
        kb.adjust(1, 1, 1)
        await msg.answer("Доступные Команды", reply_markup=kb.as_markup(resize_keyboard=True))'''

def building_keyboard(custom=default):
    kb = ReplyKeyboardBuilder()
    for element in custom:
        kb.button(text=element)
    kb.adjust(1, len(custom))
    return kb.as_markup(resize_keyboard=True)

class update(StatesGroup):
    smth = State

@router.message(Command('start'))
async def start_handler(msg: Message, state: FSMContext) -> None:
    if msg.from_user.id == ADMIN_ID:
        await msg.answer("Привет, администратор")
    else:
        await msg.answer("hello")
        await msg.answer("choose", reply_markup=building_keyboard())


@router.message(Command('menu'))
async def menu_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer('/activate')
    await msg.answer('/terminate')
    await msg.answer('/custom')
    await msg.answer('/show')


@router.message(Command('activate'))
async def activate_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer('1')



@router.message(Command('terminate'))
async def terminate_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer('2')


@router.message(Command('custom'))
async def custom_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer('3')


@router.message(Command('show'))
async def show_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer('4')
