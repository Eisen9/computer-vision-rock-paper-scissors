import random
def get_computer_choice(): 
    '''
    randomly picks an option between "Rock", "Paper", and "Scissors"
    and returns the choice
    '''
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def get_user_choice():
    '''
    asks the user for an input and returns it
    '''
    user_input = input("Enter your choice of 'Rock', 'Paper', or 'Scissors' ")
    return user_input

def get_winner(computer_choice, user_choice):
    '''
    This function decides who the winner is (user or computer),
    based on their selected choices using the classical rules of 
    Rock, Paper, Scissors.

    Parameters:
        @param computer_choice: the random choice of the computer
        @param user_choice: the selected choice of the user
    '''
    if computer_choice == user_choice:
        return 'Tie'
    elif computer_choice == 'Rock':
        if user_choice == 'Paper':
            return 'User'
        else:
            return 'Computer'
    elif computer_choice == 'Paper':
        if user_choice == 'Scissors':
            return 'User'
        else:
            return 'Computer'
    elif computer_choice == 'Scissors':
        if user_choice == 'Rock':
            return 'User'
        else:
            return 'Computer'

def main():
    '''
    This is the main function that will be called when the program is run.
    '''
    # Get the computer's choice
    computer_choice = get_computer_choice()
    # Get the user's choice
    user_choice = get_user_choice()
    # Get the winner
    winner = get_winner(computer_choice, user_choice)
    # Print the winner
    print('The winner is: {}'.format(winner))
    # Print the computer's choice
    print('The computer chose: {}'.format(computer_choice))
    # Print the user's choice
    print('The user chose: {}'.format(user_choice))
    print('Thanks for playing!')

if __name__ == '__main__':
    main()
