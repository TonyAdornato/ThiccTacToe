"""
This is the program for the game Thicc Tac Toe
It allows the player to play a game of tic tac to on a grid that is 3x3 or larger
Created by Tony Adornato
"""

def get_board_size():
    print("Welcome to Thicc Tac Toe.")
    print("The game that lets you play tic tac toe on any size grid.")
    grid_size = 0
    while True: 
        try:
            grid_size = int(input("Enter a grid size: "))
            if grid_size <= 0:
                print("Yes. You're very clever.")
            elif grid_size <= 2:
                print("That grid is not very thi" + ("c" * grid_size) + ".")
            elif grid_size == 3:
                print("Ah! An old fashioned.")
                return grid_size
            else:
                print("That's Thi" + ("c" * grid_size) + ".")
                return grid_size
        except ValueError:
            print("Please enter an integer number.")  

def generate_board(size):
    new_board = []
    for x in range(1, size+1):
        for y in range(1, (size+1)):
            new_board.append([x, y , " "])
    return new_board


def draw_board(size, board):
    numbers = [str("%3d" % num) for num in range(1, size+1)]
    print("    " + " ".join(numbers))

    res = [(" " + entry[2]+ " ") for entry in board]
    start = 0
    end = size
    for x in range(1, size+1):
        print(str("%3d" % x) + ": " + "|".join(res[start:end]))
        start += size
        end +=size


def get_square(board, indices, values):
    #want pos of item having [row, column] in positions 0 and 1
    for pos, k in enumerate(board):
        match = True
        for i in indices:
            if k[i] != values[i]:
                match = False
                break;
        if (match):
            return pos
    raise ValueError("board.index(x): x not in list")

def get_move(size, board, symbol):
    print(str(symbol) + " move")
    while True: 
        try:
            row = int(input("Enter row: "))
            column = int(input("Enter col: "))
            if row <= size and column <= size:
                indices = [0,1]
                values = [row,column]
                square = get_square(board, indices, values)
                if board[square][2] != " ":
                    print("That square is already occupied")
                    print("Try annother square.")
                else:
                    board[square][2] = symbol
                    break;
            else:
                print("Enter row and column values that are less than or equal to " + str(size))
        except ValueError:
            print("Please enter integer numbers.")


def check_win_state(size, board):

    #check rows and columns
    for i in range(1, size+1):
        for g in range(0,2):
            check_list = [t[2] for t in board if t[g] == i]
            if check_list[0] != " " and all(x == check_list[0] for x in check_list):
                print(str(check_list[0]) + " wins!")
                return True

    #check diagonal
    check_diag = [t[2] for t in board if t[0] == t[1]]
    if check_diag[0] != " " and all(x == check_diag[0] for x in check_diag):
        print(str(check_diag[0]) + " wins!")
        return True

    #check reverse diagonal
    check_reverse = []
    for i in range(1,size+1):
        row = i
        col = (size+1)-row
        check_reverse += [t[2] for t in board if t[0] == row and t[1] == col]
    if check_reverse[0]!=" " and all(x == check_reverse[0] for x in check_reverse):
        print(str(check_list[0]) + " wins!")
        return True

    #check draw
    empty_index = [board.index(x) for x in board if x[2] == " "]
    if len(empty_index) == 0:
        print("It's a draw!")
        return True

    #No one has won. Continue game
    return False
    
def main():
    while True:
        board_size = get_board_size()
        board = generate_board(board_size)
        draw_board(board_size, board)
        while True:
            #player 1 move
            get_move(board_size, board, "X")
            draw_board(board_size, board)
            win = check_win_state(board_size, board)
            if win == True:
                #play_again = input("Would you like to play again? y/n: ")
                #if 
                break;
            
            #player 2 move
            get_move(board_size, board, "O")
            draw_board(board_size, board)
            win = check_win_state(board_size, board)
            if win == True:
                break;
        ####TODO
        # make this a loop that only accepts y or n
        play_again = str(input("Would you like to play again? (y/n): "))
        if play_again == "y":
            continue
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
