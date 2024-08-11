from typing import Any

from custom_data_structures.custom_types import posint, char, TwoDimensialArrayNone


class TwoDimensialCharArray:
    def __init__(self, height: posint, width: posint):
        self._height = height
        self._width = width
        self._matrix: list[list[Any]] = [[TwoDimensialArrayNone() for _ in range(width)] for _ in range(height)]

    def get(self, height: posint, width: posint) -> Any:
        if height > self._height or width > self._width:
            raise ValueError('Values cannot be bigger than TwoDimensialArray height or width')
        return self._matrix[height][width]

    def put(self, height: posint, width: posint, value: Any):  # replace Any back on None
        if height > self._height or width > self._width:
            raise ValueError('Values cannot be bigger than TwoDimensialArray height or width')
        self._matrix[height][width] = value

    @property
    def height(self) -> posint:
        return self._height

    @property
    def width(self) -> posint:
        return self._width

