# Hangman

## Table of Contents

- Introduction
- Project Aims
- Project Outcomes
- Instructions
- File Structure

## Introduction

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game created in Python, where the computer randomly chooses a word from a given list from the user and the user then tries to guess it. The length of the game is also customisable, can choose lower amount of lives to increase difficulty.

## Project Aims

The projects aim was to create a playable Hangman game using the python techniques taught in the bootcamp thus far. This included lists,functions,loops, encapsulation, abstraction, using docstrings, object oriented programming, debugging and using the command line and GitHub to correctly upload code and use markdown.

## Project Outcomes

Created a Hangman class using an intialiser to take user input of a list of possible words to use in the game and number of lives in the game. Created four functions that built upon each other to allow a smoothly running game with no bugs arising from any user input for guesses. Using a randomiser, generators, if-else statements and for statements in the successful output of a playable user-friendly hangman game in Python.

## Instructions

- Create a new instance, for example: mygame = Hangman([],int), inserting a list of words (can be as may or as little you like, fewer words means an easier game) and an integer number of lives.
- Then mygame.play_hangman_game() will start the game and you can start inputting single alphabetical characters to guess the random word the computer has chosen from your list.
- Any character that is not alphabetical or single will flag an error.
- The rest is self-explanatory the game will run until you lose or win!

## File Structure

The files milestone_2-4.py are the building blocks for the main Python file milestone_5.py which is the finished playable Hangman game.

