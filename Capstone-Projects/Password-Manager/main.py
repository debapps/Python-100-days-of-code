from tkinter import *
from tkinter import messagebox
import random
import json

# Constants.
FONT = ('Arial', 16, 'normal')
PASSWORD_FILE = './data/password.json'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_password():
    """Generates a random password."""

    letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Get the random counts of letters, numbers and symbols.
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    # Get the random samples of letters, numbers and symbols.
    rand_letters = random.sample(letters, nr_letters)
    rand_numbers = random.sample(numbers, nr_numbers)
    rand_symbols = random.sample(symbols, nr_symbols)

    # Generate the list of random characters used in the password.
    all_pass_char = rand_letters + rand_numbers + rand_symbols
    
    # Resuffle all the characters randomly.
    random.shuffle(all_pass_char)

    # Get the random password.
    random_password = ''.join(all_pass_char)

    # The random password is populated into the password entry after clearing it..
    password_entry.delete(0, END)
    password_entry.insert(0, random_password)

    # Copy the password to clipboard.
    window.clipboard_clear()
    window.clipboard_append(random_password)



# ---------------------------- SEARCH PASSWORD ------------------------------- #
    
def search_data():
    """Search the existing credentials from the file."""
    # Get the input entry data.
    website = website_entry.get()

    try:
        with open(PASSWORD_FILE, 'r') as data_file:
            # Get the existing data from the password file.
            data = json.load(data_file) 
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Password File Exists!')
    else:
        try:
            website_data = data[website]
        except KeyError:
            messagebox.showerror(title='Error', message=f'No credentials exists for the {website}')
        else:
            messagebox.showinfo(title=website, message=f'Website: {website}\nEmail: {website_data['id']}\nPassword: {website_data['password']}')


# ---------------------------- SAVE PASSWORD ------------------------------- #
    
def write_json_data(json_data):
    """Writes JSON data into the password file."""
    data = None

    try:
        with open(PASSWORD_FILE, 'r') as data_file:
            # Get the existing data from the password file.
            data = json.load(data_file)            

    except:
        data = json_data

    else:
        # Get the updated data.
        data.update(json_data)

    finally:
        # Write the data into password file.
        with open(PASSWORD_FILE, 'w') as data_file:
            json.dump(data, data_file, indent=4)


def save_password_data():
    """Stores the input data into the file."""

    # Get the input entry data.
    website = website_entry.get()
    id = id_entry.get()
    password = password_entry.get()

    # If any of the input fields is empty, show error and do nothing.
    if len(website) == 0 or len(id) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops', message='Please do not leave any field empty!')
        return


    # is_ok = messagebox.askokcancel(title=website, 
    #         message=f'The details enterd as follows:\nEmail: {id}\nPassword: {password}\nIs it okay to save?')
    
    # if is_ok:
    #     # Format the data row to be written.
    #     data_row = f'{website} | {id} | {password}\n'

    #     # Write the data row into the password file.
    #     with open(PASSWORD_FILE, 'a') as file:
    #         file.write(data_row)

    # Format the data to be written in JSON.
    new_data = {
        website: {
            'id': id,
            'password': password 
        }
    }
    
    write_json_data(new_data)
        
    # Clear the entry widgets.
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Get the photo from the file.
logo = PhotoImage(file='logo.png')

# Canvas widget to hold the photo.
logo_canvas = Canvas(window, width=200, height=200, highlightthickness=0)
logo_canvas.create_image(100, 100, image=logo)

# Label widgets.
website_label = Label(window, text='Website:', font=FONT)
id_label = Label(window, text='Email/Username:', font=FONT)
password_label = Label(window, text='Password:', font=FONT)

# Entry widgets.
website_entry = Entry(window, font=FONT, width=21)
website_entry.focus()

id_entry = Entry(window, font=FONT, width=35)
id_entry.insert(0, 'bittu@email.com')

password_entry = Entry(window, font=FONT, width=21)

# Button widgets.
gen_pass_btn = Button(window, text='Generate Password', font=FONT, command=generate_random_password)
add_btn = Button(window, text='Add', font=FONT, width=36, command=save_password_data)
search_btn = Button(window, text='Search', font=FONT, command=search_data, width=15)

# Geometry Manager Methods
logo_canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1)
search_btn.grid(row=1, column=2)
id_label.grid(row=2, column=0)
id_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
gen_pass_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()