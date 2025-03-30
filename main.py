import copy
import random

initboard = [["_", "_", "_"],
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
    
    return False
    # look at all 8 possible winning spots and see if its close to filling any 8
    # if we are close to filling one (one spot away) then we will place there to win
    # if they are close we will block them as long as we arent close
    # if neither are close we will go for any random possible winning spot
def minimax(board, player, bot, turn):
    
    new_board = copy.deepcopy(board)
    if win(board, player, bot) == player:
        return -10 + turn, None
    elif win(board, player, bot) == bot:
        return 15 - turn, None
    elif win(board, player, bot) == "tie":
        return 5, None
    
    best_points = float('-inf') if turn % 2 == 1 else float('inf')
    best_move = None
    possible_moves = []
    for x in range(3):
        for y in range(3):
            if new_board[x][y] == "_":
                if turn % 2 == 1:
                    new_board[x][y] = bot
                else:
                    new_board[x][y] = player
                print((x,y))
                possible_moves.append((x, y))
                # prettyBoard(new_board)
                score, _ = minimax(new_board, player, bot, turn + 1)
                new_board[x][y] = "_"
                print(f"Evaluating move ({x}, {y}) for {'bot' if turn % 2 == 1 else 'player'}: score = {score}")
                
                if turn % 2 == 1:
                    if score >= best_points:
                        best_points = score
                        best_move = (x, y)
                else:
                    if score < best_points:
                        best_points = score
                        best_move = (x, y)

                # print(best_points)
        if turn <= 2:
            best_points = 0
            
            best_move = random.choice(possible_moves)
            return best_points, best_move
    # print(f"Best move for {'bot' if turn % 2 == 1 else 'player'}: {best_move} with score = {best_points}")
    return best_points, best_move

def get_move(board, player):
    while True:
        print(f"{player}'s turn:")
        try:
            row = int(input("Choose a row (1-upper, 2-middle, 3-lower): ")) - 1
            col = int(input("Choose a column (1-first, 2-second, 3-third): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == "_":
                return row, col
            else:
                print("Spot already taken. Please enter a new spot.")
        else:
            print("Invalid row or column. Please choose numbers between 1 and 3.")

def tictactoe(board, player, bot):
    turn = 0
    winner = False
    while turn < 9 and winner == False:
        print("Current Board:")
        prettyBoard(board)
        if win(board, player, bot) != False:
            print("Game over!")
            if win(board, player, bot) == "tie":
                print("Game ended with a tie with board:")
                prettyBoard(board)
            elif win(board, player, bot) == player:
                print("Game ended with player win with board:")
                prettyBoard(board)
            elif win(board, player, bot) == bot:
                print("Game ended with bot win with board:")
                prettyBoard(board)
            break
        if turn % 2 == 0:
            row, col = get_move(board, player)
            board[row][col] = player
            turn += 1
            print("New Board:")
            prettyBoard(board)
        elif turn % 2 == 1:
            score, rowcol = minimax(board, player, bot, turn)
            board[rowcol[0]][rowcol[1]] = bot
            turn += 1
            print(f"Bot chose place {rowcol[0]}, {rowcol[1]} with score of {score}.")


# print(minimax(initboard, player, bot, 1))

tictactoe(initboard, player, bot)