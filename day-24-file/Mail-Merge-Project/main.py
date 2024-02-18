# Main Merge Program.

# Contants.
START_LETTER_FILE = './Input/Letters/starting_letter.txt'
INVITE_NAMES_FILE = './Input/Names/invited_names.txt'
OUTPUT_DIR = './Output/ReadyToSend/'
PLACEHOLDER = '[name]'

# Open and Read the starting letter file.
with open(START_LETTER_FILE) as letter:
    letter_content = letter.read()

# Open and Read the invited names file and get the names in a list.
name_list = []
with open(INVITE_NAMES_FILE) as names:
    data = names.readlines()

# Remove all the whitespace character.
for name in data:
    name_list.append(name.strip())

# Create the letter content for each name in the name list and save it to output directory.
for name in name_list:
    print(f'\nSaving Letter for {name}')
    # Replace the [name] placeholder with the actual name.
    new_letter = letter_content.replace(PLACEHOLDER, name)

    # Save the letters in the folder "ReadyToSend".
    new_letter_name = OUTPUT_DIR + f'letter_for_{name}.txt'
    with open(new_letter_name, mode='w') as letter:
        letter.write(new_letter)

