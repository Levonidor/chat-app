from .cfg import *
from datetime import datetime
import pandas as pd

import os.path


def check_pathes() -> bool:
    if not os.path.isdir('./userdata'):
        os.mkdir('./userdata')


def check_user(user_id: str) -> None:
    """
    Check if there is a files with this user data. And creates them if they weren't created before.

    False: if files were created now.
    True: if files were created before.
    """
    check_pathes()
    if not os.path.exists(f'./userdata/{user_id}.csv'):
        pd.DataFrame(columns=USERDATA_COLUMNS).to_csv(f'./userdata/{user_id}.csv',index=False)
        return False
    return True

def add_timestamp(user_id: str, activity: str, time: datetime) -> None:
    check_user(user_id)
    user = pd.read_csv(f'./userdata/{user_id}.csv')
    user.loc[len(user)] = [str(activity), str(time)]
    user.to_csv(f'./userdata/{user_id}.csv',index=False)

def remove_last_timestamp(user_id: str) -> None:
    if not check_user(user_id):
        return Exception("Nothing to delete")
    user = pd.read_csv(f'./userdata/{user_id}.csv')
    user = user.iloc[:-1]
    user.to_csv(f'./userdata/{user_id}.csv',index=False)
