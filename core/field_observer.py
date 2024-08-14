from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from turn_mechanics.game_engine import GameEngine

from core.field import BaseRectangleField
import functools

import logging

from custom_data_structures.custom_types import posint
from custom_data_structures.custom_typevars import CovariantTwoDimensialArrayElementType


# TODO put in personal logging script
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class GameFieldObserver:
    def __init__(self, game_field: BaseRectangleField):
        self.game_field = game_field
        self.counter = 0
        self.game_engine: GameEngine

    def observe(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # All watchers should be in this wrapper, all performers should be called from needed watchers
            self._watcher_field_line_pattern()


            logging.warning(f'Succes_observe! {self.counter} function is observed')
            self.counter += 1
            return result
        return wrapper

    def _watcher_field_line_pattern(self) -> set[CovariantTwoDimensialArrayElementType]:
        shards_in_lines_pattern = set()
        for i in range(self.game_field.field.height):
            for j in range(self.game_field.field.width):
                element = self.game_field.field.get(posint(i), posint(j))

                if element in shards_in_lines_pattern:
                    continue
                shards_in_lines_pattern |= self._get_same_shards_if_exist_inarow(element)
                if element in shards_in_lines_pattern:
                    continue
                shards_in_lines_pattern |= self._get_same_shards_if_exist_inacolumn(element)

        self.game_engine.performer_field_line_pattern(elements=shards_in_lines_pattern)


    @staticmethod
    def _get_same_shards_if_exist_inarow(element) -> set[CovariantTwoDimensialArrayElementType]:
        """Returns a sequence of shards if there are three or more shards in a row"""
        shards_in_row = set()
        shards_in_row.add(element)

        try:  # TODO possibly can do without try except
            while element.value == element.right_element.value:
                shards_in_row.add(element.right_element)
                element = element.right_element
        except Exception as e:
            pass  # TODO log it

        if len(shards_in_row) >= 3:
            return shards_in_row
        return set()

    @staticmethod
    def _get_same_shards_if_exist_inacolumn(element) -> set[CovariantTwoDimensialArrayElementType]:
        """Returns a sequence of shards if there are three or more shards in a column"""
        shards_in_column = set()
        shards_in_column.add(element)

        try:  # TODO possibly can do without try except
            while element.value == element.down_element.value:
                shards_in_column.add(element.down_element)
                element = element.down_element
        except Exception as e:
            pass  # TODO log it

        if len(shards_in_column) >= 3:
            return shards_in_column
        return set()



