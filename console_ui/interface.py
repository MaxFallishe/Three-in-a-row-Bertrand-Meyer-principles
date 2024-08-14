import curses
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable, override, overload
import re

from core.field import BaseRectangleField
from turn_mechanics.game_engine import AbstractGameEngine

CovariantGameEngineType = TypeVar('CovariantGameEngineType', covariant=True, bound=AbstractGameEngine)


# TODO add new drawer of field with messages about entered commands status
# TODO help
# TODO error message
class AbstractGameUI(ABC):
    @abstractmethod
    def __init__(self, game_engine: CovariantGameEngineType):
        self.game_engine = game_engine
        self.is_ui_active = False

    @abstractmethod
    def start(self) -> None:
        """Starts the process of displaying the game's visual."""
        ...


class ConsoleGameUI(AbstractGameUI):
    def __init__(self, game_engine: CovariantGameEngineType):
        super().__init__(game_engine)
        self._stdscr = curses.initscr()
        self.height, self.width = 0, 0
        self.command = ''
        self._points = '000000'
        self._turn_num = 1
        self._message_bar_text = "Game was started try use `move` command"
        self.cursor_visible = True
        self.matrix = self.game_engine.game_field  # error when h>=10 or w>=10, implement validation

    @override
    def start(self) -> None:
        curses.curs_set(0)
        self._stdscr.timeout(500)
        self.is_ui_active = True

        curses.noecho()
        curses.cbreak()
        self._stdscr.keypad(True)

        self._screen_updater()

    def _screen_updater(self) -> None:
        while True:
            if not self.is_ui_active:
                curses.echo()
                curses.nocbreak()
                self._stdscr.keypad(False)
                curses.endwin()
                break

            self.height, self.width = self._stdscr.getmaxyx()
            self._stdscr.clear()
            self._draw_game_field()
            self._draw_game_command_line()
            self._draw_message_bar()
            self._draw_game_points()
            self._draw_game_turn()
            self._read_game_command_line()

    def _draw_game_field(self) -> None:  # TODO refactor
        start_y = (self.height - self.matrix.field.height*2) // 2
        start_x = (self.width - self.matrix.field.width*3) // 2
        for y in range(self.matrix.field.height):
            for x in range(self.matrix.field.width):
                self._stdscr.addstr(start_y + y * 2, start_x + x * 4, f' {self.matrix.field.get(y, x).value} ')

    def _draw_game_command_line(self) -> None:  # TODO refactor
        self._stdscr.addstr(self.height - 4, 0, "Command: " + self.command)
        if self.cursor_visible:
            self._stdscr.addstr(self.height - 4, len("Command: ") + len(self.command), '_')
        self._stdscr.refresh()
        self.cursor_visible = not self.cursor_visible

    def _draw_message_bar(self) -> None:
        message_bar_text = f'Message bar: {self._message_bar_text}'
        self._stdscr.addstr(self.height - 2, 0, message_bar_text)

    def _draw_game_points(self) -> None:  # TODO Refactor
        points_text = f'Points: {self._points}'
        start_x = self.width - len(points_text) - 1
        self._stdscr.addstr(0, start_x, points_text)

    def _draw_game_turn(self) -> None:  # Refactor
        points_text = f'Turn № {self._turn_num}'
        start_x = self.width - len(points_text) - 30
        self._stdscr.addstr(0, start_x, points_text)

    def _read_game_command_line(self) -> None:  # TODO Refactor
        key = self._stdscr.getch()
        if key == 10:
            if self.command.strip().lower() == 'exit':
                self.is_ui_active = False
            if 'move' in self.command.strip().lower():
                pattern = r"move (\d+)\.(\d+) (\d+)\.(\d+)"
                match = re.match(pattern, self.command.strip().lower())
                if not match:
                    pass
                num1 = int(match.group(1))-1
                num2 = int(match.group(2))
                num3 = int(match.group(3))-1
                num4 = int(match.group(4))

                self.game_engine.shard_castling((num1, num2), (num3, num4))
                # self.matrix = self.game_engine.game_field

                # FIXME add validation
                self._message_bar_text = "Success move!"
                self._turn_num += 1

            self.command = ''
        elif key == curses.KEY_BACKSPACE:
            self.command = self.command[:-1]
        elif key != -1:
            self.command += chr(key)
