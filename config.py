"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "25852187"))
API_HASH = getenv("API_HASH", "817bd34c0139d5819e79051da8a2a82f")
BOT_TOKEN = getenv("BOT_TOKEN", "7641782248:AAEqjuCghZTdFoYQECUrCI_ueAgaSwEWhJ8")
SESSION_STRING = getenv("SESSION_STRING", "BQGKeRsAseEddmE0D7jB9nO__36JS-NxEd70jm9GDHp8a4ZkL4o_U-AX8lKLdsfnTyp3a_5q3wW-oWKS_qJOxkN_Qpt293wvzLjRs_Rjrz4UYOR9Bx6kOvZpIYTHgyKr03my3sQLlnfKcOmEqtO_OTs5VRqvKoM8t4JI0jStI77vc6o0HTasi-bQ6fqPu0jXSTrUaGwrfj5j8HNu0PGVDsGxB1iZzTaIhLv1A_wzWPIuzA_I4E--_3AIEICIR8jdBzOH66GrutN2B-UYDqDmCqc7ZK4OxtDrzP1hoRmH9ui2sKJbvBf_YOA6cz9TdzT6mcnI_YOuyfynMCtZbVireOleGoQCVgAAAAEvo2aeAA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "IPxKINGYT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "IPxKINGYT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DESTROYER STREAMER")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "IPxKINGYT")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
