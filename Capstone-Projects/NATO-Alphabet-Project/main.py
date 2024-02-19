import pandas as pd

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

phonetic_file = 'nato_phonetic_alphabet.csv'
phonetic_data = pd.read_csv(phonetic_file)

phonetic_dict = {row.letter:row.code for (_, row) in phonetic_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Continue to take user inputs until user enters all letters from the alphabet.

def generate_phonetic():
    user_input = input('Enter a word: ').upper()
    try:
        nato_word_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print('Sorry, please enter only letters in the alphabet.')
        generate_phonetic()
    else:

        print(nato_word_list)

generate_phonetic()