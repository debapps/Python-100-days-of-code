# U.S State Quiz Game.
# You have to name a correct U.S state name. The correct US state will be mark on screen map.

import turtle
import pandas as pd
from text_writer import TextWriter

# Set up the game screen with the map of USA as background.
screen = turtle.Screen()
screen.title('U.S State Game')
back_img = 'blank_states_img.gif'
screen.addshape(back_img)
turtle.shape(back_img)

# Get the dataframe of 50 states.
state_data = pd.read_csv('50_states.csv')

# Get the text writer object.
text = TextWriter()

input_title = 'Guess a U.S State'
game_on = True
guessed_states = []

while game_on:

    # Get the user input.
    user_answer = turtle.textinput(title=input_title, prompt='Enter a US state name:').title()

    # Check if there is state data available for the user answer.
    state = state_data[state_data.state == user_answer]
    if not state.empty:
        text.write_text(state)
        guessed_states.append(user_answer)
        
    
    # If all the states are guessed.
    if len(guessed_states) == 50 :
        game_on = False

    if user_answer == 'Exit':
        game_on = False
        
        # Write the rest of the states in states_to_learn.csv file.
        all_states = state_data.state.to_list()
        missing_states = [state for state in all_states if state not in guessed_states]
        
        states_to_learn = pd.DataFrame({'state': missing_states})
        states_to_learn.to_csv('states_to_learn.csv')


    
    # Change the input title to show score.
    input_title = f'{len(guessed_states)}/50 Correct Guesses'


