import random
import string

word_list = ["Pineapple","Mango","Orange","Coconut","Banana"]
print(word_list)

def random_choice(seq):
    word = random.choice(seq)
    print(f"{word}")

random_choice(word_list)
letters =string.ascii_letters

guess = input("Guess a letter: ")

if len(guess) == 1 and guess in letters:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")