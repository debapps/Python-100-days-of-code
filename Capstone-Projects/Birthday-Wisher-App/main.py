##################### Birthday Wisher Project ######################
import pandas as pd
from datetime import date
import os
from random import choice
from dotenv import load_dotenv
import smtplib

# Load the environment file.
load_dotenv()

# Constants.
BIRTHDAY_FILE = 'birthdays.csv'
LETTER_DIR = 'letter_templates'
PLACEHOLDER = '[NAME]'
FROM_EMAIL = 'bhar.debaditya@gmail.com'
APP_PASS = os.getenv('APP_PASS_CODE')
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587

# TODO 1. Check if today matches a birthday in the birthdays.csv

# Open the birthdays.csv file and get the content into a dataframe.
data = pd.read_csv(BIRTHDAY_FILE)

# Get the today's date and extract the current month and date.
today = date.today()
current_month = today.month
current_date = today.day

# Check if the month and day in the file matches the today's month and date, 
# then pick the names and emails into a list of dictionaries.
birthday_people = data[(data['month'] == current_month) & (data['day'] == current_date)][['name', 'email']].to_dict(orient='records')

# TODO 2. Send the letter generated in step 3 to that person's email address.

def send_birthday_letter(to_email, name, letter):
    """This function sends the birthday letter to email (to_email)"""
    
    # Create a SMTP connection.
    with smtplib.SMTP(host=MAIL_HOST, port=MAIL_PORT) as connection:
        # Put the connection to SMTP server into TLS mode.
        connection.starttls()
        # Login to the sender email.
        connection.login(user=FROM_EMAIL, password=APP_PASS)
        # Send the email.
        connection.sendmail(
            from_addr=FROM_EMAIL, 
            to_addrs=to_email, 
            msg=f'Subject: Happy Birthday {name}! \n\n{letter}'
        )

# TODO 3. If step 1 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# and send the letter to the corresponding email.

# Get the sample letter template file names from the letter directory.
letter_templates = os.listdir(LETTER_DIR)

# For each person in the birthday_people list, get a random letter template file name.
for person in birthday_people:
    letter = choice(letter_templates)
    letter_file = os.path.join(LETTER_DIR, letter)

    # Get the letter content.
    with open(letter_file) as file:
        content = file.read()
    
    # Replace placeholder [NAME] by the name of the birthday person.
    letter_content = content.replace(PLACEHOLDER, person['name'])

    print(f'Sending Birthday letter for {person["name"]} to the email: {person["email"]}')

    send_birthday_letter(person['email'], person['name'], letter_content)




