from textual import events, on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static, Header, Footer
from textual.reactive import var

from LocalMusicProvider import LocalMusicProvider


# TODO: playback controls custom widget
class PlaybackControls(Footer):
    """Widget to hold playback controls"""

    def compose(self) -> ComposeResult:
        yield Static(id="songtitle")
        yield Button("Rewind", id="rewind")
        yield Button("Play", id="play")
        yield Button("Pause", id="pause")


# TODO:
# - CSS constants?
# - combine play/pause, add rewind and skip (AND icons)
# - file tree thing for viewing file lists of songs
# - custom header? pizzazz
# - playlist(?) object -> for queueing, skipping, rewinding
#   - stack/list for queue
#   - manage queue when playing song (not shuffled list)
class SummertimeFMApp(App):
    """Setting up Terminal UI for SummertimeFM"""

    songtitle = var("Song Title")

    CSS_PATH = "home_screen.css"
    BINDINGS = [
        ("p", "play", "Play"),
        ("l", "pause", "Pause"),
        ("r", "rewind", "Rewind")
    ]

    def compose(self) -> ComposeResult:
        self.music_provider = LocalMusicProvider("/Users/jaredrosen/Desktop/Desktop/test_music")
        with Container(id="summertimefm", classes="summertimefm"):
            yield Header(show_clock=True)
            yield PlaybackControls()
            yield Footer()

    @on(Button.Pressed, "#play")
    def play_pressed(self) -> None:
        # TODO: this logic should be in MusicProvider, not here
        if self.music_provider.is_playing():
            return
        self.music_provider.play()
        self.songtitle = self.music_provider.current_song

    def action_play(self) -> None:
        self.play_pressed()

    @on(Button.Pressed, "#pause")
    def pause_pressed(self) -> None:
        # TODO: same with this guy here
        if not self.music_provider.is_playing():
            return
        self.music_provider.pause()

    def action_pause(self) -> None:
        self.pause_pressed()

    @on(Button.Pressed, "#rewind")
    def rewind_pressed(self) -> None:
        self.music_provider.rewind()

    def action_rewind(self) -> None:
        self.rewind_pressed()

    def watch_songtitle(self, value: str) -> None:
        self.query_one("#songtitle", Static).update(value)


if __name__ == '__main__':
    SummertimeFMApp().run()
