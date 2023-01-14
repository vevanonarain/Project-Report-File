import random

def display_board(board):  #Create a game board
    
    print("\n"*100)

    print(" "+board[1]+" | "+board[2]+" | "+""+board[3]+" ")
    print("-----------")
    print(" "+board[4]+" | "+board[5]+" | "+""+board[6]+" ")
    print("-----------")
    print(" "+board[7]+" | "+board[8]+" | "+""+board[9]+" ")

def player_input(): #Decide player markers
    
    player1_marker = "null"
    player2_marker = "null"
    marker_option_list = ["X","O"]
    
    while player1_marker not in marker_option_list:
            player1_marker = input("Player 1, would you like to be 'X' or 'O'? ").upper()
            if player1_marker not in marker_option_list:
                print("Sorry, invalid selection. Please input 'X' or 'O'")
            else:
                break
            
    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"
    
    return(player1_marker,player2_marker)

def place_marker(board, marker, position): #Make a move
    
    board[position] = marker

def win_check(board, mark): #Check if either player has won
    
    #ROW CHECKS
        return ((board[1] == mark and board[2] == mark and board[3] == mark) or
                (board[4] == mark and board[5] == mark and board[6] == mark) or
                (board[7] == mark and board[8] == mark and board[9] == mark) or
    
    #COLUMN CHECKS
                (board[1] == mark and board[4] == mark and board[7] == mark) or
                (board[2] == mark and board[5] == mark and board[8] == mark) or
                (board[3] == mark and board[6] == mark and board[9] == mark) or
    
    #DIAGONAL
                (board[1] == mark and board[5] == mark and board[9] == mark) or
                (board[3] == mark and board[5] == mark and board[7] == mark))

def choose_first(): #randomly decide who starts
    
    first_player = random.randint(1,2)
    
    if first_player == 1:
        return "Player 1"
    elif first_player == 2:
        return "Player 2"
        
def space_check(board, position): #check if the position is empty
    
    return board[position] == " "
    
def full_board_check(board): #check if the board is full (tie check)
    
    marker_options = ["X", "O"]
    fill_counter = 0
    
    for position in board:
        if position == "X" or position == "O":
            fill_counter += 1
        else:
            pass
    return fill_counter == 9
    
def player_choice(board): #choose next move
    position = int(input("Choose your next position: (1-9) "))
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        print("Invalid selection. Position is either not an option or already taken.")
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay(): #Decide if you want to play again
    
    response = input("Would you like to play again (Yes or No)?: ").lower()
    replay_options = ["yes", "no"]
    
    while True:
        if response not in replay_options:
            print("Invalid input, please type 'Yes' or 'No'.")
            response = input("Would you like to play again (Yes or No)?: ").lower()
            continue
        elif response == "yes":
            return True
        else:
            return False


#While loop to keep running the game
print("Welcome to Knots & Crosses!")

while True:
    
    #Play The Game
    
    #Set Everything Up (Board, whos first and marker choice)
    the_board = [" "]*10  #Empty blank board
    player1_marker, player2_marker = player_input()  #Tuple unpacking to assign markers
    
    turn = choose_first() #Decides who is going to play first
    print(f"\n{turn} will play first")
    
    play_game = input("Ready to play? 'Yes' or 'No': ").lower()
    
    if play_game == "yes":
        game_on = True
    else:
        game_on = False
                        
    
    #Game Play
    
    while game_on == True:
    
        #Player 1's turn
 
        if turn == "Player 1":
            
                #Show the board
                display_board(the_board)
                
                #Choose a position
                print("\nPlayer 1")
                position = player_choice(the_board)
                
                #Place the marker on the position
                place_marker(the_board,player1_marker,position)
                
                #Check if they won
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print("PLAYER 1 WINS!")
                    game_on = False
                
                #or check if there is a tie
                else: 
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("THE GAME IS A TIE!")
                        game_on = False
                
                #No tie or no win next players turn
                    else:
                        turn = "\nPlayer 2 plays first"
    
    
        #Player 2's turn
    
        else:
                #Show the board
                display_board(the_board)
                
                #Choose a position
                print("\nPlayer 2")
                position = player_choice(the_board)
                
                #Place the marker on the position
                place_marker(the_board,player2_marker,position)
                
                #Check if they won
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print("PLAYER 2 WINS!")
                    game_on = False
                
                #or check if there is a tie
                else: 
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("THE GAME IS A TIE!")
                        game_on = False
                
                #No tie or no win next players turn
                    else:
                        turn = "Player 1"
          
#break out of game while loop on replay()

    if not replay():
        break


