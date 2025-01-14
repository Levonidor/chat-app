from .columns import *
from datetime import datetime
import pandas as pd
from ..utils import check_user
import os.path


def add_timestamp(
    user_id: str, activity_type: str, activity_name: str, time: str
) -> None:
    check_user(user_id)
    user = pd.read_csv(f"./userdata/{user_id}.csv")
    time_obj = datetime.strptime(time, r"%Y-%m-%d %H:%M:%S")
    if len(user) != 0:
        user.loc[len(user) - 1] = [
            user.at[len(user) - 1, USERDATA.TYPE],
            user.at[len(user) - 1, USERDATA.NAME],
            user.at[len(user) - 1, USERDATA.TIMESTAMP],
            time_obj
            - datetime.strptime(
                user.at[len(user) - 1, USERDATA.TIMESTAMP], r"%Y-%m-%d %H:%M:%S"
            ),
        ]
    user.loc[len(user)] = [activity_type, activity_name, str(time_obj), 0]
    user.to_csv(f"./userdata/{user_id}.csv", index=False)


def remove_last_timestamp(user_id: str) -> None:
    if not check_user(user_id):
        raise ValueError("Nothing to delete")

    user = pd.read_csv(f"./userdata/{user_id}.csv")
    user = user.iloc[:-1]
    if len(user) != 0:
        user.loc[len(user) - 1] = [
            user.at[len(user) - 1, USERDATA.TYPE],
            user.at[len(user) - 1, USERDATA.NAME],
            user.at[len(user) - 1, USERDATA.TIMESTAMP],
            0,
        ]

    user.to_csv(f"./userdata/{user_id}.csv", index=False)
