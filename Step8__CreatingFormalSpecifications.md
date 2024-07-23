# The essence of the document
A class that partially implements an Abstract Data Type is called a behavior class. Such classes play an important 
role in design by defining behavior specific to a certain group, a set of variants of an Abstract Data Type. A behavior
class captures the general behavior of this group, and its specific variants are embodied in descendants. By itself, 
a behavior class can occur in a variety of analysis classes, design classes, and implementation classes.

Partially implemented classes are also very useful in the first steps of design. In fact, we are starting to gradually 
specify our working system, our architecture, until we move on to full implementation. Ideologically, this approach can 
be partially compared with the top-down approach in the sense that we first start with a high-level description, and 
then detail it. Only in the case of the classic incorrect "top-down" we immediately write code, active logic, not 
designing the correct system as a whole, but simply randomly implementing individual step-by-step scenarios.

Of course, this approach is also strategically oriented towards implementation (only in a slightly different way), 
since we write the system specification essentially simply through the relationships between classes, taking into 
account pre- and post-conditions. The classification of entities in the system is implemented by inheritance, and the 
semantics of properties other than those explicitly set by class attributes are set by pre- and post-conditions. 
This is actually a big plus, because many design techniques offer too abstract, too vague ways to describe the system 
(for example, various graphical notations), which are then challenging to translate into code. We use a single 
formal language (Abstract Data Type specifications) for both design and programming, and the transition from design to 
implementation is very smooth due to the active use of behavior classes.
# Formal Specification of Abstract Data Types

```python
from queue import LifoQueue


class AbstractShard:
    def __init__(self):
        self.skin: str = ...  # some single character
        self.onclick_effect: AbstractFieldEffect = ...  # the effect that will be applied after clicking on the shard (if it is intended)

    # postcondition: The shard applies a certain effect to the playing field
    def activate(self) -> None:
        pass


class AbstractFieldEffect:
    def __init__(self):
        ...

    # precondition: The effect can be correctly applied to the provided playing field (the is_effect_application_possibility method returned True)
    # postcondition: The effect is applied to the playing field and the shards inside it
    def apply(self, game_field: 'AbstractGameField'):
        ...

    def _is_effect_application_possibility(self, game_field) -> bool:
        ...

    # postcondition: the parameters available for a specific type of effect have been changed
    def setup_effect_parameters(self) -> None:
        # raise/print warning if something is mess up
        ...


class ShardsCastlingEffect(AbstractFieldEffect):
    ...


class ShardsRemoveEffect(AbstractFieldEffect):
    ...


class AbstractGameField:
    def __init__(self):
        ...


class GameTurn:
    ...


class GameInterface:
    def __init__(self):
        ...

    # postcondition: Display interface with actual information
    def draw(self):
        ...


class GameSession:
    def __init__(self):
        self.game_turns: LifoQueue[GameTurn] = ...
        self.game_field: AbstractGameField = ...
        self.game_interface: GameInterface = ...

    # precondition: The game session not in progress
    # postcondition: Game session is started
    def start(self) -> None:
        ...

    # precondition: The game session is in progress
    # postcondition: Game session is restarted
    def restart(self) -> None:
        ...

    # precondition: The game session is in progress
    # postcondition: Game session is ended
    def end(self) -> None:
        ...

    def go_back_turn(self) -> None:
        ...
```
