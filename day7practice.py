# this is a program that was made to be the building blocks for the hangman game. It essentially creates a random choice from the added word list
# and assigns that as choosen word. After this, it allows the user to input a random letter which is checked against the chosen word. If the letter
# is in the chosen word, then it is added to a list that was created known as display. The parameters for display are that it will be the same characters as the string
# choosen word and as a letter is put in the matched the guess variable, it will be added to display
import random
from hangman_words import word_list
from hangman_art import logo, stages
chosen_word = random.choice(word_list)

display = []
for character in range(1,len(chosen_word)+1):
# an alternate way to display this would be range(len(choosen_word). This could be the better option because it does not shift the position. The way i did it will give the
# same number of characters but they start at 1 instead of zero and so cannot be used when trying to determine specific positioning.
    display.append('_')
lives = 6
end_of_game = False

print(logo,'\nWelcome to hangman!')
while not end_of_game and lives > 0:
    guess = str(input('guess a letter: ')).lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess in display:
        print(f'You have guessed {guess}, try another letter.')

    if guess not in chosen_word:
        print(f'{guess} is not in the word, you lose a life.')
        lives -= 1
        print(f'You have {lives} lives left')
        print(stages[lives])
    else:
        print(f'You have {lives} lives left')
        print(stages[lives])

    if '_' not in display:
        end_of_game = True
        print('You win!!')

if lives == 0:
    print('You ran out of lives, you lose :(')
    print(f'The word was {chosen_word}.')

