board = [[" ", "|", " ", "|", " "], [" ", "|", " ", "|", " "],
         [" ", "|", " ", "|", " "]]
posdone = []
pos = ""
col1 = []
col2 = []
col3 = []
row1=[]
row2=[]
row3=[]
diagonal1=[]
diagonal2=[]
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
      col1.append(str)
      row1.append(str)
      diagonal1.append(str)
    elif n == 2:
      board[0][2]=str
      col2.append(str)
      row1.append(str)
      

    elif n == 3:
      board[0][4]=str
      col3.append(str)
      row1.append(str)
      diagonal2.append(str)

    elif n == 4:
      board[1][0]=str
      col1.append(str)
      row2.append(str)
      

    elif n == 5:
      board[1][2]=str
      col2.append(str)
      row2.append(str)
      diagonal1.append(str)
      diagonal2.append(str)
    elif n==6:
      board[1][4]=str
      col3.append(str)
      row2.append(str)
      

    elif n==7:
      board[2][0]= str
      col1.append(str)
      row3.append(str)
      diagonal2.append(str)

    elif n==8:
      board[2][2] = str
      col2.append(str)
      row3.append(str)
      

    else:
      board[2][4]=str
      col3.append(str)
      row3.append(str)
      diagonal1.append(str)

print("Welcome to the Terminal-Tic-Tac-Toe game for two players!\n")

player1 = input('Who is taking "X"? ')
player2 = input('Who is taking "O"? ')
print("\n")
winner = ""

print("Enter quit anytime to 'quit', mind you it will make the other player win.\n\n")

def gamecheck():
    global winner
    if len(col1)==3 and len(set(col1)) == 1:
        winner = col1[0]
    elif len(col2)==3 and len(set(col2))==1:
        winner = col2[0]
    elif len(col3)==3 and len(set(col3)) == 1:
        winner = col3[0]
    elif len(row1)==3 and len(set(row1)) == 1:
        winner = row1[0]
    elif len(row2)==3 and len(set(row2)) == 1:
        winner = row2[0]
    elif len(row3)==3 and len(set(row3)) == 1:
        winner = row3[0]
    elif len(diagonal1)==3 and len(set(diagonal1))==1:
        winner = diagonal1[0]
    elif len(diagonal2)==3 and len(set(diagonal2)) == 1:
        winner == diagonal2[0]
    elif len(posdone) == 9:
        winner = "Tie"


chance = True
drawboard()
def gameloop():
  global posdone
  global winner
  global chance  
  if chance:
    print(f"{player1}'s turn!")
    pos = input("Pick a square from 1-9 where you want to place your \"X\"! ")
    if pos == "quit":
        print(f"\n{player2} won the game since you quit.")
        return
    try:
      int(pos)
    except:
      print("\nYou are disqualified for not following the rules.")
      print(f"{player2} wins! ")
      return
    if int(pos) in posdone:
        print("There's already a 'X' or 'O' at that place, you're disqaulified for the same.")
        return
        print(f"{player2} wins! ")
    if int(pos) > 9 or int(pos) < 1:
     print("\nYou are disqualified for not following the rules.")
     print(f"{player2} wins!")
     return
    posdone.append(int(pos))
    insertox(int(pos),"X")
    chance = not chance
    drawboard()
    gamecheck()
    if winner == "X":
        print(f"Congratulations! {player1} won the match!\n\n")
        return
    elif winner == "Tie":
        print("The game resulted in a tie.\n\n")
        return
    gameloop()
  else:
    print(f"{player2}'s turn!")
    pos = input("Pick a square from 1-9 where you want to place your \"O\"! ")
    if pos == "quit":
        print(f"\n{player1} won the game since you quit.")
        return
    try:
      int(pos)
    except:
      print("\nYou are disqualified for not following the rules.")
      print(f"{player1} wins! ")
      return
    if int(pos) in posdone:
        print("There's already a 'X' or 'O' at that place, you're disqaulified for the same.")
        print(f"{player1} wins! ")
        return
    if int(pos)>9 or int(pos)<1:
     print("\nYou are disqualified for not following the rules.")
     print(f"{player1} wins!")
     return
    posdone.append(int(pos))
    insertox(int(pos),"O")
    chance = not chance
    drawboard()
    gamecheck()
    if winner == "O":
        print(f"Congratulations! {player2} won the match!\n\n")
        return
    elif winner == "Tie":
        print("The game resulted in a tie.\n\n")
        return

    gameloop()
 
gameloop()
