import asyncio
import logging

from aiohttp import ClientWebSocketResponse
from rich.logging import RichHandler
from mipa.ext import commands
from mipac.models.note import Note

from config import settings
from src.tui.screen import TUIScreen
from src.tui.store.timeline import TIMELINE


logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger(__name__)


class PythonAi(commands.Bot):
    def __init__(self):
        super().__init__()

    async def _connect_channel(self, ws: ClientWebSocketResponse):
        await self.router.connect_channel(["global", "home", "main"])

    async def on_reconnect(self, ws: ClientWebSocketResponse):
        await self._connect_channel(ws)

    async def on_ready(self, ws: ClientWebSocketResponse):
        await self._connect_channel(ws)

    async def on_note(self, note: Note):
        timeline = TIMELINE.get()
        timeline.append(note)
        TIMELINE.set(timeline)


async def main():
    bot = PythonAi()
    app = TUIScreen()
    await asyncio.gather(
        bot.start(settings.BOT.url, settings.BOT.token, log_level=None),
        app.run_async(),
    )


if __name__ == "__main__":
    bot = PythonAi()
    asyncio.run(main())
