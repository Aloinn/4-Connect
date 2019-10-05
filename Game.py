import numpy as np
import guiOut as go
import DataSet as dt
import Algorithm as ag

# Creates a board
board = np.zeros((6,7))

_in = int(input("In:"))
board   = dt.update(_in, board)    # Updates the board to user's input, returns new board
_y = dt.returnY() # Returns the y of the most recent dropped in piece
column  = go.read(board)     # Reads the new board and compares to old board, returning column number
ag.check(_in, _y, board)      # From the column number, check board to see if win condition met return T/F
