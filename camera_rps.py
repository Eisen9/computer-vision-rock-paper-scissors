import time
import RPS_Template
import random

def get_perdiction():
    '''
    get_prediction() finds the predicted class and the confidence level of the prediction.
    It returns the predicted class and the confidence level.
    It calculates the time that has passed since the script started and prints the predicted class and the confidence level when the time has passed
    '''
    predictions = RPS_Template.prediction # predictions is a list of lists with the probabilities of each class
    predicted_class = RPS_Template.predicted_class # predicted_class is the class with the highest probability
    confidence_level = predictions[0][predicted_class] # confidence_level is the probability of the predicted_class
    start_time = time.time() # start_time is the time the script started
    while True:
        if time.time() - start_time >= 5:  # if 5 seconds have passed since the start time of the script
            print(
                f"you chose {predicted_class} with a confidence of {confidence_level}")
            break
    return predicted_class, confidence_level

computer_wins = 0
user_wins = 0
rounds = 0

while computer_wins < 3 or user_wins < 3:  # use while True: to keep playing
    if computer_wins == 3 or user_wins == 3:
        break
    else:
        if computer_wins < 3 or user_wins < 3:
            rounds += 1
            print(f"Round {rounds}")
            computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
            user_choice, confidence_level = get_perdiction()
            print(f"Computer chose {computer_choice}")
            print(
                f"User chose {user_choice} with a confidence of {confidence_level}")
            if computer_choice == user_choice:
                print("It's a tie!")
            elif computer_choice == "Rock":
                if user_choice == "Paper":
                    print("User wins!")
                    user_wins += 1
                else:
                    print("Computer wins!")
                    computer_wins = computer_wins + 1
            elif computer_choice == "Paper":
                if user_choice == "Scissors":
                    print("User wins!")
                    user_wins += 1
                else:
                    print("Computer wins!")
                    computer_wins += 1
            elif computer_choice == "Scissors":
                if user_choice == "Rock":
                    print("User wins!")
                    user_wins += 1
                else:
                    print("Computer wins!")
                    computer_wins += 1
            print(f"Computer wins: {computer_wins}")
            print(f"User wins: {user_wins}")
            print("")
