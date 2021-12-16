import pygame
import numpy as np

ROW_LENGTH,COLUMN_LENGTH=(7,7)
COLORS={"R":"red","G":"green"}
PLAYERS={"R":'player 1',"G":'player 2'}

Board=np.full((7,7),"0")

def fillRed(pos):
    arr=Board[pos][::-1]
    for index,i in enumerate(arr):
        if(i=="0"):
            Board[pos,6-index]="R"
            return
        
    print("illegal move")

def fillGreen(pos):
    arr=Board[pos][::-1]
    for index,i in enumerate(arr):
        if(i=="0"):
            Board[pos,6-index]="G"
            return
    print("illegal move")

def printBoard():
    board = np.transpose(Board)
    for row,i in enumerate(board):
        for column,j in enumerate(board[row]):
            print(f"  {board[row,column]}  ",end="")
        print("\n",end="")


def checkBoard():
    for row in Board:
        r="".join(row)
        if("RRRR" in r):
            return "R"
        elif("GGGG" in r):
            return "G"

    for row in np.transpose(Board):
        r="".join(row)
        if("RRRR" in r):
            return "R"
        elif("GGGG" in r):
            return "G"


    return "0"


player="R"

while(1):
    
    p=int(input(f"enter position (1-7) {PLAYERS[player]} : "))
    if player=="R":
        fillRed(p-1)
    else:
        fillGreen(p-1)

    if checkBoard()=="R":
        print("Red wins")
        break
    elif checkBoard()=="G":
        print("Green wins")
        break

    if player == "R":
        player="G"
    else:
        player="R"

    printBoard()

    

