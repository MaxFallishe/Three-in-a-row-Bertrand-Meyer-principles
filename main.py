# from console_ui import interface
#
#
# def main() -> None:
#     # инициализации логики/движка
#
#     # старт сессии
#
#     # инициализация UI интерфейса, рендер
#     interface.delme()
#
# if __name__ == '__main__':
#     main()


import curses


def draw_matrix(stdscr, matrix, command, cursor_visible):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Calculate position to center the matrix
    start_y = (height - 16) // 2
    start_x = (width - 32) // 2

    # Draw the matrix
    for y in range(8):
        for x in range(8):
            stdscr.addstr(start_y + y * 2, start_x + x * 4, f' {matrix[y][x]} ')
    # Draw the command line
    stdscr.addstr(height - 2, 0, "Command: " + command)
    # Blinking cursor
    if cursor_visible:
        stdscr.addstr(height - 2, len("Command: ") + len(command), '_')
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    matrix = [['😎 ' for _ in range(8)] for _ in range(8)]
    command = ''
    cursor_visible = True
    stdscr.timeout(500)  # Set timeout for blinking cursor

    while True:
        draw_matrix(stdscr, matrix, command, cursor_visible)
        key = stdscr.getch()

        if key == 10:  # Enter key
            if command.strip().lower() == 'exit':
                break
            command = ''
        elif key == 127 or key == curses.KEY_BACKSPACE:  # Backspace key
            command = command[:-1]
        elif key != -1:  # Any other key
            command += chr(key)

        # Toggle cursor visibility
        cursor_visible = not cursor_visible


if __name__ == "__main__":
    curses.wrapper(main)

