#strategy to make the game
# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check coloums
    # check diagnols
#check tie  
#flip player

board=[" - "," - "," - "," - "," - "," - "," - "," - "," - "]

game_still_going=True
#who won? or tie?
winner=None
#whose turn it is?
current_player= " X "

def display():
    print(board[0] + "|" +board[1] + "|" + board[2])
    print(board[3] + "|" +board[4] + "|" + board[5])
    print(board[6] + "|" +board[7] + "|" + board[8])

def play():

    #display initial board
    display()
    while game_still_going:
      handle_turn(current_player)
      check_if_game_over()
      flip_player()

    if winner== " X " or winner==" O ":
        print(winner +"won.")
    elif(winner==None):
        print("Tie.")

def handle_turn(player):
    print(player +"s turn")
    position=input("Choose a position from 1-9: ")

    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("Choose position from 1-9: ")
        
        position=int(position)-1 

        if board[position]==" - ":
            valid=True
        else:
            print("You cant go there.Go again")

    board[position]=player
    display()

def check_if_game_over():
    check_win()
    check_tie()

def check_win():
    #setting global variable
    global winner
    #check rows
    row_winner=check_rows()
    #check coloumns
    coloumn_winner=check_coloumns()
    #check diagnols
    diagnol_winner=check_diagnols()

    if row_winner:
        winner=row_winner

    elif coloumn_winner:
        winner=coloumn_winner

    elif diagnol_winner:
        winner=diagnol_winner
    else:
        winner=None
    return

def check_rows():
    global game_still_going
    row1=board[0]==board[1]==board[2]!=" - "
    row2=board[3]==board[4]==board[5]!=" - "
    row3=board[6]==board[7]==board[8]!=" - "

    if row1 or row2 or row3:
        game_still_going=False
    #return the winner X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_coloumns():
    global game_still_going
    column1=board[0]==board[3]==board[6]!=" - "
    column2=board[1]==board[4]==board[7]!=" - "
    column3=board[2]==board[5]==board[8]!=" - "

    if column1 or column2 or column3:
        game_still_going=False
    #return the winner X or O
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diagnols():
    global game_still_going
    diagnol1=board[0]==board[4]==board[8]!=" - "
    diagnol2=board[2]==board[4]==board[6]!=" - "

    if diagnol1 or diagnol2:
        game_still_going=False
    #return the winner X or O
    if diagnol1:
        return board[0]
    elif diagnol2:
        return board[2]
    return

def check_tie():
    global game_still_going
    if " - " not in board:
        game_still_going=False
    return

def flip_player():
    global current_player
    if current_player==" X ":
        current_player=" O "
    elif current_player==" O ":
        current_player=" X "
    return

play()