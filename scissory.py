'''
Created by: Jakob
Date: 19.03.2022
Name: Rock Paper Scissors Game
Programming Language: Python
'''

# Packages used in this code
import random

# Creating variables for scores
user_score = 0.0
computer_score = 0

# Creating states to choose
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type in Rock/Paper/Scissors or q for Quit : ").lower()

    # Check if the user wants to quit
    if user_input == 'q' :
        break
    # Check if the input is valid
    if(user_input not in options) :
        print('Please enter a valid input: /n')
        continue

    r = random.randint(0,2)
    # Rock = 0, Paper = 1, Scissors = 2
    computer_pick = options[r]
    print("The Computer picked ", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a draw, play again \nThe Score is You: ", user_score, "\n Computer Score:", computer_score)
        continue

    elif computer_pick == "rock" and user_input == "paper":
        user_score += 1
        print("You won, Paper packs Rock. \n The Score is \n You: ", user_score, "\nComputer Score: ", computer_score)
        continue

    elif computer_pick == "rock" and user_input == "scissors":
        computer_score += 1
        print("You lost, Rock breaks Scissors. \n The Score is \n You: ", user_score, "\nComputer Score: ", computer_score)
        continue

    elif computer_pick == "paper" and user_input == "rock":
        computer_score += 1
        print("You lost, Raper packs Rock. \n The Score is \n You: ", user_score, "\nComputer Score: ", computer_score)
        continue

    elif computer_pick == "paper" and user_input == "scissors":
        user_score += 1
        print("You won, Scissors cut Paper. \n The Score is \n You: ", user_score, "\nComputer Score: ", computer_score)
        continue

    elif computer_pick == "scissors" and user_input == "paper":
        computer_score += 1
        print("You lost,  Scissors cut Paper. \n The Score is \n You: ", user_score, "\nComputer Score: ", computer_score)
        continue

    elif computer_pick == "scissors" and user_input == "rock":
        user_score += 1
        print("You won,  Rock breaks Scissors. \n The Score is \n You: ", user_score, "\nComputer Score: ", computer_score)
        continue
print("Goodbye.")


