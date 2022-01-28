
import random
from telnetlib import theNULL
from tkinter import messagebox
from typing import List

U = input("Please choose one of : 'rock' , 'paper' or 'scissors' : ").lower()
print("USER CHOSE:", U)
possible_choices =  ["rock","paper","scissors"]
# VALIDATIONS
if U not in possible_choices:
    print("Error: Please choose 'rock, 'paper' or 'scissors' only.")
    exit()

# COMPUTER CHOICE
Computer_Choice = random.choice(possible_choices)
print ( "The computer chose", Computer_Choice)

# DETERMINE THE WINNER
if U == Computer_Choice:  
    print("It's a tie")

if U == "rock" & Computer_Choice =="paper":
    print("Computer wins!")

if U == "paper" & Computer_Choice=="rock":
    print("You win!")

if U == "rock" & Computer_Choice =="scissors":
    print("You win!")

if U == "scissors" & Computer_Choice =="rock":
    print("Computer wins!")

if U == "paper" & Computer_Choice=="scissors":
    print("Computer wins!")

if U == "scissors" & Computer_Choice=="paper":
    print("You win!")


# FINAL RESULTS 
