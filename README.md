# Hangman

## Table of Contents

- [Introduction](#brief)
- [Project Aims](#aim)
- [Project Outcomes](#outcome)
- [Key Tools](#tools)
- [Game Breakdown](#instructions)
- [File Structure](#structure)

<a id="intro"></a>
## Introduction

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game created in Python, where the computer randomly chooses a word from a given list from the user and the user then tries to guess it. The length of the game is also customisable, can choose lower amount of lives to increase difficulty.

<a id="aim"></a>
## Project Aims

The projects aim was to create a playable Hangman game using the python techniques taught in the bootcamp thus far. This included lists,functions,loops, encapsulation, abstraction, using docstrings, object oriented programming, debugging and using the command line and GitHub to correctly upload code and use markdown.

## Project Outcomes

Created a Hangman class using an intialiser to take user input of a list of possible words to use in the game and number of lives in the game. Created four functions that built upon each other to allow a smoothly running game with no bugs arising from any user input for guesses. Using a randomiser, generators, if-else statements and for statements in the successful output of a playable user-friendly hangman game in Python.

<a id="tools"></a>
## Key Tools

* [Python](https://wiki.python.org/moin/BeginnersGuide/Programmers) is a programming language that lets you work more quickly and integrate your systems more effectively and is used here as the language to create our game within.
* [random](https://docs.python.org/3/library/random.html) is a module which implements pseudo-random number generators for various distributions and is used in our project to generate a random number to pick the index of a word within our hangman options list.
<img width="288" alt="image" src="https://github.com/jbell22j/hangman/assets/141024595/5a9eb69e-0b85-4034-9b8e-2ef36094a222">


<a id="instructions"></a>
## Game Breakdown

Create a new instance, for example: mygame = Hangman([],int), inserting a list of words (can be as may or as little you like, fewer words means an easier game) and an integer number of lives. The `Hangman` class has the following attributes :
* self.word_list = the user's chosen list of words to choose a random word from.
* self.number_of_lives = the user's chosen amount of lives allowed in that game.
* self.chosen_word= the chosen random word from the user's word_list.
* self.chosen_word_guessed = a list of _ at each index the length of the chosen_word to represent the characters still to be guessed.
* self.number_of_unguessed_characters = the number of characters in the chosen_word still to be guessed, initially the length of the chosen_word.
* self.list_of_guesses = initially an empty list, characters users input will be added to the list to keep track of previously guessed characters.


<img width="333" alt="image" src="https://github.com/jbell22j/hangman/assets/141024595/1d427a05-f3a9-4cb8-807d-5742914561f1">

Then mygame.play_hangman_game() will start the game and you can start inputting single alphabetical characters to guess the random word the computer has chosen from your list. Any character that is not alphabetical or single will flag an error. The rest is self-explanatory the game will run until you lose or win!

<img width="540" alt="image" src="https://github.com/jbell22j/hangman/assets/141024595/59bcaad8-d89a-4666-a195-761a92f6c042">

<a id="structure"></a>
## File Structure

The files milestone_2-4.py are the building blocks for the main Python file milestone_5.py which is the finished playable Hangman game.

