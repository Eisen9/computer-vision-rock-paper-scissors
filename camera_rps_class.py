import time
import random
import cv2
from keras.models import load_model
import numpy as np
class RPS:
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # self.computer_wins = 0
        # self.user_wins = 0
        # self.rounds = 0
        # self.computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        self.ret, self.frame = self.cap.read()
        self.resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        self.image_np = np.array(self.resized_frame)
        self.normalized_image = (self.image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = self.normalized_image
        self.prediction = self.model.predict(self.data) # delete verbose to retrieve to origianal state
        self.predicted_class = np.argmax(self.prediction[0]) # Get the index of the highest value in the row (we only have one row)


        
    def get_perdiction(self):
        '''
        get_prediction() finds the predicted class and the confidence level of the prediction.
        It returns the predicted class and the confidence level.
        It calculates the time that has passed since the script started and prints the predicted class and the confidence level when the time has passed
        '''
        self.predictions = self.prediction
        self.predicted_class = self.predicted_class
        self.confidence_level = self.predictions[0][self.predicted_class] # confidence_level is the probability of the predicted_class
        start_time = time.time() # start_time is the time the script started
        while True:
            if time.time() - start_time >= 5:  # if 5 seconds have passed since the start time of the script
                print(
                    f"you chose {self.predicted_class} with a confidence of {self.confidence_level}")
                break
        return self.predicted_class, self.confidence_level
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
                print(f"User chose {user_choice} with a confidence of {confidence_level}")
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


# create a new instance of the RPS class
rps = RPS()
# play the game
rps.get_perdiction()



    