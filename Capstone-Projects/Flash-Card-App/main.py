# The Flash Card Program.

from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

# Program Constants.
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
DATA_FILE = './data/french_words.csv'

#------------------------------- Listener Functions -------------------------------#
# Global Variable
data_rows = None

def read_data_file(filename):
    """This function reads the file and returns the rows as list of dictionary."""
    global data_rows
    
    try:
        # Get the dataframe from the CSV words file.
        data = pd.read_csv(filename)
    except FileNotFoundError as error:
        messagebox.showerror(title='ERROR', message=error)
    else:
        data_rows = data.to_dict(orient='records')
        return data_rows

def show_flash_word(mode, row):
    """This function show text on flash card based on mode. 
    Parameters: 
    1. mode: str = 'French' | 'English'. 
    2. row: Data row dictionary."""

    flash_card_canvas.itemconfig(title_text, text=mode)
    flash_card_canvas.itemconfig(word_text, text=row[mode])

def pick_random_word():
    """This function picks the random French word from the data file."""
    # Get the file data.
    rows = read_data_file(DATA_FILE)
    # Get the random data row.
    random_row = random.choice(rows)
    # Display the random french word on the flash card.
    show_flash_word('French', random_row)

#------------------------------------ UI Setup ------------------------------------#
window = Tk()
window.title('Flash Card App - French to English')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flash Card Canvas.
flash_card_canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Front Card Image.
card_front = PhotoImage(file='./images/card_front.png')
flash_card_canvas.create_image(400, 263, image=card_front)
title_text = flash_card_canvas.create_text(400, 150, text='language', font=TITLE_FONT)
word_text = flash_card_canvas.create_text(400, 263, text='word', font=WORD_FONT)

# Buttons Images.
right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')

# Buttons.
right_btn = Button(window, image=right_image, border=0, highlightthickness=0, command=pick_random_word)
wrong_btn = Button(window, image=wrong_image, border=0, highlightthickness=0, command=pick_random_word)

# Application Layouts: Geometry Manager Functions.
flash_card_canvas.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row=1, column=0, pady=5)
right_btn.grid(row=1, column=1, pady=5)

window.mainloop()
