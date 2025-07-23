import random

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
|_|  \___/ \___|_|\_\""""


scissors = """ ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/"""

# VARIABLES
results = ["paper", "rock", "scissors"];
# ---------------

# GAME CHOICES
human_choice = input("rock, paper, or scissors")
human_choice = human_choice.lower()

computer_choice = random.randint(0,2);
bot_result = results[computer_choice];


# OUTPUT
print(f"You chose:{human_choice}")
print(f"The computer chose:{bot_result}")

# Game Logic
You_lose = False
#-------

if (human_choice == "paper" and bot_result == "scissors"):
    You_lose = True
    print(paper)
    print(scissors)
elif (human_choice == "rock" and bot_result == "paper"):
    You_lose = True
    print(rock)
    print(paper)
elif (human_choice == "scissors" and bot_result == "rock"):
    You_lose = True
    print(scissors)
    print(rock)
elif (human_choice == "paper" and bot_result == "rock"):
    You_lose = False
    print(paper)
    print(rock)
elif (human_choice == "rock" and bot_result == "scissors"):
    You_lose = False
    print(paper)
    print(scissors)
elif (human_choice == "scissors" and bot_result == "paper"):
    You_lose = False
    print(scissors)
    print(paper)
elif (human_choice == "paper" and bot_result == "paper"):
    You_lose = "Draw"
    print(paper)
    print(paper)
elif (human_choice == "rock" and bot_result == "rock"):
    You_lose = "Draw"
    print(rock)
    print(rock)
elif (human_choice == "scissors" and bot_result == "scissors"):
    You_lose = "Draw"
    print(scissors)
    print(scissors)
else:
    You_lose = True

# RESULT
if (You_lose == True):
    print("\nYOU LOST!")
elif (You_lose == "Draw"):
    print("\nDRAW!")
else:
    print("\nYOU WIN!");


    