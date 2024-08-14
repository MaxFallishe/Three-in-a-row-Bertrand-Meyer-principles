import logging
import time

from core.field import BaseRectangleField
from custom_data_structures.custom_types import posint, char

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# FIXME .up_element and .down_element are working opposite it name
# TODO add step-by-step physics for animations
class GameFieldPhysics:
    def __init__(self, game_field):
        self.game_field: BaseRectangleField = game_field

    def _calculate_correct_shards_position(self):
        """Simple strictly horizontal force of gravity"""
        for i in range(self.game_field.field.height-2, -1, -1):
            for j in range(self.game_field.field.width-1, 0, -1):
                element = self.game_field.field.get(posint(i), posint(j))
                # logging.warning(f'element [{i, j}], {element.value}, UP_EL{element.down_element.value}')

                if i == 0:
                    continue
                if element.value != '*':  # TODO replace with type
                    continue


                logging.warning(f'element [{i, j}], {element.value}, UP_EL{element.down_element.value}')
                try:
                    most_down_hole = self.game_field.field.get(i, j)
                    while True:

                        if element.value == '*':
                            element = element.down_element
                            continue

                        element.value, most_down_hole.value = most_down_hole.value, element.value  # TODO should be up element fix it


                        if element.height_coord == 0:
                            break

                        element = element.down_element
                        most_down_hole = most_down_hole.down_element

                except Exception as e:
                    logging.warning(e)

    def apply_physics_to_field(self):
        self._calculate_correct_shards_position()

