board = [["","|","","|",""],["","|","","|",""],["","|","","|",""]]
def drawboard():
  for i in range(0,3):
    print("   ",end = "")
    for j in board[i]:
      print(j,end = "  ")
    if i != 2:
       print("\n","--------------")
  print("")

drawboard()