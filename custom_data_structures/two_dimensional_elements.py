from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from custom_data_structures.custom_typevars import CovariantTwoDimensialArrayElementType
    from custom_data_structures.two_dimensional_array import TwoDimensialCharArray

from custom_data_structures.custom_types import PositiveInt, CharStr
from abc import ABC, abstractmethod
from typing import Any


class AbstractTwoDimensialArrayElement(ABC):
    # TODO TwoDimensialCharArray create TypeVar with abstract class for two_dimensional_array
    def __init__(self, two_dimensional_array: TwoDimensialCharArray,
                 value: Any,
                 height_coord: PositiveInt,
                 width_coord: PositiveInt):
        self.two_dimensial_array = two_dimensional_array  # make it again private _etc
        self._value = value
        self._height_coord = height_coord
        self._width_coord = width_coord

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def height_coord(self):
        return self._height_coord

    @height_coord.setter
    def height_coord(self, value):
        self._height_coord = value

    @property
    def width_coord(self):
        return self._width_coord

    @width_coord.setter
    def width_coord(self, value):
        self._width_coord = value


    @property
    @abstractmethod
    def right_element(self) -> CovariantTwoDimensialArrayElementType:
        ...

    @property
    @abstractmethod
    def left_element(self) -> CovariantTwoDimensialArrayElementType:
        ...

    @property
    @abstractmethod
    def up_element(self) -> CovariantTwoDimensialArrayElementType:
        ...

    @property
    @abstractmethod
    def down_element(self) -> CovariantTwoDimensialArrayElementType:
        ...


class TwoDimensialArrayElement(AbstractTwoDimensialArrayElement):
    def __init__(self, two_dimensional_array: TwoDimensialCharArray,
                 value: CharStr | None,
                 height_coord: PositiveInt,
                 width_coord: PositiveInt):
        super().__init__(two_dimensional_array=two_dimensional_array,
                         height_coord=height_coord,
                         width_coord=width_coord,
                         value=value)

    @property
    def right_element(self):
        return self.two_dimensial_array.get(self.height_coord, self.width_coord + 1)

    @property
    def left_element(self):
        return self.two_dimensial_array.get(self.height_coord, self.width_coord - 1)

    @property
    def up_element(self):
        return self.two_dimensial_array.get(self.height_coord + 1, self.width_coord)

    @property
    def down_element(self):
        return self.two_dimensial_array.get(self.height_coord - 1, self.width_coord)



class TwoDimensialArrayNoneElement(TwoDimensialArrayElement):  # TODO migrate from None to custom empty type
    def __init__(self,
                 two_dimensional_array: TwoDimensialCharArray,
                 height_coord: PositiveInt,
                 width_coord: PositiveInt):
        super().__init__(two_dimensional_array=two_dimensional_array,
                         height_coord=height_coord,
                         width_coord=width_coord,
                         value=CharStr('g')
                         )
