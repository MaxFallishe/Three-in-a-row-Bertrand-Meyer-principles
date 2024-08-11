from functools import cache


class PositiveInt(int):
    """
    ALWAYS: PositiveInt + PositiveInt = PositiveInt
    ALWAYS: PositiveInt * PositiveInt = PositiveInt
    """
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Value must be positive")
        return super().__new__(cls, value)

    def __init__(self, value):
        super().__init__()

    def __add__(self, value):
        if isinstance(value, PositiveInt):
            return posint(int(self) + int(value))
        return super().__add__(value)

    def __mul__(self, other):
        if isinstance(other, PositiveInt):
            return posint(int(self) * int(other))
        return super().__mul__(other)

    def __repr__(self):
        return f"PositiveInt({int(self)})"

    def __str__(self):
        return self.__repr__()


class CharStr(str):
    def __new__(cls, value):
        value = str(value)
        if 0 < len(value) < 2:
            return super().__new__(cls, value)
        raise ValueError("Value must br str with 1 symbol")

    def __init__(self, value):
        super().__init__()


@cache
class TwoDimensialArrayNone:
    pass


posint = PositiveInt
char = CharStr
