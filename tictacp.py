board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def show(board):
    for i in range(0, 3):
        print(board[i])
    


sample_board = [
 [(0,0), (0,1), (0,2)],

 [(1,0), (1,1), (1,2)],

 [(2,0), (2,1), (2,2)]
]


for i in range(0, 3):
        print(sample_board[i])



def check_win(symbol):
    
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    
    for i in range(0, 3):
        if board[i] == [symbol, symbol, symbol]:
            return True
        if (
            board[0][i] == symbol and
            board[1][i] == symbol and
            board[2][i] == symbol
        ):
            return True
    
    return False
def check_draw():
        
        for row in board:
            if "" in row:
                return False
            
        return True
p = 0
while p != 1:
        
    k = 0
    while k != 1:
            
        print("Its X player Turn")
            
        x = int(input("Enter the row number:  "))
        y = int(input("Enter the column number:  "))
            
        if board[x][y] == "":
            board[x][y] = "X"
            break
        else:
            print("Position is Already Occupied")
                
    show(board)
    if check_win("X"):

        print("X Player Won !!!")
        break

    if check_draw():
        
        print("Match Draw")
        break
    
    
        
            
    j = 0
    while j != 1:
        print("Its O player turn")
            
        x = int(input("Enter the row number:  "))
        y = int(input("Ener the column number:  "))
            
        if board[x][y] == "":
            board[x][y] = "O"
            break
        else:
            print("Position is Already Occupied")
            
    show(board)
    if check_win("O"):

        print("O Player Won !!!")
        break

    if check_draw():
        
        print("Match Draw")
        break
        
        
            



