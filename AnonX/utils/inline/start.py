from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✧ أضفني إلى مجموعتك ✧",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="مساعدة",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="الإعدادات", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✧ أضفني إلى مجموعتك ✧",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="مساعدة", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✧ المساعدة ✧", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="المطور الغالي", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="قناة السورس ",
                url=f"https://t.me/Mlze1bot",
            )
        ],
        [ 
            InlineKeyboardButton(
                text="اضغط هنا لتفعيل بوت حماية",
                url=f"https://t.me/smauabot?startgroup=true",
            ) 
        ], 
        ] 
    return buttons
