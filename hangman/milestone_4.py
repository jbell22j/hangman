import random
import string

class Hangman:
    

    def __init__(self,word_list,number_of_lives):
        self.word_list = word_list
        self.number_of_lives = number_of_lives
        self.chosen_word = random.choice(self.word_list)
        self.chosen_word_guessed = ["_"]*len(self.chosen_word)
        self.number_of_unguessed_characters = self.chosen_word_guessed.count("_")
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.chosen_word:
            print(f"Good guess! {guess} is in the word!")
            for letter in self.chosen_word:
                if letter == guess:
                    self.chosen_word_guessed[letter].replace(guess) 
                    print(f"{self.chosen_word_guessed}")
                else:
                    break
            self.number_of_unguessed_characters = self.number_of_unguessed_characters - 1
        else:
            self.number_of_lives = self.number_of_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again!")
            print(f"You have {self.number_of_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


game = Hangman( ["Pineapple","Mango","Orange","Coconut","Banana"],3)

game.ask_for_input()
    
    
    