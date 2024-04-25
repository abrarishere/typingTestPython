# ui.py

import curses


def init_screen():
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # New color for error lines
    return screen

def cleanup_screen(screen):
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()

def display_passage(screen, passage, cursor_pos, user_input):
    screen.clear()
    height, width = screen.getmaxyx()
    y_offset = max(0, cursor_pos - height // 2)

    for i, word in enumerate(passage.split()[y_offset:y_offset + height]):
        truncated_word = word[:width - 1]
        if i == cursor_pos - y_offset:
            screen.addstr(i, width//2 - len(truncated_word)//2, truncated_word, curses.color_pair(2))
        else:
            screen.addstr(i, width//2 - len(truncated_word)//2, truncated_word, curses.color_pair(1))

    screen.addstr(height - 1, 0, f"Your input: {user_input}", curses.color_pair(1))
    screen.refresh()

def close_screen(screen):
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()
