# leaderboard.py

def update_leaderboard(username, wpm, accuracy):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{username},{wpm},{accuracy}\n")

def display_leaderboard():
    print("\n--- Leaderboard ---")
    print("Username   |   WPM   |   Accuracy")
    with open("leaderboard.txt", "r") as file:
        lines = file.readlines()
        lines.sort(key=lambda line: float(line.split(",")[1]), reverse=True)
        for line in lines:
            username, wpm, accuracy = line.strip().split(",")
            print(f"{username.ljust(10)} | {wpm.ljust(7)} | {accuracy}%")

