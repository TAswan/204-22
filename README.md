# CISC/CMPE 204 Modelling Project

Welcome to the Tetris Modelling Project!

In Tetris, players manipulate falling shapes called Tetromino’s within a playing area measuring ten squares in width and twenty squares in height. There are seven distinct Tetromino shapes. The objective is to manoeuvre and rotate these falling pieces to complete entire rows in the playing field. This process is referred to as a line clear.

The aim of this project is to model a game of Tetris, and analysing the state of the game so that given a random board and Tetromino in play we can find if a row can be cleared successfully within 20 moves of the Tetromino.

## Structure

* `constructors.py`: Contains all proposition classes.
* `documents`: Contains folders for both of our draft and final submissions. README.md files are included in both.
* `run.py`: General wrapper script which runs the 4 main phases of our algorithm and adds constraints to the model.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.
* `tetrominos.py`: Provides coordinate definitions for each Tetromino and rotation.
