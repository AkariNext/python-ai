from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from src.tui.widgets.bot_info import BotInfoWidget

from src.tui.widgets.timeline import TimelineWidget


class TUIScreen(App):
    TITLE = "Dashboard"
    CSS_PATH = "../tcss/layout.tcss"  # 相対パスなので注意
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield TimelineWidget(name="タイムライン", id="timeline")
        yield BotInfoWidget(name="BotInfo", id="bot_info")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
