import datetime
from textual.reactive import Reactive
from textual.widgets import Static

start_time = datetime.datetime.now()


class BotInfoWidget(Static):
    total_running_time = Reactive(datetime.datetime.now())
    bot_info = Reactive(f"Running time: {total_running_time}")

    def on_mount(self):
        self.update_total_running_timer = self.set_interval(1 / 60, self.update_total_running_time)
        self.update_total_running_timer.resume()

    def update_total_running_time(self):
        self.total_running_time = datetime.datetime.now() - start_time
        self.bot_info = f"Running time: {self.total_running_time}"

    def watch_total_running_time(self, value):
        self.update(f"Running time: {value}")
