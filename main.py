board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]
player = "x"
bot = "o"
def prettyBoard(board):
    rows = len(board)
    print("  1 2 3")
    for i in range(rows):
        print(f"{i+1} " + board[i][0] + "|" + board[i][1] + "|" + board[i][2])
    
def win(board, player, bot):
    for row in board:
        if all(cell == player for cell in row):
            return True, player
        elif all(cell == bot for cell in row):
            return True, bot
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True, player
        elif all(board[row][col] == bot for row in range(3)):
            return True, bot
        
    if all(board[i][i] == player for i in range(3)):
        return True, player
    if all(board[i][i] == bot for i in range(3)):
        return True, bot
    if all(board[i][2 - i] == player for i in range(3)):
        return True, player
    if all(board[i][2 - i] == bot for i in range(3)):
        return True, bot
    for row in board:
        r=0
        if "_" in row:
            r += 1
            pass
    if r == 0:
        return False, "Tie"
    
    return False, None
    
def minimax(board, player, bot, turn):
    copy = board
    # look at all 8 possible winning spots and see if its close to filling any 8
    # if we are close to filling one (one spot away) then we will place there to win
    # if they are close we will block them as long as we arent close
    # if neither are close we will go for any random possible winning spot