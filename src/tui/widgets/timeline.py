from textual.events import Mount
from textual.widget import Widget
from textual.widgets import RichLog
from rich.panel import Panel
from mipac.models.note import Note

from src.tui.store.timeline import TIMELINE


class TimelineWidget(Widget):
    def compose(self):
        yield RichLog(
            id="timeline", name="Timeline", highlight=True, markup=True, auto_scroll=False
        )

    def _on_mount(self, event: Mount) -> None:
        TIMELINE.subscribe(self._on_update_timeline)
        return super()._on_mount(event)

    def _on_update_timeline(self, timeline: list[Note]):
        _timeline = self.query_one(RichLog)
        _timeline.clear()
        for note in timeline:
            if note.text is None:
                continue
            _timeline.write(
                Panel(
                    f"{note.text}",
                    title=f"[bold magenta]{note.user.username}[/bold magenta][default] | {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n\n",
                    title_align="left",
                    subtitle=note.url,
                    subtitle_align="right",
                ),
                expand=True,
            )
