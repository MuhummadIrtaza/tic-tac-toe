
board = ("""1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9""")

def pr_board(board):
    print(board)




def check_winner(board_2d):

    #checking rows
    for row in board_2d:    
        result = False
        if all(cell == row[0] for cell in row):
            return True , row[0]
        
    #checking columns 
    for col in range(3):
        if all (row[col] == board_2d[0][col] for row in board_2d):
            return True , board_2d[0][col]
    # checking diagonals 
    if all(board_2d[i][i] == board_2d[0][0] for i in range(3)) or \
    all(board_2d[i][2 - i] == board_2d[0][2] for i in range(3)):
        return True, board_2d[1][1]
    #No winner
    return False , None


def checkdraw(board):
    #if any cell is not numeric that means there is a draw
    return all(not cell.isnumeric() for cell in board)

def main_loop(board):
    ct_x = 0
    count = 0
    ct_y = 0 
    q = True
    pr_board(board)



    #Converting the string into 2d array
    board_rows = board.split('\n')
    board_2d = []
    board_2d = [row.split(' | ') for row in board_rows]

    #counter
    while q == True:
        # Checking Turns 
        if count % 2 == 0:
            x = input("It is X's turn: ")
            if x.isnumeric():
                for i in board:
                    if i == x:
                        board = board.replace(i , "X")
                        print(board)
                        count += 1
            #Check if input in numeric
            if x.isnumeric() != True:
                print("invalid Input")
        #check winner function after every turn
        winner , symbol = check_winner(board_2d)
        if winner:
            ct_x += 1
            print(f"{symbol} won {ct_x} times")
            
            break

        if count % 2 != 0:
            o = input ("It is O's turn: ")
            for i in board:
                if i == o:
                    board = board.replace(i , "O")
                    print(board)
                    count += 1
            if o.isnumeric() != True:
                print("invalid Input")

        #check winner after every O turn
        winner , symbol = check_winner(board)
        if winner:
            ct_y += 1
            print(f"{symbol} won {ct_y} times")
            break

        #check draw
        draw = checkdraw(board)
        if draw:
            print("It is a draw")
            break

while True:
    X = input ("Do you want to play  Y or N")
    if X == "y" or X == "Y":
        main_loop(board)
    else:
        print("Bye!")
        break
