import numpy as np


def test(n):
    """
    :param n: test number, 1 to 4
    1 is horizontal 4 in a row
    2 is vertical 4 in a row
    3 is rightward diagonal
    4 is leftward diagonal
    :returns: the board
    """
    board1 = np.zeros((6, 7))
    if n == 1:  # horizontal row
        for i in range(1, 5):
            board1[3, i] = 1
    elif n == 2:  # vertical row
        for i in range(1, 5):
            board1[i, 3] = 1
    elif n == 3:  # bottom left to top right
        for i in range(4, 0, -1):
            board1[i, 5 - i] = 1
    elif n == 4:  # top left to bottom right
        for i in range(1, 5):
            board1[i, i] = 1
    print(board1)
    return board1


def check(player, board):
    """
    :param player: player number, 1 or 2
    :param board: current state of the board
    :returns: Boolean
    4 in a row is True
    Anything else is False
    """
    counter = 0
    # horizontal check
    for y in range(6):
        for x in range(7):
            if board[y, x] == player:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
    # vertical check
    for x in range(7):
        for y in range(6):
            if board[y, x] == player:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
    # no 4 in a row
    return False


print(check(1, test(0)))
