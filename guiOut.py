import numpy as np
import os
import time as ti


def getComp(board):
    """
    :param board: Data set of board (2D array of 0's, 1's and 2's)
    :return: boardComp: Board symbolically represented as a single list (1D array of spaces, X's and O's)
    """
    string = str(board)  # converting list to string
    boardComp = ''
    sym = '012'
    for i, x in enumerate(string):
        if x in sym:  # removing irrelevant characters and converting to graphical symbols
            if x == '0':
                dis_sym = ' '
            elif x == '1':
                dis_sym = 'X'
            elif x == '2':
                dis_sym = 'O'
            boardComp += dis_sym
    boardComp = list(boardComp)  # converting string into a singular 1D list
    return boardComp


def read(oldB, newB):
    """
    Reads two consecutive boards and returns the difference between them
    :param: oldB: Previous board state
    :param: newB: Current board state
    :return: : change: The index location and value of the change.
    """

    for y in range(0, 6):  # looping rows
        for x in range(0, 7):  # looping columns
            if oldB[y, x] != newB[y, x]:
                change = [y, x, newB[y, x]]
    return change  # change[0] = row, change[1] = column, change[2] = player


def printGuiBoard(board):
    """
    Takes any board state and prints is graphically
    :param board: Any board state
    :return: Print out of 4-connect board
    """
    boardShell = ("   __   _   _   _   _   _   _   __\n"
                  "   || {} | {} | {} | {} | {} | {} | {} ||\n"
                  "   || {} | {} | {} | {} | {} | {} | {} ||\n"
                  "   || {} | {} | {} | {} | {} | {} | {} ||\n"
                  "   || {} | {} | {} | {} | {} | {} | {} ||\n"
                  "   || {} | {} | {} | {} | {} | {} | {} ||\n"
                  "   || {} | {} | {} | {} | {} | {} | {} ||\n"
                  "   ||^^^^^^^^^^^^^^^^^^^^^^^^^^^||\n"
                  "   ||                           ||\n"
                  "___||___                     ___||___\n")

    print(boardShell.format(*getComp(board)))  # formats the list into the board shell


def boardAni(oldB, change):
    """
    Animates the player piece as it falls into place
    :param oldB: old board (before)
    :param change: new board (after)
    :return:
    """
    yLimit = change[0]
    column = change[1]
    playerUnit = change[2]
    for i in range(0, yLimit + 1):  # reprint the game board until it reaches its limit
        oldB[i, column] = playerUnit
        print("\n" * 100)  # Using this until i find a way to actually clear the screen in pycharm
        printGuiBoard(oldB)
        if i != yLimit:
            oldB[i, column] = 0
        ti.sleep(0.35)


# TODO: remove comments to run an example.

# result1 = np.zeros((6, 7))
# result2 = np.zeros((6, 7))
# result2[5, 3] = 1
# boardAni(result1, read(result1, result2))
