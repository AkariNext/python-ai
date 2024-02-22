from mipac.models.note import Note

from src.utils.tui.storage import UseStorage


def vacuum_overflow(timeline: list[Note]) -> list[Note]:
    return timeline[-100:]


TIMELINE = UseStorage[list[Note]](default=[], callback=vacuum_overflow)
