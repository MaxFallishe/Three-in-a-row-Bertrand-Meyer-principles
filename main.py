from console_ui.interface import ConsoleGameUI
from core.field import BaseRectangleField
from core.field_observer import GameFieldObserver
from custom_data_structures.custom_types import posint
from turn_mechanics.game_engine import GameEngine
from turn_mechanics.game_session import GameSession
from turn_mechanics.game_turn import GameTurn


def main() -> None:
    # инициализации логики/движка
    # старт сессии  # TODO refactor
    game_field = BaseRectangleField(posint(8), posint(8))
    game_observer = GameFieldObserver(game_field=game_field)
    my_game_engine = GameEngine(game_session=GameSession(GameTurn()), game_observer=game_observer, game_field=game_field)
    game_observer.game_engine = my_game_engine  # TODO kinda want to do this withother options

    # инициализация UI интерфейса, рендер
    game_ui = ConsoleGameUI(game_engine=my_game_engine)
    game_ui.start()


if __name__ == '__main__':
    main()

