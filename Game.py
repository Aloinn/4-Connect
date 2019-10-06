import numpy as np

import guiOut as go
import DataSet as dt
import Algorithm as ag
import CPU as ai

if __name__ == "__main__":
    gamemode = int(input("Play against human[1] or CPU[2]? :"))

    # Creates a board
    board = np.zeros((6,7))
    go.printGuiBoard(board)
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
        go.printGuiBoard(board)

        #print(board)
        _y = dt.returnY()  # Returns the y of the most recent dropped in piece
        print(ag.check(player,board))
        # Alternates between players
        player = 2 if player == 1 else 1

