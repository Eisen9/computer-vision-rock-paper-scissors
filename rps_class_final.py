import time
import random
import cv2
from keras.models import load_model
import numpy as np

class RPS:
    '''
    RPS game class that allows the user to play rock, paper, scissors against the computer

    Attributes:
        computer_wins (int): The number of times the computer has won
        user_wins (int): The number of times the user has won
        rounds (int): The number of rounds played
        predictions (list): The list of predictions
        predicted_class (int): The predicted class
        confidence_level (float): The confidence level of the prediction
        start_time (float): The start time of the game
        computer_choice (str): The computer's choice
        user_choice (str): The user's choice

    Methods:
        get_prediction: Gets the prediction from the model
        get_computer_choice: Gets the computer's choice
        get_user_choice: Gets the user's choice
        get_confidence_level: Gets the confidence level of the prediction
        get_winner: Gets the winner of the round
        play: Plays the game
        
    '''
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.rounds = 0
        self.predictions = None
        self.predicted_class = None
        self.confidence_level = None
        self.start_time = None
        self.computer_choice = None
        self.user_choice = None

    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0) 
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.start_time = time.time()
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            # set verbose to 0 if you want to slience print
            # prediction = model.predict(data, verbose=0) # delete verbose to retrieve to origianal state
            self.prediction = model.predict(data)
            # Notice that the prediction is a numpy array with one row and four columns. So first, you need to access the first row, and then get the index of the highest value in the row
            self.predicted_class = np.argmax(self.prediction[0]) # Get the index of the highest value in the row (we only have one row)
            print(f"Predicted class is: {self.predicted_class}") 
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(self.prediction)
            # set the end time
            end_time = time.time()
            # set the time difference
            time_difference = end_time - self.start_time
            # if the time difference is greater than 5 seconds
            if time_difference > 5:
                # break the loop
                break 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    def get_computer_choice(self):
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])

    def get_user_choice(self):
        if self.predicted_class == 0:
            self.user_choice = 'rock'
        elif self.predicted_class == 1:
            self.user_choice = 'paper'
        elif self.predicted_class == 2:
            self.user_choice = 'scissors'
    
    def get_confidence_level(self):
        if self.predicted_class == 0:
            self.confidence_level = self.prediction[0][0]
        elif self.predicted_class == 1:
            self.confidence_level = self.prediction[0][1]
        elif self.predicted_class == 2:
            self.confidence_level = self.prediction[0][2]
    
    def get_winner(self):
        if self.user_choice == self.computer_choice:
            print("It's a tie!")
        elif self.user_choice == 'Rock':
            if self.computer_choice == 'Scissors':
                print("You win!")
                self.user_wins += 1
            else:
                print("You lose!")
                self.computer_wins += 1
        elif self.user_choice == 'Paper':
            if self.computer_choice == 'Rock':
                print("You win!")
                self.user_wins += 1
            else:
                print("You lose!")
                self.computer_wins += 1
        elif self.user_choice == 'Scissors':
            if self.computer_choice == 'Paper':
                print("You win!")
                self.user_wins += 1
            else:
                print("You lose!")
                self.computer_wins += 1

    def play(self):
        self.get_prediction()
        self.get_computer_choice()
        self.get_user_choice()
        self.get_confidence_level()
        self.get_winner()
        self.rounds += 1
        print(f"Computer choice: {self.computer_choice}")
        print(f"User choice: {self.user_choice}")
        print(f"Confidence level: {self.confidence_level}")
        print(f"Computer wins: {self.computer_wins}")
        print(f"User wins: {self.user_wins}")
        print(f"Rounds: {self.rounds}")

if __name__ == "__main__":
    rps = RPS()
    # The game should be repeated until either the computer or the user wins three rounds.
    while rps.computer_wins < 3 and rps.user_wins < 3:
        rps.play()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'n':
            break


