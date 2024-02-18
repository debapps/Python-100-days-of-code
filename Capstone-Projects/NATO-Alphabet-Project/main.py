import pandas as pd

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

phonetic_file = 'nato_phonetic_alphabet.csv'
phonetic_data = pd.read_csv(phonetic_file)

# for (key, row) in phonetic_data.iterrows():
#     print(row.code)

phonetic_dict = {row.letter:row.code for (_, row) in phonetic_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word: ').upper()
nato_word_list = [phonetic_dict[letter] for letter in user_input]
print(nato_word_list)

