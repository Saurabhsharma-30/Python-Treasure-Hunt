# Treasure Hunt Game

## Overview

The Treasure Hunt Game is a simple console-based game where the player attempts to find a hidden treasure on a grid-based board. The player has a limited number of attempts to guess the location of the treasure. After each guess, the game provides feedback on how close the guess is to the actual location of the treasure.

## Features

- **Board Initialization:** The game board is a square grid initialized with empty spaces.
- **Random Treasure Placement:** The treasure is randomly placed on the board at the start of each game.
- **Distance Feedback:** After each guess, the game provides feedback on how close the player is to the treasure, based on the Manhattan distance.
- **Limited Attempts:** The player has a maximum number of attempts to find the treasure.
- **Game Over:** The game ends either when the player finds the treasure or when they run out of attempts.

## How to Play

1. **Game Start:**
   - The game starts by displaying a grid representing the board.
   - The player is prompted to guess the location of the treasure by entering row and column numbers.

2. **Making a Guess:**
   - Enter a row number between `0` and `size-1`.
   - Enter a column number between `0` and `size-1`.

3. **Feedback:**
   - If the guess is correct, the game congratulates the player.
   - If the guess is incorrect, the game provides feedback:
     - **Very close!** if the guess is within a Manhattan distance of 2.
     - **Close.** if the guess is within a Manhattan distance of 5.
     - **Far away.** if the guess is farther away.
   - The guessed location is marked on the board with an `X`.

4. **Game End:**
   - The game ends when the player either finds the treasure or uses up all attempts.
   - If the player fails to find the treasure, the location of the treasure is revealed.

## Code Structure

- **`initialize_board(size)`**: Creates and returns an empty game board of the specified size.
- **`place_treasure(board, size)`**: Randomly selects and returns the row and column indices for the treasure's location.
- **`print_board(board, size)`**: Displays the current state of the board.
- **`get_distance(treasure_row, treasure_col, guess_row, guess_col)`**: Calculates the Manhattan distance between the guessed location and the treasure.
- **`play_game(size=5, max_attempts=10)`**: Main game loop that handles user input, checks the guess, and provides feedback.

## Requirements

- Python 3.x

## Running the Game

To run the game, simply execute the Python script. The game will initialize and prompt the user to start guessing the treasure's location.

```bash
python treasure_hunt_game.py
```

## Customization

- **Board Size:** The size of the board can be adjusted by modifying the `size` parameter in the `play_game` function.
- **Number of Attempts:** The maximum number of attempts can be customized by changing the `max_attempts` parameter in the `play_game` function.

## Example

```plaintext
Welcome to the Treasure Hunt Game!
Find the treasure hidden on the board.
  0 1 2 3 4
0          
1          
2          
3          
4          

Attempt 1/10 - Enter row (0-4): 2
Attempt 1/10 - Enter column (0-4): 3
Close.
  0 1 2 3 4
0          
1          
2       X  
3          
4          
```
---

Enjoy the game and happy treasure hunting!
