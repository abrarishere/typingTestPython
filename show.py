import curses
import time

import ui


def get_input(screen):
    curses.echo()
    curses.curs_set(1)
    user_input = screen.getstr().decode('utf-8')
    curses.noecho()
    curses.curs_set(0)
    return user_input


def display_progress(username, passage):
    screen = ui.init_screen()
    try:
        cursor_pos = 0
        correct_words = 0
        total_words = len(passage.split())
        start_time = time.time()

        while cursor_pos < len(passage.split()):
            ui.display_passage(screen, passage, cursor_pos, "")  # Provide empty user_input
            user_input = get_input(screen)
            if cursor_pos < len(passage.split()) and user_input == passage.split()[cursor_pos]:
                cursor_pos += 1
                correct_words += 1

        elapsed_time = time.time() - start_time
        wpm = calculate_wpm(correct_words, elapsed_time)
        accuracy = calculate_accuracy(correct_words, total_words)
        return wpm, accuracy

    finally:
        ui.close_screen(screen)


def calculate_wpm(correct_words, total_time):
    minutes = total_time / 60
    if minutes > 0:
        return int(correct_words / minutes)
    else:
        return 0


def calculate_accuracy(correct_words, total_words):
    return (correct_words / total_words) * 100 if total_words > 0 else 0
