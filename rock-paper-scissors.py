import random

# ASCII Art
paper =  """ __  __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |           | |             
|_|           |_|   
"""

rock = """                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\\
"""

scissors = """ ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
"""

# CHOICES
ascii_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

options = ["rock", "paper", "scissors"]

# USER INPUT
human_choice = input("rock, paper, or scissors? ").lower()
if human_choice not in options:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    exit()

# BOT CHOICE
bot_choice = random.choice(options)

# SHOW CHOICES
print(f"\nYou chose:\n{ascii_art[human_choice]}")
print(f"\nComputer chose:\n{ascii_art[bot_choice]}")

# GAME LOGIC
if human_choice == bot_choice:
    result = "draw"
elif (
    (human_choice == "rock" and bot_choice == "scissors") or
    (human_choice == "paper" and bot_choice == "rock") or
    (human_choice == "scissors" and bot_choice == "paper")
):
    result = "win"
else:
    result = "lose"

# RESULT
if result == "draw":
    print("\nDRAW!")
elif result == "win":
    print("\nYOU WIN!")
else:
    print("\nYOU LOST!")
