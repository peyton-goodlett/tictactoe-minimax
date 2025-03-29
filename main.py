import copy

initboard = [["x", "_", "o"],
         ["x", "o", ""],
         ["_", "_", "_"]]
player = "x"
bot = "o"
def prettyBoard(board):
    rows = len(board)
    print("  1 2 3")
    for i in range(rows):
        print(f"{i+1} " + board[i][0] + "|" + board[i][1] + "|" + board[i][2])
    
def win(board, player, bot):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return player
        if all(board[i][j] == bot for j in range(3)) or all(board[j][i] == bot for j in range(3)):
            return bot
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return player
    if all(board[i][i] == bot for i in range(3)) or all(board[i][2 - i] == bot for i in range(3)):
        return bot
    
    if all(cell != "_" for row in board for cell in row):
        return "tie"
    
    return None
    # look at all 8 possible winning spots and see if its close to filling any 8
    # if we are close to filling one (one spot away) then we will place there to win
    # if they are close we will block them as long as we arent close
    # if neither are close we will go for any random possible winning spot
def minimax(board, player, bot, turn):
    new_board = copy.deepcopy(board)
    if win(board, player, bot) == player:
        return -10, None
    elif win(board, player, bot) == bot:
        return 10, None
    
    
    best_points = float("inf") if turn % 2 == 1 else float("-inf")
    best_move = None
    for x in range(3):
        for y in range(3):
            if new_board[x][y] == "_":
                if turn % 2 == 1:
                    new_board[x][y] = bot
                else:
                    new_board[x][y] = player
                prettyBoard(new_board)
                score, _ = minimax(new_board, player, bot, turn+1)
                new_board[x][y] = "_"
                print(f"Evaluating move ({x}, {y}) for {'bot' if turn % 2 == 1 else 'player'}: score = {score}")
                if turn % 2 == 1:
                    if score >= best_points:
                        best_points = score
                        best_move = (x, y)
                else:
                    if score <= best_points:
                        best_points = score
                        best_move = (x, y)
                print(best_points)
    print(f"Best move for {'bot' if turn % 2 == 1 else 'player'}: {best_move} with score = {best_points}")
    return best_points, best_move
print(minimax(initboard, player, bot, 3))