import numpy as np

import guiOut as go
import DataSet as dt
import Algorithm as ag
import CPU as ai

if __name__ == "__main__":
    gamemode = int(input("Play against human[1] or CPU[2]? :"))
    # Creates a board
    board = np.zeros((6,7))

    # Creates a CPU
    if gamemode == 2: cpu = ai.AI(2)

    play = True
    player = 1

    while play:
        if player == 2 and gamemode == 2:
            _in = cpu.play(board)
        else:
            _in = int(input("In:"))
            if gamemode == 2: cpu.updatemap([0,_in, -1],1)

        board = dt.update(_in, player, board)    # Updates the board to user's input, returns new board

        #_y = dt.returnY() # Returns the y of the most recent dropped in piece
        #column  = go.read(board)     # Reads the new board and compares to old board, returning column number
        print(board)

        #play = ag.check(_in, _y, player, board)      # From the column number, check board to see if win condition met return T/F
        # Alternates between players
        player = 2 if player == 1 else 1

