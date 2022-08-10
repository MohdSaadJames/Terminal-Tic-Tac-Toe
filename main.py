board = [[" ", "|", " ", "|", " "], [" ", "|", " ", "|", " "],
         [" ", "|", " ", "|", " "]]
posdone = []
pos = ""
def drawboard():
    for i in range(0, 3):
        print("   ", end="")
        for j in board[i]:
            print(j, end="  ")
        if i != 2:
            print("\n", "-----------------")
    print("\n")
def insertox(n,str):
    if n == 1:
      board[0][0]=str
    elif n == 2:
      board[0][2]=str
    elif n == 3:
      board[0][4]=str
    elif n == 4:
      board[1][0]=str
    elif n == 5:
      board[1][2]=str
    elif n==6:
      board[1][4]=str
    elif n==7:
      board[2][0]= str
    elif n==8:
      board[2][2] = str
    else:
      board[2][4]=str
print("Welcome to the Terminal-Tic-Tac-Toe game for two players!\n")

player1 = input('Who is taking "X"? ')
player2 = input('Who is taking "O"? ')

chance = True
drawboard()
def gameloop():
  global chance  
  if chance:
    print(f"{player1}'s turn!")
    pos = input("Pick a square from 1-9 where you want to place your \"X\"! ")
    try:
      int(pos)
    except:
      print("\nYou are disqualified for not following the rules.")
      print(f"{player2} wins! ")
      return
    if int(pos) > 9 or int(pos) < 1 and int(pos) not in posdone:
     print("\nYou are disqualified for not following the rules.")
     print(f"{player2} wins!")
     return
     posdone.append(int(pos))
    insertox(int(pos),"X")
    chance = not chance
    drawboard()
    gameloop()
  else:
    print(f"{player2}'s turn!")
    pos = input("Pick a square from 1-9 where you want to place your \"O\"! ")
    try:
      int(pos)
    except:
      print("\nYou are disqualified for not following the rules.")
      print(f"{player1} wins! ")
      return
    if int(pos) > 9 or int(pos) < 1 and int(pos) not in posdone:
     print("\nYou are disqualified for not following the rules.")
     print(f"{player1} wins!")
     return
     posdone.append(int(pos))
    insertox(int(pos),"O")
    chance = not chance
    drawboard()
    gameloop()
 
gameloop()
