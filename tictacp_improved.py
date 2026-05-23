"""
Tic-Tac-Toe Game
Two-player game where X and O take turns marking a 3x3 board
"""

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]


def show(board):
    """Display the current board state"""
    print("\n")
    for i in range(3):
        print(board[i])
    print()


def check_win(symbol):
    """Check if the given symbol has won"""
    # Check diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    
    # Check rows and columns
    for i in range(3):
        # Check row
        if board[i] == [symbol, symbol, symbol]:
            return True
        # Check column
        if (
            board[0][i] == symbol and
            board[1][i] == symbol and
            board[2][i] == symbol
        ):
            return True
    
    return False


def check_draw():
    """Check if the board is full (draw condition)"""
    for row in board:
        if "" in row:
            return False
    return True


def get_valid_move(player):
    """Get a valid move from the player with input validation"""
    while True:
        try:
            x = int(input(f"Its {player} player turn. Enter row number (0-2): "))
            y = int(input(f"Enter column number (0-2): "))
            
            # Validate range
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Invalid position! Please enter numbers between 0 and 2.")
                continue
            
            # Check if position is occupied
            if board[x][y] != "":
                print("Position is already occupied! Try another position.")
                continue
            
            return x, y
        
        except ValueError:
            print("Invalid input! Please enter integers only (0-2).")


def play_game():
    """Main game loop"""
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns entering row and column numbers (0-2)")
    show(board)
    
    while True:
        # X player turn
        x, y = get_valid_move("X")
        board[x][y] = "X"
        show(board)
        
        if check_win("X"):
            print("🎉 X Player Won!!!")
            break
        
        if check_draw():
            print("🤝 It's a Draw!")
            break
        
        # O player turn
        x, y = get_valid_move("O")
        board[x][y] = "O"
        show(board)
        
        if check_win("O"):
            print("🎉 O Player Won!!!")
            break
        
        if check_draw():
            print("🤝 It's a Draw!")
            break


if __name__ == "__main__":
    play_game()
