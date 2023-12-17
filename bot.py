# (©)Codexbotz
# Recode By Zaen @Mafia_Tobatz
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod

import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL1,
    FORCE_SUB_CHANNEL2,
    FORCE_SUB_CHANNEL3,
    FORCE_SUB_CHANNEL4,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL1:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                self.invitelink1 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot cannot retrieve invitation link FORCE_SUB_CHANNEL1!"
                )
                self.LOGGER(__name__).warning(
                    f"Please check back var FORCE_SUB_CHANNEL1 and make sure your bot is an admin on a channel with link permission to invite users via the invitation link, Current Channel Subs: {FORCE_SUB_CHANNEL1}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Stopped. Join Group https://t.me/WD_Topic_Group for Help"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bots cannot Retrieve Invite links from FORCE_SUB_CHANNEL2!"
                )
                self.LOGGER(__name__).warning(
                    f"Please double check the var FORCE_SUB_CHANNEL2 and make sure your bot is an admin on the channel with link permission to invite users via the invitation link, Current Group Subs: {FORCE_SUB_CHANNEL2}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Stopped. Join Group https://t.me/WD_Topic_Group for Help"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL3:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL3)
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bots cannot Retrieve Invite links from FORCE_SUB_CHANNEL3!"
                )
                self.LOGGER(__name__).warning(
                    f"Please double check the var FORCE_SUB_CHANNEL3 and make sure your bot is an admin on a channel with link permission to invite users via the invitation link, Current Channel Subs: {FORCE_SUB_CHANNEL3}"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL4:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL4)
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bots cannot Retrieve Invite links from FORCE_SUB_CHANNEL4!"
                )
                self.LOGGER(__name__).warning(
                    f"Please double check the var FORCE_SUB_GROUP and make sure your bot is an admin on the channel with link permission to invite users via the invitation link, Current Group Subs: {FORCE_SUB_CHANNEL2}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Stopped. Join Group https://t.me/WD_Topic_Group for Help"
                )
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Make sure the Bot is an Admin on the DataBase Channel, and Double Check the Value CHANNEL_ID, Current Value: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "\nBot Stopped. Join Group https://t.me/WD_Topic_Group for Help"
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[⚡️ SUCCESSFULLY ACTIVATED! ⚡️]\n\nBOT Made by @{OWNER}\nif @{OWNER} Need Help, Please Ask https://t.me/WD_Contact_Bot"
        )
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
