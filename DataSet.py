import numpy as np

def update(xVal, player, board):
    """"""
    """Update function. Update the user's input, returns board. Function also sends 'yVal' to returnY(yVal).
        The function checks whether the coordinate in numpy is empty (value = 0). If it is occupied, then the yVal
        decreases until an empty space is found. Otherwise, it prompts the user that the column is full."""
                    #Note: param 'player' should be an int value, 1 or 2
    check = True    #Boolean that loops(value = True) until a proper user input is selected(value = False).
    yVal = 5        #Original y value.
    while check:
        if xVal < 1 or xVal > 7:    #Condition met when user does not select the correct row
            print('Please choose a row 1-7. In: ')
            check = False
            yVal = 5
            xVal = 1

        elif board[yVal, xVal - 1] == 0 and yVal >= 0: # First condition checks whether space is empty, second condition checks
                                                       # whether there is still space in the column.
            board[yVal, xVal - 1] = player          # Adds piece onto the board
            check = False                           # Changes boolean to false, breaks loop

        elif yVal < 0:  #Condition is met when the column is full.
            yVal = 5    #Resets value
            xVal = 1
            print('The column is full. In: ')   #prompts  user when column is full
            check = False

        else:
            yVal = yVal - 1  #Decreases y value (as mentioned in description) to check whether the coordinate is empty.
            check = True

    returnY(yVal) #Sends yVal over to the returnY(yVal) function
    return board  #returns the board back to Game.py

def returnY(yVal): #Returns the y Value
    return yVal


# board = np.zeros((6, 7)) #TODO: TEST CODE, FEEL FREE TO UNCOMMENT AND TEST IT OUT!
#
# while True:
#     n = int(input('Enter xVal: '))
#     print(update(n, 1, board))
#

