from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PrimeMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="close")
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"], callback_data="settingsback_helper"
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data="close"
        ),
    ]
    mark = second if START else first
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb5",
                ),
            ],
            mark,
        ]
    )


def help_back_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"], callback_data="settings_back_helper"
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data="close"
                ),
            ]
        ]
    )


def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
