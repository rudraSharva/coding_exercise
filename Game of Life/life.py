#**********************************#
     ##      John Conway's     ##
#          Game of Life            #

#   Existence is just two states   #

#**********************************#

import time
import random
from csplot import *

# display the grid
def displayBoard(Board):
    d = {0:'white', 1:'black'}
    show(Board,d)

# count the live neighbours of a cell
def countLiveNeighbours(Board,row,column):
    count = 0
    for i in range(row-1,row+2):
        for j in range(column-1,column+2):
            if i==row and j==column:continue
            if Board[i][j] is 1: count += 1
    return count

# main logic for update logic 'Game of Life'
def updateNextLife(oldB,newB):
    width = len(oldB[0])
    height = len(oldB)
    for row in range(1,width-1):
        for column in range(1,height-1):
            count = countLiveNeighbours(oldB,row,column)
            if oldB[row][column] and (count<2 or count>3):
                newB[row][column] = 0
            elif oldB[row][column] is 0 and count == 3:
                newB[row][column] = 1
            else:
                newB[row][column] = oldB[row][column]

# reverse the updates
# dummy update function for test
def updateReversed(oldB,newB):
    width = len(oldB[0])
    height = len(oldB)
    for row in range(1,width-1):
        for column in range(1,height-1):
            if oldB[row][column] is 0:
                newB[row][column] = 1
            else:
                newB[row][column] = 0

# test random update function (dummy function)
# uses choice function to randomly select value from a sequence
def updateRandom(Board):
    width = len(Board[0])
    height = len(Board)
    for row in range(1,width-1):
        for column in range(1,height-1):
            Board[row][column] = random.choice([0,1])
    #displayBoard(Board)

# create the grid
def createBoard(rows,columns):
    board = [[0]*rows for i in range(columns)]
    return board

def life(rows, columns):
    """
    This is John Conway's Game of Life
    """
    board = createBoard(rows,columns)
    showAndClickInIdle(board) # user input for live cells

    while True: # run forever
        displayBoard(board) # show current B
        #time.sleep(0.002) # pause a bit
        oldB = board
        board = createBoard(rows, columns) #  creates a new board
        updateNextLife( oldB, board ) #  sets the new board correctly

# main function
if __name__ == '__main__':
    """
    How to run:
    1). python life.py (on command line)
    2). enter comma separated dimensions : 50,50 (for 50 by 50 grid)
    More description in README
    """
    x,y = map(int,raw_input("enter the dimensions of the board separated by comma: ").split(','))
    life(x,y)

