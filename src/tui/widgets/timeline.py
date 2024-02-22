from textual.events import Mount
from textual.widget import Widget
from textual.widgets import Log
from mipac.models.note import Note

from src.tui.store.timeline import TIMELINE


class TimelineWidget(Widget):
    def compose(self):
        yield Log(id="timeline", name="Timeline")

    def _on_mount(self, event: Mount) -> None:
        TIMELINE.subscribe(self._on_update_timeline)
        return super()._on_mount(event)

    def _on_update_timeline(self, timeline: list[Note]):
        _timeline = self.query_one(Log)
        _timeline.clear()
        for note in timeline:
            _timeline.write_line(f"{note.user.username}: {note.text}")
