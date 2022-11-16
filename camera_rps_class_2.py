# we want to create a class that encasulates the RPS template and 
# camera_rps
import cv2
from keras.models import load_model
import numpy as np
import time
import random

class RPS:
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.rounds = 0

    def load_model(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        while True: 
                self.ret, self.frame = self.cap.read()
                resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                self.data[0] = normalized_image
                prediction = self.model.predict(self.data)
                # Notice that the prediction is a numpy array with one row and four columns. So first, you need to access the first row, and then get the index of the highest value in the row
                predicted_class = np.argmax(prediction[0]) # Get the index of the highest value in the row (we only have one row)
                print(f"Predicted class is: {predicted_class}") 
                cv2.imshow('frame', self.frame)
                # Press q to close the window
                print(prediction) 
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        return prediction, predicted_class
        



    def get_predictions(self):
          
            predictions = self.prediction # predictions is a list of lists with the probabilities of each class
            predicted_class = load_model.predicted_class # predicted_class is the class with the highest probability
            confidence_level = predictions[0][predicted_class] # confidence_level is the probability of the predicted_class
            start_time = time.time() # start_time is the time the script started
            while True:
                if time.time() - start_time >= 5:  # if 5 seconds have passed since the start time of the script
                    print(
                        f"you chose {predicted_class} with a confidence of {confidence_level}")
                    break
            return predicted_class, confidence_level

def play_game():
    game = RPS()
    while game.computer_wins < 3 or game.user_wins < 3:  # use while True: to keep playing
        if game.computer_wins == 3 or game.user_wins == 3:
            break
        else:
            if game.computer_wins < 3 or game.user_wins < 3:
                game.rounds += 1
                print(f"Round {game.rounds}")
                computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
                user_choice, confidence_level = game.get_predictions()
                print(f"Computer chose {computer_choice}")
                print(
                    f"User chose {user_choice} with a confidence of {confidence_level}")
                if computer_choice == user_choice:
                    print("It's a tie!")
                elif computer_choice == "Rock":
                    if user_choice == "Paper":
                        print("User wins!")
                        game.user_wins += 1
                    else:
                        print("Computer wins!")
                        game.computer_wins += 1
                elif computer_choice == "Paper":
                    if user_choice == "Scissors":
                        print("User wins!")
                        game.user_wins += 1
                    else:
                        print("Computer wins!")
                        game.computer_wins += 1
                elif computer_choice == "Scissors":
                    if user_choice == "Rock":
                        print("User wins!")
                        game.user_wins += 1
                    else:
                        print("Computer wins!")
                        game.computer_wins += 1
                print(f"Computer wins: {game.computer_wins}")
                print(f"User wins: {game.user_wins}")
                print("")

# play the game
play_game()