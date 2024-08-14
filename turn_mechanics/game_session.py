from abc import ABC, abstractmethod
from typing import TypeVar

from turn_mechanics.game_turn import AbstractGameTurn

CovariantGameTurnType = TypeVar('CovariantGameTurnType', covariant=True, bound=AbstractGameTurn)


class AbstractGameSession(ABC):
    def __init__(self, game_turn: CovariantGameTurnType):
        ...


class GameSession(AbstractGameSession):
    ...
