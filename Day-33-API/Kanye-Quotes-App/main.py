from tkinter import *
import requests

# API URL
API_URL = 'https://api.kanye.rest'

def get_quote():
    response = requests.get(url=API_URL)
    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()
        message = data['quote']

        canvas.itemconfig(quote_text, text=message)


# ---------------------- UI Setup ----------------------#
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=300, height=414, bg='white', highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text='', width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

get_quote()

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, bg='white', border=0, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()