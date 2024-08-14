import random
from typing import Any

from custom_data_structures.custom_types import posint, char
from custom_data_structures.two_dimensional_array import TwoDimensialCharArray
from custom_data_structures.two_dimensional_elements import TwoDimensialArrayElement


class BaseRectangleField:
    def __init__(self, height: posint, width: posint):
        self.field = TwoDimensialCharArray(height + 1, width + 1)
        self.width = width
        self.height = height
        self._setup_game_field()

    def _setup_game_field(self) -> None:
        # temp
        for i in range(self.width + 1):
            for j in range(self.height + 1):
                posint_i = posint(i)
                posint_j = posint(j)
                # random_shard = random.choice(["🌕", "🌏", "🪐", "🌝", "🌞"])  # TODO refactor
                random_shard = chr(i*77+j*92)
                if posint_i == 1 and posint_j == 3: random_shard = "🌏"
                if posint_i == 1 and posint_j == 4: random_shard = "🌏"
                if posint_i == 1 and posint_j == 5: random_shard = "🌏"
                if posint_i == 3 and posint_j == 4: random_shard = "🌏"
                if posint_i == 3 and posint_j == 5: random_shard = "🌏"
                if posint_i == 3 and posint_j == 6: random_shard = "🌏"

                element = TwoDimensialArrayElement(self.field, random_shard, posint_j, posint_i)  # TODO refactor - heigh and width is calculated in process of paste
                self.field.put(posint_j, posint_i, element)

        self.field.put(self.height, posint(0), TwoDimensialArrayElement(self.field, " ", self.height, posint(0)))

        for i in range(1, self.width + 1):
            posint_i = posint(i)
            self.field.put(self.height, posint_i, TwoDimensialArrayElement(self.field, char(i), self.height, posint_i))
        for i in range(0, self.height):
            posint_i = posint(i)
            self.field.put(posint_i, posint(0), TwoDimensialArrayElement(self.field, char(i + 1), posint_i, posint(0)))

