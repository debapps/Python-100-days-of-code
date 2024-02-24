# The Flash Card Program.

from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import os

# Program Constants.
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
DATA_FILE = './data/words_to_learn.csv'
INITIAL_DATA_FILE = './data/french_words.csv'

#------------------------------- Listener Functions -------------------------------#

def read_data_file(filename):
    """This function reads the file and returns the rows as list of dictionary."""
    
    data = None
    try:
        # Get the dataframe from the CSV words file.
        data = pd.read_csv(filename)
    except FileNotFoundError:
        try:
            data = pd.read_csv(INITIAL_DATA_FILE)
        except FileNotFoundError as error:
            messagebox.showerror(title='ERROR', message=error)
    
    # If the valid data exists.
    if data.shape[0]:
        card_to_learn = data.to_dict(orient='records')
        return card_to_learn
    else:
        messagebox.showerror(title='ERROR', message='Data File issue!')

# Call the read file initially and save the data rows into a Global Variable.   
card_to_learn = read_data_file(DATA_FILE)
current_card = None

def show_flash_word(mode, color = 'black'):
    """This function show text on flash card based on mode. 
    Parameter: 
    mode: str = 'French' | 'English'.
    color: str = 'black'| 'white' (Default 'black')."""

    flash_card_canvas.itemconfig(title_text, text=mode, fill=color)
    flash_card_canvas.itemconfig(word_text, text=current_card[mode], fill=color)

def flip_card():
    """This function shows the back of the card with English word."""
    flash_card_canvas.itemconfig(card_image, image=card_back)
    show_flash_word('English', color='white')


def next_card():
    """This function picks the random French and English words from the data file."""

    global current_card, flip_timer

    window.after_cancel(flip_timer)

    # Change the card background as front image.
    flash_card_canvas.itemconfig(card_image, image=card_front)

    if len(card_to_learn) > 0:
        # Get the random data row.
        current_card = random.choice(card_to_learn)
        # Display the random french word on the flash card.
        show_flash_word('French')

        # After 3s (3000 ms) the card should flip and show the English Word.
        flip_timer = window.after(3000, flip_card)
    else:
        messagebox.showinfo(title='Wow!', message='You have learn all the words!\nClose the application to reload the word file.')
        os.remove(DATA_FILE)

def right_next_card():
    """This function is called when the right check button is pressed. 
    The current card data will be removed from the cards to learn list."""

    global card_to_learn

    card_to_learn.remove(current_card)

    # Save the data into words_to_lern.csv
    new_data = pd.DataFrame(card_to_learn)
    new_data.to_csv(DATA_FILE, index=False)

    # Show next card.
    next_card()


#------------------------------------ UI Setup ------------------------------------#
window = Tk()
window.title('Flash Card App - French to English')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flash Card Canvas.
flash_card_canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Card Front Image.
card_front = PhotoImage(file='./images/card_front.png')
# Card Back Image.
card_back = PhotoImage(file='./images/card_back.png')
# Show front image on the card. 
card_image = flash_card_canvas.create_image(400, 263, image=card_front)
title_text = flash_card_canvas.create_text(400, 150, text='language', font=TITLE_FONT)
word_text = flash_card_canvas.create_text(400, 263, text='word', font=WORD_FONT)

# Buttons Images.
right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')

# Buttons.
right_btn = Button(window, image=right_image, border=0, highlightthickness=0, command=right_next_card)
wrong_btn = Button(window, image=wrong_image, border=0, highlightthickness=0, command=next_card)

# Application Layouts: Geometry Manager Functions.
flash_card_canvas.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row=1, column=0, pady=5)
right_btn.grid(row=1, column=1, pady=5)

# Flip the card after 3s.
flip_timer = window.after(3000, flip_card)

# Pick a random French word on the card for the first time.
next_card()

window.mainloop()
