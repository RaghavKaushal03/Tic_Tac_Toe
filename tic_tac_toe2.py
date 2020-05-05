board =["_","_","_",
        "_","_","_",
        "_","_","_"]
game_still_going = True
winner = None
current_player = "X"
def display_board():
  print(board[0] + " | "+ board[1] + " | "+ board[2])
  print(board[3] + " | "+ board[4] + " | "+ board[5])
  print(board[6] + " | "+ board[7] + " | "+ board[8])
def play_game():
  display_board()
  while game_still_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  if winner=="X" or winner=="O":
    print(winner + " Won.")
  elif winner== None:
    print("Tie.")
def handle_turn(player):
  print(player + "'s turn.")
  position = input("Choose a number between 1 to 9: ")
  valid=False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a number between 1 to 9: ")
    position = int(position)-1
    if board[position] == "_":
      valid=True
    else:
      print("You cant go there.Go again")
  board[position]= player
  display_board()
def check_if_game_over():
  check_for_winner()
  check_if_tie()
def check_for_winner():
  global winner 
  row_winner=check_rows()
  coloumn_winner=check_coloumn()
  diagonal_winner= check_diagonals()
  if row_winner:
    winner = row_winner
  elif coloumn_winner:
    winner = coloumn_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return
def check_rows():
  global game_still_going
  row_1 = board[0]==board[1]==board[2] != "_"
  row_2 = board[3]==board[4]==board[5] != "_"
  row_3 = board[6]==board[7]==board[8] != "_"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return
def check_coloumn():
  global game_still_going
  coloumn_1 = board[0]==board[3]==board[6] != "_"
  coloumn_2 = board[1]==board[4]==board[7] != "_"
  coloumn_3 = board[2]==board[5]==board[8] != "_"
  if coloumn_1 or coloumn_2 or coloumn_3:
    game_still_going = False
  if coloumn_1:
    return board[0]
  elif coloumn_2:
    return board[1]
  elif coloumn_3:
    return board[2]
  return
def check_diagonals():
  global game_still_going
  diagonal_1 = board[0]==board[4]==board[8] != "_"
  diagonal_2 = board[2]==board[4]==board[6] != "_"
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return
def check_if_tie():
  global game_still_going
  if "_" not in board:
    game_still_going = False
  return
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player =="O":
    current_player = "X"
  return
play_game()