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


def straight_check(isHorizontal, range1, range2, player, board):
    """
    function to check for 4 in a row in the x or y axis
    :param isHorizontal: bool for horizontal or vertical check
    :param range1: first for loop
    :param range2: second for loop
    :param player: player number
    :param board: current board
    :return: boolean
    """
    counter = 0
    for i in range(range1):
        for j in range(range2):
            if isHorizontal:
                temp = board[i, j]
            else:
                temp = board[j, i]
            if temp == player:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True


def diagonal_check(rangeStart, rangeEnd, difference, player, board):
    """
    function checks for diagonal 4 in a row from bottom left to top right of board
    :param rangeStart: start of for loop
    :param rangeEnd: end of for loop
    :param difference: difference between the x and y values
    :param player: player number
    :param board: current board
    :return: boolean
    """
    counter = 0
    for i in range(rangeStart, rangeEnd):
        if board[difference - i, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True


def diagonal_check2(rangeEnd, diffY, diffX, player, board):
    """
    function checks for diagonal 4 in a row from bottom right to top left of board
    :param rangeEnd: range for the for loop
    use each difference depending on which direction the axis is going
    :param diffY: difference of y from x
    :param diffX: difference of x from y
    :param player: player number
    :param board: current board
    :return: boolean
    """
    counter = 0
    for i in range(rangeEnd):
        if board[i + diffY, i + diffX] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True


def check(player, board):
    """
    :param player: player number, 1 or 2
    :param board: current state of the board
    :returns: Boolean
    4 in a row is True
    Anything else is False
    """
    if straight_check(True, 6, 7, player, board):
        return True
    elif straight_check(False, 7, 6, player, board):
        return True
    elif diagonal_check(0, 4, 3, player, board):
        return True
    elif diagonal_check(3, 7, 8, player, board):
        return True
    elif diagonal_check(0, 5, 4, player, board):
        return True
    elif diagonal_check(2, 7, 7, player, board):
        return True
    elif diagonal_check(0, 6, 5, player, board):
        return True
    elif diagonal_check(1, 7, 6, player, board):
        return True
    elif diagonal_check2(4, 2, 0, player, board):
        return True
    elif diagonal_check2(4, 0, 3, player, board):
        return True
    elif diagonal_check2(5, 1, 0, player, board):
        return True
    elif diagonal_check2(5, 0, 2, player, board):
        return True
    elif diagonal_check2(6, 0, 0, player, board):
        return True
    elif diagonal_check2(6, 0, 1, player, board):
        return True

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
    
    
    # bottom left to top right check
    for i in range(4):
        if board[3 - i, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(3, 7):
        if board[8 - i, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(5):
        if board[4 - i, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(2, 7):
        if board[7 - i, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(6):
        if board[5 - i, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(1, 7):
        if board[6 - i, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True


    # bottom right to top left check
    for i in range(4):
        if board[i + 2, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(4):
        if board[i, i + 3] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(5):
        if board[i + 1, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(5):
        if board[i, i + 2] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(6):
        if board[i, i] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True

    for i in range(6):
        if board[i, i + 1] == player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
    """  # old code

    # no 4 in a row
    return False

# TESTING
# print(check(1, test(1)))
