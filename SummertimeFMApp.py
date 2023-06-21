from textual import events, on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static
from textual.reactive import var

from LocalMusicProvider import LocalMusicProvider


class SummertimeFMApp(App):
    """Setting up Terminal UI for SummertimeFM"""

    songtitle = var("Song Title")

    def compose(self) -> ComposeResult:
        self.music_provider = LocalMusicProvider("/Users/jaredrosen/Desktop/Desktop/test_music")
        with Container(id="summertimefm"):
            yield Button("Play", id="play", variant="primary")
            yield Button("Pause", id="pause", variant="warning")
            yield Static(id="songtitle")

    @on(Button.Pressed, "#play")
    def play_pressed(self):
        # if self.music_provider.is_playing():
        #     return
        self.music_provider.play()
        self.songtitle = self.music_provider.current_song

    @on(Button.Pressed, "#pause")
    def pause_pressed(self):
        if not self.music_provider.is_playing():
            return
        self.music_provider.pause()

    def watch_songtitle(self, value: str) -> None:
        self.query_one("#songtitle", Static).update(value)


if __name__ == '__main__':
    SummertimeFMApp().run()
