def determine_winner(choice_1, choice_2):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
 # todo: write some Python here to determine the winner
    if choice_1 == choice_2:
        result = "Oof - it's a tie!"

    if choice_1 == "rock" and choice_2 == "paper":
        result = "Oh no, computer wins!"

    if choice_1 == "paper" and choice_2 == "rock":
        result = "You win, yay!"

    if choice_1 == "rock" and choice_2 == "scissors":
        result = "You win, yay!"

    if choice_1 == "scissors" and choice_2 == "rock":
        result = "Oh no, computer wins!"

    if choice_1 == "paper" and choice_2 == "scissors":
        result = "Oh no, computer wins!"

    if choice_1 == "scissors" and choice_2 == "paper":
        result = "You win, yay!"

        return result


if __name__ == "__main__":

    print("WELCOME TO MY ROCK PAPER SCISSORS GAME!")

    # ...

    import os
    player_name = os.getenv("PLAYER_NAME", default="Player One")
    import random
    from telnetlib import theNULL
    from tkinter import messagebox
    from typing import List

    print("Welcome to Rock, Paper, Scissors Game,", player_name, "!")
    print("------------------------------------------")

    # VARIABLE ASSIGNMENTS
    U = input("Please choose one of : 'rock' , 'paper' or 'scissors' : ").lower()
    possible_choices = ["rock", "paper", "scissors"]
    result = "outcome"

    # VALIDATIONS
    if U not in possible_choices:
        print("Sorry, please choose 'rock, 'paper' or 'scissors' only.")
        exit()

    # COMPUTER CHOICE
    Computer_Choice = random.choice(possible_choices)

    # DETERMINE THE WINNER
    if U == Computer_Choice:
        result = "Oof - it's a tie!"

    if U == "rock" and Computer_Choice == "paper":
        result = "Oh no, computer wins!"

    if U == "paper" and Computer_Choice == "rock":
        result = "You win, yay!"

    if U == "rock" and Computer_Choice == "scissors":
        result = "You win, yay!"

    if U == "scissors" and Computer_Choice == "rock":
        result = "Oh no, computer wins!"

    if U == "paper" and Computer_Choice == "scissors":
        result = "Oh no, computer wins!"

    if U == "scissors" and Computer_Choice == "paper":
        result = "You win, yay!"

    determine_winner(U, Computer_Choice)

    # FINAL RESULTS
    print("User chose:", U, "\n"  "Computer Chose:", Computer_Choice)
    print("-----------------------")
    print(result)
    print("--------------------------------")
    print("Thanks for playing, come again!")
