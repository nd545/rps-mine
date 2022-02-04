def determine_winner(choice_1, choice_2):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
 # todo: write some Python here to determine the winner
    if choice_1 == choice_2:
        result = None

    if choice_1 == "rock" and choice_2 == "paper":
        result = "paper"

    if choice_1 == "paper" and choice_2 == "rock":
        result = "paper"

    if choice_1 == "rock" and choice_2 == "scissors":
        result = "rock"

    if choice_1 == "scissors" and choice_2 == "rock":
        result = "rock"

    if choice_1 == "paper" and choice_2 == "scissors":
        result = "scissors"

    if choice_1 == "scissors" and choice_2 == "paper":
        result = "scissors"

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
        final_message = "Oof - it's a tie!"

    if U == "rock" and Computer_Choice == "paper":
        final_message = "Oh no, computer wins!"

    if U == "paper" and Computer_Choice == "rock":
        final_message = "You win, yay!"

    if U == "rock" and Computer_Choice == "scissors":
        final_message = "You win, yay!"

    if U == "scissors" and Computer_Choice == "rock":
        final_message = "Oh no, computer wins!"

    if U == "paper" and Computer_Choice == "scissors":
        final_message = "Oh no, computer wins!"

    if U == "scissors" and Computer_Choice == "paper":
        final_message = "You win, yay!"

    determine_winner(U, Computer_Choice)

    # FINAL RESULTS
    print("User chose:", U, "\n"  "Computer Chose:", Computer_Choice)
    print("-----------------------")
    print(final_message)
    print("--------------------------------")
    print("Thanks for playing, come again!")
