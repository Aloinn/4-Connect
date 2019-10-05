"""Alain's AI code"""
import numpy as np

class AI:
    def __init__(self,_team):
        """ Creates important variables and internal 'best place to go' map """
        self.turn = 1
        self.team = _team
        self.playerteam = 1 if self.team == 2 else 2
        self.board = 0
        self.map = np.array([[0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0],
                             [0,0,0,4,0,0,0],
                             [0,0,3,4,3,0,0],
                             [0,1,3,4,3,1,0],
                             [1,2,4,5,4,2,1],])
        self.map = np.rot90(self.map)
        self.map = np.flip(self.map)

    def check(self):
        """ Checks to see which column has the highest value placement"""
        """ Returns pos[value, x, y]"""
        tboard = self.map
        recorded = np.array([0,0,0])
        for xx,row in enumerate(tboard):
            for yy,value in enumerate(row):
                if value != 0 and value != -1:
                    if value > recorded[0]:
                        recorded[0] = value
                        recorded[1] = xx
                        recorded[2] = yy
                        break
                        # Forces program to continue
                        # So it doesn't check empty spaces as they are unreachable anyways
        # Returns data list for highest value, xx, and yy
        return recorded

    def updatemap(self,pos,turn):
        """ Updates the internal map of best place to go """
        """ Takes pos[v,x,y] and whose turn it is as parameters """

        xx = pos[1]
        yy = pos[2]

        """ If piece was placed by CPU, Increase value of all adjacent blocks or blocks that are capable of making a 4"""
        if turn == self.team:
            self.map[xx,yy] = self.team*-1
            for dx in range(-4,4):
                for dy in range(4):
                    """ Basically checking to see if adjacent block exists and if it is may be contained in either adjacent or diagonal line including piece"""
                    if ((dx != 0 and dy != 0) or (dx != 0 and dy == 0) or (dy != 0 and dx == 0))\
                            and (xx+dx < 7) and (xx+dx >= 0) and (yy + dy < 6) and (abs(dx)+abs(dy) != 5):
                        if self.map[xx+dx, yy+dy] >= 0:
                            """ If the slot hasnt been taken up, increase it's desirability """
                            self.map[xx+dx, yy+dy] += 6-abs(dx)-abs(dy)
        else:
            """ Finds location of most recently placed's y"""
            pos[1] -=1
            for count,piece in enumerate((self.map[pos[1]])):
                if piece > 0:
                    pos[2] = count
                    print(pos[2])
                    break;
            self.map[pos[1],pos[2]] = self.playerteam*-1

            """ Debug print location """
            #print(self.map[pos[1],pos[2]])

            """" Will add later, change desirability based on user input as well
            self.map[xx,yy] = self.playerteam*-1
            dx = 0
            streak = 0
            ## [Priority, x, y,] x2
            ends = np.array([[0,0],[0,0]])
            # Goes as far left as possible of human line
            while dx+xx >= 0 and self.map[xx+dx,yy] == self.playerteam*-1: dx+=1
            # Saves furthest left
            print(xx+dx)
            ends[0,0] = xx+dx
            ends[0,1] = yy
            # Goes as far right as possible of human line afterwards
            while dx+xx < 7 and self.map[xx+dx,yy] == self.playerteam*1:
                streak += 1
                dx-=1
            # Saves furthest right
            ends[1,0] = xx+dx
            ends[1,1] = yy
            print(ends)
            """

    def play(self,_board):
        """ Chooses a column to go based on the board given and current decision map """
        self.board = _board             # Updates board
        position = self.check()         # Check for best position to go

        # Feel free to uncomment out the print lines to see how the map is updated
        # print(np.rot90(self.map))
        self.updatemap(position,self.team)  # Updates internal desirability map based on best position
        # print(np.rot90(self.map))

        return(position[1]+1)           # Returns said position
