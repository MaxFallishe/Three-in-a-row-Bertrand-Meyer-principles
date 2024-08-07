from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable

from turn_mechanics.game_engine import AbstractGameEngine, GameEngine


CovariantGameEngineType = TypeVar('CovariantGameEngineType', covariant=True, bound=AbstractGameEngine)


class AbstractGameUI(ABC):
    def __init__(self, game_engine: CovariantGameEngineType):
        self.game_engine = game_engine

    @abstractmethod
    def start(self) -> None:
        """Starts the process of displaying the game's visual."""
        ...


class ConsoleGameUI(AbstractGameUI):
    def start(self) -> None:
        ...





# my_game_engine = GameEngine()
# a = ConsoleGameUI(game_engine=my_game_engine)
