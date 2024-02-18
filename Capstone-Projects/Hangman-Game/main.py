from os import name, system
import random
from hangman_art import hangman_logo, hangman_stages
from hangman_words import word_list

def clear():
    """This clears the screen."""
    # For Linux and Mac OS.
    if name == 'posix':
        system('clear')
    # For Windows.
    elif name == 'nt':
        system('cls')

# Display the hangman logo.
print(hangman_logo)

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# Testing Code.
# print(f'Chit: {chosen_word}')

# Create a empty list called "display" and for each letter in the chosen_word, add an underscore "_" to the list.

display = []
for letter in chosen_word:
    display.append("_")

# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6

# Use a while loop to let the user guess letters until they guess the chosen_word. The loop should only stop when the user has guessed all the letters in the chosen_word and all elements in "display" list has no more "_". Then we can tell user that they have won.

end_of_game = False

while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

    guess = input("Guess a letter: ").lower()

    # Clears the screen.
    clear()

    # If user entered a letter, they have already guessed earlier, print the letter and let them know.
    if guess in display:
        print(f'You\'ve already guessed {guess}')

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Loop through the chosen_word and if the "guess" is in the chosen_word at the position, add that letter to the list "display" to reveal the letter.

    for idx in range(len(chosen_word)):
        if chosen_word[idx] == guess:
            display[idx] = guess

    # If guess is not a letter in the chosen_word, then reduce 'lives' by 1.

    if guess not in chosen_word:
        print(f'You guess {guess}, that\'s not in the word. You lose a life')
        lives -= 1

    # If lives goes down to 0 then the game should stop and it should print "You lose."

    if lives == 0:
        print("You lose. The word was: ", chosen_word)
        end_of_game = True

    # Join all the elements in the list and turn it into a String.
    print(' '.join(display))

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_stages[lives])

    # The loop should only stop when the user has guessed all the letters in the chosen_word and all elements in "display" list has no more "_". Then we can tell user that they have won.
    if "_" not in display:
        print("You won!")
        end_of_game = True
