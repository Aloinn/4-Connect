import numpy as np
import guiOut as go
import DataSet as dt
import Algorithm as ag

"""Game"""
# Creates a board
board = np.zeros((6,7))

"""JonathanIsHere"""

"""Ricc"""
def getBoard():
    return board

"""Alain"""
_in = int(input("In:"))
board   = dt.update(_in, board)    # Updates the board to user's input, returns new board
column  = go.read(board)     # Reads the new board and compares to old board, returning column number
ag.check(column,board)      # From the column number, check board to see if win condition met return T/F
