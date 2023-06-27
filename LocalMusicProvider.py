import pygame

from MusicProvider import MusicProvider

from pathlib import Path
from pygame.mixer import music
from random import shuffle


class LocalMusicProvider(MusicProvider):
    """Music provider for local storage music"""

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.current_song = ""
        self.is_paused = False
        pygame.mixer.init()

    def play(self) -> None:
        if self.is_paused:
            music.unpause()
            self.is_paused = False
            return
        shuffled_list = self.get_all_songs()
        shuffle(shuffled_list)

        music.set_volume(1.0)
        music.load(shuffled_list[0])
        self.current_song = shuffled_list[0].name.rstrip(".mp3")
        self.is_paused = False
        music.play()


    def pause(self):
        music.pause()
        self.is_paused = True

    def rewind(self) -> None:
        pass

    def skip(self) -> None:
        pass

    def get_all_songs(self) -> list[Path]:
        """Gets list of song filenames from filepath attribute"""
        return [song for song in self.filepath.glob("*.mp3")]

    def is_playing(self) -> bool:
        return music.get_busy()

# if __name__ == "__main__":
#     provider = LocalMusicProvider("/Users/jaredrosen/Desktop/Desktop/test_music")
#     provider.play()