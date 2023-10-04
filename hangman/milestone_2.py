import random
import string
import milestone_3

word_list = ["Pineapple","Mango","Orange","Coconut","Banana"]
print(word_list)

def random_word_choice(seq):
    chosen_word = random.choice(seq)
    print(f"{chosen_word}")

chosen_word = random_word_choice(word_list)
letters_in_alphabet =string.ascii_letters

guess = input("Guess a letter: ")

if len(guess) == 1 and guess in letters_in_alphabet:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

milestone_3.ask_for_input("g")