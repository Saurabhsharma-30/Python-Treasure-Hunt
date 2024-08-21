import random

def initialize_board(size):
    """Initialize the game board with empty spaces."""
    return [[' ' for _ in range(size)] for _ in range(size)]

def place_treasure(board, size):
    """Place the treasure at a random location on the board."""
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    return row, col

def print_board(board, size):
    """Print the game board."""
    print("  " + " ".join(str(i) for i in range(size)))
    for i in range(size):
        print(f"{i} " + " ".join(board[i]))

def get_distance(treasure_row, treasure_col, guess_row, guess_col):
    """Calculate the distance between the guess and the treasure."""
    return abs(treasure_row - guess_row) + abs(treasure_col - guess_col)

def play_game(size=5, max_attempts=10):
    """Main game loop."""
    board = initialize_board(size)
    treasure_row, treasure_col = place_treasure(board, size)
    
    print("Welcome to the Treasure Hunt Game!")
    print("Find the treasure hidden on the board.")
    print_board(board, size)
    
    attempts = 0

    while attempts < max_attempts:
        try:
            guess_row = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter row (0-{size - 1}): "))
            guess_col = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter column (0-{size - 1}): "))
            
            if guess_row < 0 or guess_row >= size or guess_col < 0 or guess_col >= size:
                print("Invalid input. Please enter values within the board size.")
                continue
            
            distance = get_distance(treasure_row, treasure_col, guess_row, guess_col)
            
            if distance == 0:
                print("Congratulations! You found the treasure!")
                break
            elif distance <= 2:
                print("Very close!")
            elif distance <= 5:
                print("Close.")
            else:
                print("Far away.")
            
            board[guess_row][guess_col] = 'X'
            print_board(board, size)
            
            attempts += 1

        except ValueError:
            print("Invalid input. Please enter integer values.")
    
    if attempts == max_attempts:
        print("Game Over! You've used all your attempts.")
        print(f"The treasure was at ({treasure_row}, {treasure_col}).")

if __name__ == "__main__":
    play_game()
