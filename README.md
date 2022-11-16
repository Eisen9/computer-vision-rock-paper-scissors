# Computer Vision RPS

## Milestone 1
Setting up the environment.

--------------
## Milestone 2
Created an *Image Project* in [TeachableMachine](https://teachablemachine.withgoogle.com/train) then downloaded it to my local machine and ran it with the code template provided *RPS-Template.py*.

**Technical Steps:**
1. Created a new env by running `conda create -n AiCore_Testing python=3.9.12`
2. Intalled tensorflow opencv and keras. by running: 
`pip install tensorflow`, `pip install opencv-python opencv-python-headless` and
`pip install keras`.
3. Copied the *keras_model.h5* and *labels.txt* to the same directory RPS-Template resides in. These two files were taken from the model that was downloaded from *TeachableMachine* -- The model was built, trained and downloaded from there. Note, the code you need to download from *Teachablemachines* is taken from the *Tensorflow* section, there are two options: *Keras* and *OpenCV Keras*, you need to downlaod **Keras**.
4. Ran the code. You may need to run it twice as the first run may not produce results, for some reason.

--------------
## Milestone 3
Installing the dependenices -- already mentiond in *Milestone 2*.
Notes: to export the list of requirements to a file you can either do:
`pip list > requirements.txt` or `conda env export > env.yaml`.
How can this be useful? To create an env with desired dependicies, you can do:
`conda env create --f env.yaml -n new_test_env`


--------------
## Milestone 4
Creating a Python script that simulats the game. The code asks the user for their input and compares it with a random choice from the computer, then, according to the classical rules of RPS, the winner is announced.
The script is creates and uses the following functions:
`get_computer_choice`: randomly picks an option between "Rock", "Paper", and "Scissors" and returns the choice.
`get_user_choice`: asks the user for an input and returns it.
`get_winner`: This function decides who the winner is (user or computer), based on their selected choices using the classical rules of Rock, Paper, Scissors.
`play`: This function plays the game of RPS by:
assigning the get_computer_choice and the get_user_choicefunctions to
variables then passing these two variables as arguments for the 
get_winner function.

--------------
## Milestone 5
In this milestone, we bring the project to its final stage. Find the code for this milestone in a file called `camera_rps.py`. When you run this file, you play the Rock Paper Scissors (RPS) with your computer: you show either Rock, Paper or Scissors to the camera that will be invoked when you run the file, then the computer picks a random choice of Rock, Paper or Scissors... The winner is decided according to the classical rules of RPS. 

