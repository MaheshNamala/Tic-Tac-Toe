import numpy as np
import random 
from time import sleep


#creating empty board
def e_b():
    board=np.array(
                     [[0,0,0],
                     [0,0,0],
                     [0,0,0]]
                     )
    return board


#search empty row
def s_e_r(board):
    l=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                l.append((i,j))
    return l

#Random player
def random_p(board,player):
    select=s_e_r(board)
    current_location=random.choice(select)
    board[current_location]=player
    return board




#checking the horizontal rows for a winner

def row_w(board,player):
    for i in range(len(board)):
        win=True
        for j in range(len(board)):
            if board[i,j]!=player:
                win=False
                continue
        if win==True:
            return win
    return win


#checking the vertical column for a winner

def col_w(board,player):
    for i in range(len(board)):
        win=True
        for j in range(len(board)):
            if board[j,i]!=player:
                win=False
                continue
        if win==True:
            return win
    return win



#checking the diagonol rows for a winner

def diag_w(board,player):
        win=True
        j=0
        for i in range(len(board)):
            if board[i,i]!=player:
                win=False
        if win:
            return win
        win=True
        if win:
            for i in range(len(board)):
                j=len(board)-1-i
                if board[i,j]!=player:
                    win=False
        return win

#Evaluating winner
def eval_win(board):
    win=0
    for player in [1,2]:
        if row_w(board,player) or col_w(board,player) or diag_w(board,player):
            win=player
        if np.all(board!=0) and win ==0:
            win=-1
        return win

#main function
def tic_tac_toe():
    board=e_b()
    win=0
    counter=0
    print(board)
    sleep(2)
    while win == 0:
        for player in [1,2]:
            brd=random_p(board,player)
            print("board after"  +str(counter)  +"move","\n")
            print(brd)
            sleep(1)
            counter+=1
            win=eval_win(brd)
            if win !=0:
                break
    return win
print("winner is player:"+str(tic_tac_toe()))