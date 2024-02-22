from mipac.models.note import Note

from src.utils.tui.storage import UseStorage


TIMELINE = UseStorage[list[Note]](default=[])
