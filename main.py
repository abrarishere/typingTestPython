# main.py

import intro
import leaderboard
import results
import setup
import show


def main():
    intro.display_intro()
    username = input("Enter your username: ")
    choice = input("\nWould you like to view the leaderboard? (yes/no): ").lower()
    if choice == "yes":
        leaderboard.display_leaderboard()
    words = setup.load_words("words.txt")
    difficulty = setup.select_difficulty()
    passage = setup.select_passage(words, difficulty)
    formatted_passage = format_paragraph(passage)
    wpm, accuracy = show.display_progress(username, formatted_passage)
    results.display_results(wpm, accuracy)
    leaderboard.update_leaderboard(username, wpm, accuracy)
    leaderboard.display_leaderboard()

def format_paragraph(passage):
    lines = passage.split('\n')
    max_length = max(len(line) for line in lines)
    formatted_lines = [line.center(max_length) for line in lines]
    return '\n'.join(formatted_lines)

if __name__ == "__main__":
    main()
