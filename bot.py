from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
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
        self.uptime = datetime.now()

        # Handle FORCE_SUB_CHANNEL
        if FORCE_SUB_CHANNEL:
            try:
                chat = await self.get_chat(FORCE_SUB_CHANNEL)
                link = chat.invite_link or await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning("Error exporting invite link from Force Sub Channel!")
                sys.exit()

        # Check channel access
        try:
            self.db_channel = await self.get_chat(CHANNEL_ID)
            await self.send_message(chat_id=self.db_channel.id, text="Test Message").delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning("Ensure bot is an admin in the DB Channel.")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("Bot Running..!\n\nCreated by https://t.me/waspros")
        self.username = usr_bot_me.username

        # Setup web server
        app = web.Application()
        app.add_routes([web.get('/', self.handle)])
        runner = web.AppRunner(app)
        await runner.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(runner, bind_address, PORT).start()

    async def handle(self, request):
        return web.Response(text="Hello, world!")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

# Main execution
if __name__ == "__main__":
    bot = Bot()
    bot.run()
