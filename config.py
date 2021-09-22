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
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = 8997742
API_HASH = "414ef4da4921ef3fd3632d017513e139"
BOT_TOKEN = "2017737389:AAFNAZ-rZTVmwrkTZ32wToIhzZTIZTzvP2c"
SESSION_STRING = """BQAB76WbqaDrSpFEIYz7jkzElVQVAf6wDhHlrY7Pa21bSj1LmG-l-kkAhXPr89tQUSWeNWi_Sb_QVJ4OTLuGTy9fA5kv2pmw9amRPZEUSt2eNcbDgnvVpvUyizSOKlQfWVGXB8kFf5JMh_SFauZ5zwAkw3uYfsNK_AYeWtcBNgFtWEX0bhRDEZR-LnBoBPKYTo_tZgWquB0U-EaX06j8zq9HR6qbMYfKlynkUkvjj7DKuOooPn5PpVzTa3_TohW4vwxR6t-t3CJYDQzaGob5FABJJvxDhV1dLi-VGh-dhv5e795pPGEA7csTuPPoJtVGmQL2F2svP5Zic6mx-cwxWgD-dOTZAgA
"""
SUPPORT_GROUP = "vstreamtest1"
UPDATES_CHANNEL = ""
ASSISTANT_NAME = "vsassist1"
SUDO_USERS = [1961154818]
REPLY_MESSAGE = "I am busy, please speak with the experts. "
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
