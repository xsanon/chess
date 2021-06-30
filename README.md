# Chess
created by XS

A simple command line chess game using Python

## Starting the Game
1. Clone this repository
2. In the command line, go to the src directory
3. run `python chess.py` or `python3 chess.py`

## How to Play
The rules are standard chess rules.

Each turn, you will be prompted with `from: ` and `to: ` which you will enter a board position of a piece (ie. '2d') to where you want to move it (ie. '3d').

### Notes
Chess board only prints properly on Unix-type terminals due to system-specific colored printing. 
For Windows, check out Ubuntu on WSL.

Not currently supported: 
 * checking that king does not threaten king
 * checking for checks
 * checking for checkmates
