from abc import ABC, abstractmethod


class MusicProvider(ABC):
    """
    Abstract base class for any type of music provider
    (e.g. Apple Music, Soundcloud, local storage, etc.)
    """

    @abstractmethod
    def play(self) -> None:
        """Play a song"""
        pass

    @abstractmethod
    def pause(self) -> None:
        """Pause a song"""
        pass

    @abstractmethod
    def skip(self) -> None:
        """Skips current song, and plays next one"""
        pass

    @abstractmethod
    def rewind(self) -> None:
        """Rewinds current song to beginning, or plays previous song"""
        pass
