from typing import TypeVar

from custom_data_structures.two_dimensional_elements import AbstractTwoDimensialArrayElement
from turn_mechanics.game_session import AbstractGameSession

CovariantTwoDimensialArrayElementType = TypeVar('CovariantTwoDimensialArrayElementType', covariant=True, bound=AbstractTwoDimensialArrayElement)
CovariantGameSessionType = TypeVar('CovariantGameSessionType', covariant=True, bound=AbstractGameSession)
