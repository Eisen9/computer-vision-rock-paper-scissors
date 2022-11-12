# This code needs to randomly choose an option
# (rock, paper, or scissors) and then ask the user for an input.
import random
def get_computer_choice(): 
    '''
    randomly picks an option between "Rock", "Paper", and "Scissors"
    and returns the choice
    '''
    return random.choice(["Rock", "Paper", "Scissors"]).capitalize()

def get_user_choice():
    '''
    asks the user for an input and returns it
    '''
    return input("Rock, Paper, or Scissors? ").capitalize()

def get_winner(computer_choice, user_choice):
    '''
    This function decides who the winner is (user or computer),
    based on their selected choices using the classical rules of 
    Rock, Paper, Scissors.

    Parameters:
        @param computer_choice: the random choice of the computer
        @param user_choice: the selected choice of the user
    '''
    if computer_choice == "Rock":
        if user_choice == "Rock":
            print("It is a tie!")
        elif user_choice == "Paper":
            print("You won!")
        elif user_choice == "Scissors":
            print("You lost")
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            print("You lost")
        elif user_choice == "Paper":
            print("It is a tie!")
        elif user_choice == "Scissors":
            print("You won!")
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You won")
        elif user_choice == "Paper":
            print("You lost!")
        elif user_choice == "Scissors":
            print("It is a tie!")

# Play the game
def play():
    '''
    This function plays the game of RPS by:
    assigning the get_computer_choice and the get_user_choice functions to
    variables then passing these two variables as arguments for the 
    get_winner function.
    '''
    print("Welcome to Rock-Paper-Scissors!")
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
    print("The computer chose", computer_choice)
    print("You chose", user_choice)
    print("Thanks for playing!")

print(play())


