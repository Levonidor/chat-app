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
from .cfg import default_keyboard
from .utils import build_keyboard


router = Router()

@router.message(Command('start'))
async def start_handler(msg: Message, state: FSMContext) -> None:
    if msg.from_user.id == ADMIN_ID:
        await msg.answer("Привет, администратор")
    else:
        await msg.answer("hello")



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
