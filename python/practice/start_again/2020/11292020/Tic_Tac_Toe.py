#Create a Tic Tac Toe game.
#Two players should play the game 
#The board should printed out every time a player makes a move 
#You should be accept input from player position and place a symbol on the board 
#Accept user input from user 
#test_board = ['X','0','X','O','X','O','X','O','X']
#Solution :-
#https://bennettgarner.medium.com/tic-tac-toe-series-4-game-over-making-moves-permanent-23bca3b40ce0
def main():
    board = [["_" for _ in range (3)] for _ in range(3)]
    is_x = True
    game_over = False
    while not game_over:
        player = "X" if is_x else "0"
        display_board(board)
        try: 
            place_marker (convert_selection(accept()), player, board )
        except ValueError:
            print ("Sorry, Please select a number between 1 - 9 that is unoccupied ")
            continue
        game_over = is_win(board) or is_draw(board)
        is_x = not is_x
    #display_board(board)
def convert_selection(selection):
    selection -= 1
    return (selection // 3 , selection % 3)

def place_marker (selection, player, board):
    i, j = selection
    if board[i][j] == "_":
        board[i] [j] = player
    else:
        raise ValueError
        
def display_board(board):
    for row in board :
        print (row)

def accept():
    #Print Board 
    selection = int (input("Enter a square : "))
    if not 1 <= selection <= 9 :
        raise ValueError
    return selection
def is_draw (board):
    for row in board:
        for val in row:
            if val == "_":
                return False
    print ("Draw! No more moves!")
    return True
def is_win(board):
    winner = None
    for i in range(3):
        #Horizontal 
        if board[i][0] == board[i][1] == board [i][2] and board [i][0] != "_":
            winner = board [i][0]
            break
        #Vertical 
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board [0][i]
            break 
        #Diagonal
        if board [1][1] != "_":
            if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board [1][1] == board[2][0]):
                winner = board [1][1]
        if winner is not None:
            display_board(board)
            print ("{}is the winner! ".format(winner))
            return True 
        return False    
if __name__ == "__main__":
    main()