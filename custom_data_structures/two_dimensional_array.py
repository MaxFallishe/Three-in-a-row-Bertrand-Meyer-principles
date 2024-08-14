from __future__ import annotations
from typing import TYPE_CHECKING

from custom_data_structures.custom_types import posint
from custom_data_structures.two_dimensional_elements import TwoDimensialArrayNoneElement, TwoDimensialArrayElement

if TYPE_CHECKING:
    from custom_data_structures.custom_typevars import CovariantTwoDimensialArrayElementType

from typing import Any


class TwoDimensialCharArray:
    def __init__(self, height: posint, width: posint):
        self._height = height
        self._width = width
        self.matrix: list[list[CovariantTwoDimensialArrayElementType]] = self._init_matrix() # Maybe matrix should be private # FIXME

    def get(self, height: posint, width: posint) -> CovariantTwoDimensialArrayElementType:
        if height > self._height or width > self._width:
            raise ValueError('Values cannot be bigger than TwoDimensialArray height or width')
        return self.matrix[height][width]

    def put(self, height: posint, width: posint, value: TwoDimensialArrayElement):
        value.height_coord, value.width_coord = height, width
        if height > self._height or width > self._width:
            raise ValueError('Values cannot be bigger than TwoDimensialArray height or width')
        self.matrix[height][width] = value

    def _init_matrix(self) -> list[list[CovariantTwoDimensialArrayElementType]]:
        matrix = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                element = TwoDimensialArrayNoneElement(self, posint(i), posint(j))
                row.append(element)
            matrix.append(row)

        return matrix

    @property
    def height(self) -> posint:
        return self._height

    @property
    def width(self) -> posint:
        return self._width

    def __str__(self):  # TODO make better
        str_representation = ""
        for i in self.matrix:
            for j in i:
                str_representation += f"{j.value} "
            str_representation += "\n"
        return str_representation
