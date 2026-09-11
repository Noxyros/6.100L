## Problem Set 2, hangman.py
## Name: Yohan
## Collaborators: None

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def help_mode(secret_word, available_letters):
    choose_from = ''
    for e in secret_word:
        if e in available_letters:
            choose_from += e

    new = random.randint(0, len(choose_from)-1)
    reveal_letter = choose_from[new]

    return reveal_letter

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for e in secret_word:
        if e not in letters_guessed:
            return False
    return True

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_progress = ""
    for e in secret_word:
        if e in letters_guessed:
            word_progress += e
        else:
            word_progress += '*'
    return word_progress

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = list(string.ascii_lowercase)
    for e in letters_guessed:
        if e in available_letters:
            available_letters.remove(e)
    return ''.join(available_letters)

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Necessary variables
    guesses_left = 10
    all_letters_guessed = []
    win = False

    #UI and Logic
    print(f"\nWelcome to Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.")
    while guesses_left > 0 and win == False:
        print("----------------------------")
        available_letters = get_available_letters(all_letters_guessed)
        print(f"You have {guesses_left} guesses left.\n"
              f"Available letters: {available_letters}")

        letters_guessed = input("Please guess a letter: ").lower()

        if len(letters_guessed) != 1:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, all_letters_guessed))
        else:
            if with_help == True and letters_guessed == '!':
                if guesses_left >= 3:
                    revealed = help_mode(secret_word, available_letters)
                    guesses_left -=  3
                    print("Letter revealed:", revealed)
                    all_letters_guessed.append(revealed)
                    print(get_word_progress(secret_word, all_letters_guessed))
                else:
                    print("Oops! Not enough guesses left:", get_word_progress(secret_word, all_letters_guessed))
            elif letters_guessed.isalpha():
                if letters_guessed in all_letters_guessed:
                    print("Oops! You've already guessed that letter:", get_word_progress(secret_word, all_letters_guessed))
                elif letters_guessed not in secret_word:
                    all_letters_guessed.append(letters_guessed)
                    if letters_guessed in 'aeiou':
                        guesses_left -= 2
                    else:
                        guesses_left -= 1
                    print("Oops! That letter is not in my word:", get_word_progress(secret_word, all_letters_guessed))
                else:
                    all_letters_guessed.append(letters_guessed)
                    print("Good guess:",  get_word_progress(secret_word, all_letters_guessed))
            else:
                print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, all_letters_guessed))

        win = has_player_won(secret_word, all_letters_guessed)

    print("----------------------------")

    if win:
        unique = []
        for e in secret_word:
            if e not in unique:
                unique.append(e)
        total_score = (guesses_left + 4 * len(unique) + (3 * len(secret_word)))
        print(f"Congratulations, you won!\n"
              f"Your total score for this game is: {total_score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass