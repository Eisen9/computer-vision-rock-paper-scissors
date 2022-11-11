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
3. Copied the *keras_model.h5* and *labels.txt* to the same directory RPS-Template resides in. These two files were taken from the model that was downloaded from *TeachableMachine* -- The model was built, trained and downloaded from there.
4. Ran the code. You may need to run it twice twice as the first run may not produce results, for some reason.

--------------
## Milestone 3
*refine later*: to export the list of requirements to a file you can either do:
`pip list > requirements.txt` or `conda env export > env.yaml`.
How can this be useful? To create an env with desired dependicies, you can do:
`conda env create --f env.yaml -n new_test_env`


--------------
## Milestone 4
