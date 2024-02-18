# Python GUI program using tkinter.

from tkinter import *

# Listener functions.
def button_clicked():
    text_label.config(text=input_var.get())
    input_var.set('')
    

window = Tk()
window.title('My First GUI Program') 
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Creating a label.
heading = Label(window, text="Tkinter GUI", font=('Arial', 24, 'bold'))
text_label = Label(window, text='Hello World', font=('Courier', 16, 'italic'))

# Button
click_button = Button(window, text='Click Me', command=button_clicked)

# Entry: Input box.
input_var = StringVar()
input = Entry(window, width=20, textvariable=input_var)

# Geometry Manager Method: pack.
heading.pack(side='top', expand=False, ipadx=10, ipady=10)
input.pack()
click_button.pack()
text_label.pack()

# Geometry Manager Method: place
# heading.place(x=150, y=0)
# input.place(x=50, y=50)
# click_button.place(x=270, y=50)
# text_label.place(x=50, y=100)

# Geometry Manager Method: grid
# heading.grid(column=1, row=0)
# input.grid(column=0, row=1)
# click_button.grid(column=2, row=1)
# text_label.grid(column=0, row=2)

window.mainloop()