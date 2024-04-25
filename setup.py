# setup.py

import random


def load_words(filename):
    with open(filename, "r") as file:
        words = file.readlines()
    return [word.strip() for word in words]

def select_difficulty():
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return ["easy", "medium", "hard"][int(choice) - 1]
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def select_passage(words, difficulty):
    passage_length = {"easy": 20, "medium": 30, "hard": 40}[difficulty]
    passage = random.sample(words, passage_length)
    return " ".join(passage)

