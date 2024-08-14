import time
from abc import ABC, abstractmethod, ABCMeta
from typing import TypeVar

from core.field import BaseRectangleField
from core.field_observer import GameFieldObserver
from core.field_physics import GameFieldPhysics
from custom_data_structures.custom_types import PositiveInt, char
from custom_data_structures.custom_typevars import CovariantGameSessionType, CovariantTwoDimensialArrayElementType
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class CombinedMeta(ABCMeta):
    def __new__(cls, name, bases, dct):
        klass = super().__new__(cls, name, bases, dct)

        # Identify methods marked for observation
        methods_to_observe = [
            name for name, method in dct.items()
            if callable(method) and getattr(method, '_mark_for_observation', False)
        ]
        klass._methods_to_observe = methods_to_observe
        return klass

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        for method_name in cls._methods_to_observe:
            method = getattr(instance, method_name)
            observer = instance.game_observer
            decorated_method = observer.observe(method)
            setattr(instance, method_name, decorated_method)
        return instance


def mark_for_observation(func):
    func._mark_for_observation = True
    return func


class AbstractGameEngine(ABC):
    def __init__(self, game_session: CovariantGameSessionType, game_observer: GameFieldObserver, game_field: BaseRectangleField):
        self._game_session: CovariantGameSessionType = game_session
        self.game_observer = game_observer
        self.game_field = game_field
        self.game_physics: GameFieldPhysics

    @abstractmethod
    def start_game_session(self):
        ...


class GameEngine(AbstractGameEngine, metaclass=CombinedMeta):
    def __init__(self, game_session: CovariantGameSessionType, game_observer: GameFieldObserver, game_field: BaseRectangleField):
        super().__init__(game_session=game_session, game_observer=game_observer, game_field=game_field)
        self.game_physics = GameFieldPhysics(game_field=self.game_field)

    def start_game_session(self):
        ...

    @mark_for_observation
    def shard_castling(self, element1: tuple[PositiveInt, PositiveInt], element2: tuple[PositiveInt, PositiveInt]) -> None:
        a = self.game_field.field.get(element1[0], element1[1])
        b = self.game_field.field.get(element2[0], element2[1])
        self.game_field.field.put(element1[0], element1[1], b)
        self.game_field.field.put(element2[0], element2[1], a)


    def performer_field_line_pattern(self, elements: CovariantTwoDimensialArrayElementType):
        # Should be done with effect
        for i in elements:  # TODO should change type of object, not jut value
            i.value = '*'

        # time.sleep(5)

        self.game_physics.apply_physics_to_field()


