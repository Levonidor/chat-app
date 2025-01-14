import os
from functools import cache
from pathlib import Path
from typing import List, Optional

import pandas as pd
from dotenv import load_dotenv

from app.cfg import default_keyboard
from .handlers import ReplyKeyboardBuilder
from .services.columns import USERDATA_COLUMNS

def build_keyboard(custom: Optional[List[str]] = None) -> ReplyKeyboardBuilder:
    """
    Build a custom keyboard with the given buttons.

    Args:
        custom (Optional[List[str]]): List of button texts. Defaults to default_keyboard.

    Returns:
        ReplyKeyboardMarkup: The built keyboard.
    """
    custom = custom or default_keyboard
    kb = ReplyKeyboardBuilder()
    kb.add(*[kb.button(text=element) for element in custom])
    kb.adjust(1, len(custom))
    return kb.as_markup(resize_keyboard=True)

def ensure_userdata_directory(path: str = "./userdata") -> None:
    """
    Ensure the userdata directory exists.

    Args:
        path (str): Path to the userdata directory. Defaults to "./userdata".
    """
    Path(path).mkdir(exist_ok=True)

def check_user(user_id: str) -> bool:
    """
    Check if there is a file with this user's data and create it if it doesn't exist.

    Args:
        user_id (str): The user's ID.

    Returns:
        bool: True if the file already existed, False if it was just created.
    """
    ensure_userdata_directory()
    user_file = Path(f"./userdata/{user_id}.csv")
    if not user_file.exists():
        pd.DataFrame(columns=USERDATA_COLUMNS).to_csv(user_file, index=False)
        return False
    return True

@cache
def get_token() -> str:
    """
    Get the bot token from environment variables.

    Returns:
        str: The bot token.

    Raises:
        ValueError: If BOT_TOKEN is not set in the environment.
    """
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if token is None:
        raise ValueError("BOT_TOKEN is not set in the environment")
    return token
