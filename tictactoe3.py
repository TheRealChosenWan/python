#############
#Board -done
#Starting playing game
#Who starts? Turn?
#player marker X or O
#player needs to be able to place a marker at location on the board <--kinda
#determine winner or tie or continue
#flip player turn
#Restart?
###################

#####GLOBAL VAR##############
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

Game_On = True   
current_player ="Player X"

###############################

def play_game():
  global board
  global Game_On
  display_board()
  while Game_On:
    player_X_choice()
    if Game_On:
      player_O_choice()
  while not Game_On:
    
    restart_question = input("Do you want to restart? Y/N").upper()
    if restart_question == "Y":
      for i in range(len(board)):
        board[i] = "-"
      Game_On = True
      play_game()
    else:
      print("GG")
      break
    


def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])



def player_X_choice():
    
    position = input("Choose a position 1-9: ")

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Choose a position 1-9: ")


    position = int(position)-1
    if board[position] != "-":
      print("Please choose another space")
      display_board() 
      player_X_choice()
    
    else: 
      board[position] = "X" #Either X or O
      display_board() 
    check_win()
    check_tie()

def player_O_choice():
    position = input("Choose a position 1-9: ")

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Choose a position 1-9: ")
    
    position = int(position)-1
    if board[position] != "-":
      print("Please choose another space")
      display_board() 
      player_O_choice()
    
    else: 
      board[position] = "O" #Either X or O
      display_board() 
    check_win()
    check_tie()
def check_win():
  check_row()
  check_column()
  check_diag()
  

def check_row():
  global Game_On
  row_1=board[0]==board[1]==board[2]!="-" 
  row_2=board[3]==board[4]==board[5]!="-"    
  row_3=board[6]==board[7]==board[8]!="-"      
  if row_1 or row_2 or row_3:
    Game_On = False
    if row_1:
      print(board[0]+" won")
    elif row_2:
      print(board[3]+" won")
    elif row_3:
      print(board[6]+" won")
    

def check_column():
  global Game_On
  column_1=board[0]==board[3]==board[6]!="-" 
  column_2=board[1]==board[4]==board[7]!="-"    
  column_3=board[2]==board[5]==board[8]!="-"      
  if column_1 or column_2 or column_3:
    Game_On = False
    if column_1:
      print(board[0]+" won")
    elif column_2:
      print(board[1]+" won")
    elif column_3:
      print(board[2]+" won")

def check_diag():
  global Game_On
  diag_1=board[0]==board[4]==board[8]!="-" 
  diag_2=board[6]==board[4]==board[2]!="-"        
  if diag_1 or diag_2 :
    Game_On = False
    if diag_1:
      print(board[0]+" won")
    elif diag_2:
      print(board[6]+" won")

def check_tie():
  global Game_On
  if "-" not in board:
    print("Tie.")
    Game_On = False




play_game()

