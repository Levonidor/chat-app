
from functools import cache
from dotenv import load_dotenv
import pandas as pd
import os
from bot.app.cfg import default_keyboard

def build_keyboard(custom: list[str] = default_keyboard):
    kb = ReplyKeyboardBuilder()
    for element in custom:
        kb.button(text=element)
    kb.adjust(1, len(custom))
    return kb.as_markup(resize_keyboard=True)


def check_pathes() -> bool:
    if not os.path.exists("./userdata"):
        os.mkdir("./userdata")

def check_user(user_id: str) -> None:
    """
    Check if there is a files with this user data. And creates them if they weren't created before.

    False: if files were created now.
    True: if files were created before.
    """
    check_pathes()
    if not os.path.exists(f"./userdata/{user_id}.csv"):
        pd.DataFrame(columns=USERDATA_COLUMNS).to_csv(
            f"./userdata/{user_id}.csv", index=False
        )
        return False
    return True

@cache
def get_token() -> str:
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if token is None:
        raise ValueError("BOT_TOKEN is not set in the environment")
    return token
