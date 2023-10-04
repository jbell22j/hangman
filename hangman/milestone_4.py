import random
import string

class Hangman:
    
    '''
    This class is used for the Hangman game.

    Attributes:
        word_list(list) = the user's chosen list of words to choose a random word from.
        number_of_lives(int) = the user's chosen amount of lives allowed in that game.#
        chosen_word(str) = the chosen random word from the user's word_list.
        chosen_word_guessed(list) = a list of _ at each index the length of the chosen_word to represent the characters still to be guessed.
        number_of_unguessed_characters(int) = the number of characters in the chosen_word still to be guessed, initially the length of the chosen_word.
        list_of_guesses = initially an empty list, characters users input will be added to the list to keep track of previously guessed characters.

    '''

    def __init__(self,word_list,number_of_lives):

        '''
        See help(Hangman) for accurate signature
        '''

        self.word_list = word_list
        self.number_of_lives = number_of_lives
        self.chosen_word = random.choice(self.word_list).lower()
        self.chosen_word_guessed = ["_"]*len(self.chosen_word)
        self.number_of_unguessed_characters = self.chosen_word_guessed.count("_")
        self.list_of_guesses = []

    def _add_correct_guess_to_list(self,guess):
        '''
        This function is to add correct guesses to the list of unguessed characters and print the list so users can see their progress in guessing the chosen_word.

        Parameters:
            guess (str): a lower case alphabetical character inputted by the user.

        Returns:
        -------
        None
        '''
        for i in range(len(self.chosen_word)):
            if self.chosen_word[i] == guess:
                self.chosen_word_guessed[i] = guess
        print(f"Here is how your guesses look so far: {self.chosen_word_guessed}")
        self.number_of_unguessed_characters = self.number_of_unguessed_characters - 1

    def check_guess_in_word(self,guess):
        '''
        This function converts guess to lowercase, then checks if the guess is in the chosen_word then passes to the add_correct_guess_list function.
        If the guess is not in chosen_word the function takes a life away from the user.

        Parameters:
            guess (str): a lower case alphabetical character inputted by the user.

        Returns:
        -------
        None
        '''
        guess = guess.lower()
        if guess in self.chosen_word:
            print(f"Good guess! {guess} is in the word!")
            self._add_correct_guess_to_list(guess)
        else:
            self.number_of_lives = self.number_of_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again!")
            print(f"You have {self.number_of_lives} lives left.")

    def ask_for_input(self):
        '''
        This function is to loop user input until either the user wins the game or has no lives remaining, also checks user input to see if it is valid, i.e. a single alphabetical character.
        Function passes to check_guess_in_word if user input is valid.
        Function adds guess to list_of_guesses so user can keep track of which characters they have already attempted.
        
        Parameters:
        -------
        None

        Returns:
        -------
        None
        '''
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess_in_word(guess)
                self.list_of_guesses.append(guess)
                print(f"Characters you've guessed already: {self.list_of_guesses}")


game = Hangman( ["Pineapple","Mango","Orange","Coconut","Banana"],3)

game.ask_for_input()
    
    
    