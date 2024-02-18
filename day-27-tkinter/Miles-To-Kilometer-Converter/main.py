# This program is the GUI program that converts the miles to kilometer.
# This uses Tkinter module to build the GUI.

from tkinter import *

FONT = ('Arial', 16)
NUM_FONT = ('Courier', 16)

# This function converts Miles to kilometer.
def convert_mile_km():
    miles = float(mile_entry.get())
    km = round(miles * 1.609344, 2)
    km_val.config(text=str(km))

# Create the window.
window = Tk()
window.minsize(width=300, height=100)
window.title('Miles to Km Converter')
window.config(padx=20, pady=20)

# Create Entry for Miles.
mile_entry = Entry(window, width=10, font=NUM_FONT)

# Labels
mile_label = Label(window, text='Miles', font=FONT)
equal_label = Label(window, text='is equal to', font=FONT)
km_val = Label(window, text='0', font=NUM_FONT)
km_label = Label(window, text='Km', font=FONT)

# Button
cal_btn = Button(window, text='Calculate', font=FONT, command=convert_mile_km)

# Geometry Managers.
mile_entry.grid(column=1, row=0, padx=5, pady=5)
mile_label.grid(column=2, row=0, pady=5)
equal_label.grid(column=0, row=1, padx=5, pady=5)
km_val.grid(column=1, row=1, padx=5, pady=5)
km_label.grid(column=2, row=1)
cal_btn.grid(column=1, row=2, pady=5)

window.mainloop()