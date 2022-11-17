
# Computer Vision Rock Paper Scissors Project Documentation 

> Rock Paper Scissors (RPS) Game is a game that asks two users to display Rock, Paper or Scissors at the same time and declares a winner according to the classical rule of RPS. 
- In this project the computer chooses an option (rock, paper, or scissors) and then ask the user for an input and the user has to decide.

- User's input will first be entered manually. In the next stage of the project, we use the camera (using computer vision techniques) to get the input of the user.

- To start, we need to install all libraries and python packages that we need for this project.

## Milestone 1

- Create a virtual environment:

    - First, create a conda environment and then install the necessary requirements as well as opencv-python, tensorflow, and ipykernel.

    - After creating the environment, activate it, and then install pip as following:
    ```code
    conda install pip
    ```
    
    Now in order to install any library, you can run:
    ```code
    pip install <library>
    ```

    - Important: In some cases (depending on your current OS) the latest version of Tensorflow may not work with the default version of Python. When creating the virtual environment, use Python 3.8 instead by running:
    ```code
    conda create -n my_env python=3.8
    ```

    Where my_env is the name of the environment you want to create.

   
- See exact libraries in *Milestone 2* below.

--------------
## Milestone 2
Created an *Image Project* in [TeachableMachine](https://teachablemachine.withgoogle.com/train) then downloaded it to my local machine and ran it with the code template provided *RPS-Template.py*.

**Technical Steps:**
1. Created a new env by running `conda create -n AiCore_Testing python=3.9.12`
2. Installed tensorflow opencv and keras. by running: 
`pip install tensorflow`, `pip install opencv-python opencv-python-headless` and
`pip install keras`.
3. Copied the *keras_model.h5* and *labels.txt* to the same directory RPS-Template resides in. These two files were taken from the model that was downloaded from *TeachableMachine* -- The model was built, trained and downloaded from there. Note, the code you need to download from *Teachablemachines* is taken from the *Tensorflow* section, there are two options: *Keras* and *OpenCV Keras*, you need to download **Keras**.
4. Ran the code. You may need to run it twice as the first run may not produce results, for some reason.

--------------
## Milestone 3
Installing the dependencies -- already mentioned in *Milestone 2*.
Notes: to export the list of requirements to a file you can either do:
`pip list > requirements.txt` or `conda env export > env.yaml`.
How can this be useful? To create an env with desired dependencies, you can do:
`conda env create --f env.yaml -n new_test_env`


--------------
## Milestone 4
Creating a Python script that simulates the game. The code asks the user for their input and compares it with a random choice from the computer, then, according to the classical rules of RPS, the winner is announced.
The script is creates and uses the following functions:
`get_computer_choice`: randomly picks an option between "Rock", "Paper", and "Scissors" and returns the choice.
`get_user_choice`: asks the user for an input and returns it.
`get_winner`: This function decides who the winner is (user or computer), based on their selected choices using the classical rules of Rock, Paper, Scissors.
`play`: This function plays the game of RPS by:
assigning the get_computer_choice and the get_user_choice functions to
variables then passing these two variables as arguments for the 
get_winner function.

--------------
## Milestone 5
In this milestone, we bring the project to its final stage. Find the code for this milestone in a file called `camera_rps.py`. When you run this file, you play the Rock Paper Scissors (RPS) with your computer: you show either Rock, Paper or Scissors to the camera that will be invoked when you run the file, then the computer picks a random choice of Rock, Paper or Scissors... The winner is decided according to the classical rules of RPS. 

**Improved Application**
User can run the file `rps_class_final.py` to play the game. This class encapsulates the code for the game in a class without the need to invoke other files; it is a stand alone file. The user can play the game by running the file and following the instructions displayed on the console.

