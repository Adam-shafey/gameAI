from queue import PriorityQueue
from queue import LifoQueue
import IO
import time
import Game

#each state of the grid, which is our array
class State(object):
    def __init__(self, grid, parent, currentLocation, move = 0, start_grid = 0):
        self.grid = grid
        self.parent = parent
        self.children = []
        self.solutionPath = []
        self.move = move


        #if a parent exists, i.e. the state is a child of another state
        if parent:
            self.path = parent.path[:]
            self.currentLocation = currentLocation
            self.swap(move, grid)
            self.path.append(grid)
            self.solutionPath = parent.solutionPath[:]
            # adding 65 to the int in chr will give you the correct A-O ascii
            self.solutionPath.append(chr(self.currentLocation + 65))
            self.depth = len(self.solutionPath)
            self.start_grid = parent.start_grid
            self.goal = self.winCondition()
            self.distance = self.getDistance()

        #this is the root node, the starting state
        else:
            self.path = [grid]
            self.depth = 0
            self.start_grid = start_grid
            self.currentLocation = self.getCurrentLoc()
            self.goal = self.winCondition()
            self.distance = self.getDistance()

    #this works very similarly to what we have in Game.py
    #when a child is initialized, it takes the currentLocation given by the parent
    #then the swap function takes place
    def swap(self, move, grid):

        if move == 'r':
            position = self.currentLocation
            grid[position] = grid[position + 1]
            position = position + 1
            grid[position] = 'e'
            self.currentLocation = position
        if move == 'l':
            position = self.currentLocation
            grid[position] = grid[position - 1]
            position = position - 1
            grid[position] = 'e'
            self.currentLocation = position
        if move == 'u':
            position = self.currentLocation
            grid[position] = grid[position - 5]
            position = position - 5
            grid[position] = 'e'
            self.currentLocation = position
        if move == 'd':
            position = self.currentLocation
            grid[position] = grid[position + 5]
            position = position + 5
            grid[position] = 'e'
            self.currentLocation = position
    #Like with Game.py, this only happens at the beginning (the root in this case)
    #after that the location is fed to child nodes through the constructor
    def getCurrentLoc(self):
        for index in range(len(self.grid)):
            if self.grid[index] == 'e':
                return index
    #The idea here is that if the goal is met, the distance to goal is zero
    #The more matches exist, the closer it is to the goal
    #The less difference there is between the left side and the right side, the closer it is to the goal
    def getDistance(self):
        #The distance is zero if the goal is met
        if self.goal == True:
            return 0
        #This tallies up the distance of the nearest matching char to its proper position on the opposing side
        #It tallies this for both the top and bottom side so there are 2 tallies
        else:
            tally = 0



            if self.grid[10] == 'e':
                tally = tally + 1
                if self.grid[0] == self.grid[5]:
                    tally = tally + 0
                # no addition if empty space
                #   elif self.currentLocation == 0:
                #       tally = tally + 0

                # they don't match, so we calculate nearest distance to x[0]
                elif (self.grid[5] == self.grid[1] and self.grid[1] != self.grid[11]):
                    tally = tally + 1
                elif (self.grid[5] == self.grid[2] and self.grid[2] != self.grid[12]) or self.grid[5] == self.grid[6]:
                    tally = tally + 2
                elif (self.grid[5] == self.grid[3] and self.grid[3] != self.grid[13]) or self.grid[5] == self.grid[7] or \
                    (self.grid[5] == self.grid[11] and self.grid[11] != self.grid[1]):
                    tally = tally + 3
                elif (self.grid[5] == self.grid[4] and self.grid[4] != self.grid[14]) or self.grid[5] == self.grid[8] or \
                    (self.grid[5] == self.grid[12] and self.grid[12] != self.grid[2]):
                    tally = tally + 4
                elif self.grid[5] == self.grid[9] or (self.grid[5] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally = tally + 5
                elif self.grid[5] == self.grid[14] and self.grid[14] != self.grid[4]:
                    tally = tally + 6
            else:
                if self.grid[0] == self.grid[10]:
                    tally = tally + 0
                # no addition if empty space
                #   elif self.currentLocation == 0:
                #       tally = tally + 0

                # they don't match, so we calculate nearest distance to x[0]
                elif (self.grid[10] == self.grid[1] and self.grid[1] != self.grid[11]) or self.grid[10] == self.grid[5]:
                    tally = tally + 1
                elif (self.grid[10] == self.grid[2] and self.grid[2] != self.grid[12]) or self.grid[10] == self.grid[6]:
                    tally = tally + 2
                elif (self.grid[10] == self.grid[3] and self.grid[3] != self.grid[13]) or self.grid[10] == self.grid[7] or \
                    (self.grid[10] == self.grid[11] and self.grid[11] != self.grid[1]):
                    tally = tally + 3
                elif (self.grid[10] == self.grid[4] and self.grid[4] != self.grid[14]) or self.grid[10] == self.grid[8] or \
                    (self.grid[10] == self.grid[12] and self.grid[12] != self.grid[2]):
                    tally = tally + 4
                elif self.grid[10] == self.grid[9] or (self.grid[10] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally = tally + 5
                elif self.grid[10] == self.grid[14] and self.grid[14] != self.grid[4]:
                    tally = tally + 6

            if self.grid[11] == 'e':
                tally = tally + 1
                if self.grid[1] == self.grid[6]:
                    tally = tally + 0
                #  elif self.currentLocation == 1:
                #     tally = tally + 0
                elif (self.grid[6] == self.grid[0] and self.grid[0] != self.grid[10]) or \
                    (self.grid[6] == self.grid[2] and self.grid[2] != self.grid[12]):
                    tally = tally + 1
                elif (self.grid[6] == self.grid[3] and self.grid[3] != self.grid[13]) or self.grid[6] == self.grid[5] or \
                    self.grid[6] == self.grid[7]:
                    tally = tally + 2
                elif (self.grid[6] == self.grid[4] and self.grid[4] != self.grid[14]) or self.grid[6] == self.grid[8] or \
                    (self.grid[6] == self.grid[10] and self.grid[10] != self.grid[0]) or \
                    (self.grid[6] == self.grid[12] and self.grid[12] != self.grid[2]):
                    tally = tally + 3
                elif self.grid[6] == self.grid[9] or (self.grid[6] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally = tally + 4
                elif self.grid[6] == self.grid[14] and self.grid[14] != self.grid[4]:
                    tally = tally + 5

            else:
                if self.grid[1] == self.grid[11]:
                    tally = tally + 0
                #  elif self.currentLocation == 1:
                #     tally = tally + 0
                elif (self.grid[11] == self.grid[0] and self.grid[0] != self.grid[10]) or \
                    (self.grid[11] == self.grid[2] and self.grid[2] != self.grid[12]) or self.grid[11] == self.grid[6]:
                    tally = tally + 1
                elif (self.grid[11] == self.grid[3] and self.grid[3] != self.grid[13]) or self.grid[11] == self.grid[5] or \
                    self.grid[11] == self.grid[7]:
                    tally = tally + 2
                elif (self.grid[11] == self.grid[4] and self.grid[4] != self.grid[14]) or self.grid[11] == self.grid[8] or \
                    (self.grid[11] == self.grid[10] and self.grid[10] != self.grid[0]) or \
                    (self.grid[11] == self.grid[12] and self.grid[12] != self.grid[2]):
                    tally = tally + 3
                elif self.grid[11] == self.grid[9] or (self.grid[11] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally = tally + 4
                elif self.grid[11] == self.grid[14] and self.grid[14] != self.grid[4]:
                    tally = tally + 5

            if self.grid[12] == 'e':
                tally = tally + 1
                if self.grid[2] == self.grid[7]:
                    tally = tally + 0
            # elif self.currentLocation == 2:
            #   tally = tally + 0
                elif (self.grid[7] == self.grid[1] and self.grid[1] != self.grid[11]) or \
                    (self.grid[7] == self.grid[3] and self.grid[3] != self.grid[13]):
                    tally = tally + 1
                elif (self.grid[7] == self.grid[0] and self.grid[0] != self.grid[10]) or \
                    (self.grid[7] == self.grid[4] and self.grid[4] != self.grid[14]) or self.grid[7] == self.grid[
                    6] or \
                    self.grid[7] == self.grid[8]:
                    tally = tally + 2
                elif self.grid[7] == self.grid[5] or self.grid[7] == self.grid[9] or (self.grid[7] == self.grid[11] and \
                    self.grid[7] != self.grid[1]) or (self.grid[7] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally = tally + 3
                elif (self.grid[7] == self.grid[10] and self.grid[10] != self.grid[0]) or \
                    (self.grid[7] == self.grid[14] and self.grid[14] != self.grid[4]):
                    tally = tally + 4
            else:
                if self.grid[2] == self.grid[12]:
                    tally = tally + 0
                # elif self.currentLocation == 2:
                #   tally = tally + 0
                elif (self.grid[12] == self.grid[1] and self.grid[1] != self.grid[11]) or \
                    (self.grid[12] == self.grid[3] and self.grid[3] != self.grid[13]) or self.grid[12] == self.grid[7]:
                    tally = tally + 1
                elif (self.grid[12] == self.grid[0] and self.grid[0] != self.grid[10]) or \
                    (self.grid[12] == self.grid[4] and self.grid[4] != self.grid[14]) or self.grid[12] == self.grid[6] or \
                    self.grid[12] == self.grid[8]:
                    tally = tally + 2
                elif self.grid[12] == self.grid[5] or self.grid[12] == self.grid[9] or (self.grid[12] == self.grid[11] and \
                    self.grid[11] != self.grid[1]) or (self.grid[12] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally = tally + 3
                elif (self.grid[12] == self.grid[10] and self.grid[10] != self.grid[0]) or \
                    (self.grid[12] == self.grid[14] and self.grid[14] != self.grid[4]):
                    tally = tally + 4

            if self.grid[13] == 'e':
                tally = tally + 1
                if self.grid[3] == self.grid[8]:
                    tally = tally + 0
                # elif self.currentLocation == 3:
                #   tally = tally + 0
                elif (self.grid[8] == self.grid[2] and self.grid[2] != self.grid[12]) or \
                    (self.grid[8] == self.grid[4] and self.grid[4] != self.grid[14]):
                    tally = tally + 1
                elif (self.grid[8] == self.grid[1] and self.grid[1] != self.grid[11]) or self.grid[8] == self.grid[7] or \
                    self.grid[8] == self.grid[9]:
                    tally = tally + 2
                elif (self.grid[8] == self.grid[0] and self.grid[0] != self.grid[10]) or self.grid[8] == self.grid[6] or \
                    (self.grid[8] == self.grid[12] and self.grid[12] != self.grid[2]) or \
                    (self.grid[8] == self.grid[14] and self.grid[14] != self.grid[4]):
                    tally = tally + 3
                elif self.grid[8] == self.grid[5] or (self.grid[8] == self.grid[11] and self.grid[11] != self.grid[1]):
                    tally = tally + 4
                elif self.grid[8] == self.grid[10] and self.grid[10] != self.grid[0]:
                    tally = tally + 5
            else:
                if self.grid[3] == self.grid[13]:
                    tally = tally + 0
                # elif self.currentLocation == 3:
                #   tally = tally + 0
                elif (self.grid[13] == self.grid[2] and self.grid[2] != self.grid[12]) or \
                    (self.grid[13] == self.grid[4] and self.grid[4] != self.grid[14]) or self.grid[13] == self.grid[8]:
                    tally = tally + 1
                elif (self.grid[13] == self.grid[1] and self.grid[1] != self.grid[11]) or self.grid[13] == self.grid[7] or \
                    self.grid[13] == self.grid[9]:
                    tally = tally + 2
                elif (self.grid[13] == self.grid[0] and self.grid[0] != self.grid[10]) or self.grid[13] == self.grid[6] or \
                    (self.grid[13] == self.grid[12] and self.grid[12] != self.grid[2]) or \
                    (self.grid[13] == self.grid[14] and self.grid[14] != self.grid[4]):
                    tally = tally + 3
                elif self.grid[13] == self.grid[5] or (self.grid[13] == self.grid[11] and self.grid[11] != self.grid[1]):
                    tally = tally + 4
                elif self.grid[13] == self.grid[10] and self.grid[10] != self.grid[0]:
                    tally = tally + 5

            if self.grid[14] == 'e':
                tally = tally + 1
                if self.grid[4] == self.grid[9]:
                    tally = tally + 0
                # elif self.currentLocation == 4:
                #   tally = tally + 0
                elif (self.grid[9] == self.grid[3] and self.grid[3] != self.grid[13]):
                    tally = tally + 1
                elif (self.grid[9] == self.grid[2] and self.grid[2] != self.grid[12]) or self.grid[9] == self.grid[8]:
                    tally = tally + 2
                elif (self.grid[9] == self.grid[1] and self.grid[1] != self.grid[11]) or self.grid[9] == self.grid[7] or \
                    (self.grid[9] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally = tally + 3
                elif (self.grid[9] == self.grid[0] and self.grid[0] != self.grid[10]) or self.grid[9] == self.grid[6] or \
                    (self.grid[9] == self.grid[12] and self.grid[12] != self.grid[2]):
                    tally = tally + 4
                elif self.grid[9] == self.grid[5] or (self.grid[9] == self.grid[11] and self.grid[11] != self. grid[1]):
                    tally = tally + 5
                elif self.grid[9] == self.grid[10] and self.grid[10] != self.grid[0]:
                    tally = tally + 6
            else:
                if self.grid[4] == self.grid[14]:
                    tally = tally + 0
                # elif self.currentLocation == 4:
                #   tally = tally + 0
                elif (self.grid[14] == self.grid[3] and self.grid[3] != self.grid[13]) or self.grid[14] == self.grid[9]:
                    tally = tally + 1
                elif (self.grid[14] == self.grid[2] and self.grid[2] != self.grid[12]) or self.grid[14] == self.grid[8]:
                    tally = tally + 2
                elif (self.grid[14] == self.grid[1] and self.grid[1] != self.grid[11]) or self.grid[14] == self.grid[7] or \
                    (self.grid[14] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally = tally + 3
                elif (self.grid[14] == self.grid[0] and self.grid[0] != self.grid[10]) or self.grid[14] == self.grid[6] or \
                    (self.grid[14] == self.grid[12] and self.grid[12] != self.grid[2]):
                    tally = tally + 4
                elif self.grid[14] == self.grid[5] or (self.grid[14] == self.grid[11] and self.grid[11] != self. grid[1]):
                    tally = tally + 5
                elif self.grid[14] == self.grid[10] and self.grid[10] != self.grid[0]:
                    tally = tally + 6

            tally2 = 0
            # Both side's scores are compared
            if self.grid[0] == 'e':
                tally2 = tally2 + 1
                if self.grid[5] == self.grid[10]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 10:
                #   tally = tally + 0
                # they don't match
                elif (self.grid[5] == self.grid[11] and self.grid[11] != self.grid[1]):
                    tally2 = tally2 + 1
                elif (self.grid[5] == self.grid[12] and self.grid[12] != self.grid[2]) or self.grid[5] == self.grid[6]:
                    tally2 = tally2 + 2
                elif (self.grid[5] == self.grid[13] and self.grid[13] != self.grid[3]) or self.grid[5] == self.grid[7] or \
                    (self.grid[5] == self.grid[1] and self.grid[1] != self.grid[11]):
                    tally2 = tally2 + 3
                elif (self.grid[5] == self.grid[14] and self.grid[14] != self.grid[4]) or self.grid[5] == self.grid[8] or \
                    (self.grid[5] == self.grid[2] and self.grid[2] != self.grid[12]):
                    tally2 = tally2 + 4
                elif self.grid[5] == self.grid[9] or (self.grid[5] == self.grid[3] and self.grid[3] != self.grid[13]):
                    tally2 = tally2 + 5
                elif self.grid[5] == self.grid[4] and self.grid[4] != self.grid[14]:
                    tally2 = tally2 + 6
            else:
                if self.grid[0] == self.grid[10]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 10:
                #   tally = tally + 0
                # they don't match
                elif (self.grid[0] == self.grid[11] and self.grid[11] != self.grid[1]) or self.grid[0] == self.grid[5]:
                    tally2 = tally2 + 1
                elif (self.grid[0] == self.grid[12] and self.grid[12] != self.grid[2]) or self.grid[0] == self.grid[6]:
                    tally2 = tally2 + 2
                elif (self.grid[0] == self.grid[13] and self.grid[13] != self.grid[3]) or self.grid[0] == self.grid[7] or \
                    (self.grid[0] == self.grid[1] and self.grid[1] != self.grid[11]):
                    tally2 = tally2 + 3
                elif (self.grid[0] == self.grid[14] and self.grid[14] != self.grid[4]) or self.grid[0] == self.grid[8] or \
                    (self.grid[0] == self.grid[2] and self.grid[2] != self.grid[12]):
                    tally2 = tally2 + 4
                elif self.grid[0] == self.grid[9] or (self.grid[0] == self.grid[3] and self.grid[3] != self.grid[13]):
                    tally2 = tally2 + 5
                elif self.grid[0] == self.grid[4] and self.grid[4] != self.grid[14]:
                    tally2 = tally2 + 6

            if self.grid[1] == 'e':
                tally2 = tally2 + 1
                if self.grid[6] == self.grid[11]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 11:
                #    tally = tally + 0
                elif (self.grid[6] == self.grid[10] and self.grid[10] != self.grid[0]) or \
                    (self.grid[6] == self.grid[12] and self.grid[12] != self.grid[2]):
                    tally2 = tally2 + 1
                elif (self.grid[6] == self.grid[13] and self.grid[13] != self.grid[3]) or \
                    self.grid[6] == self.grid[5] or self.grid[6] == self.grid[7]:
                    tally2 = tally2 + 2
                elif (self.grid[6] == self.grid[14] and self.grid[14] != self.grid[4]) or self.grid[6] == self.grid[8] or \
                    (self.grid[6] == self.grid[0] and self.grid[0] != self.grid[10]) or \
                    (self.grid[6] == self.grid[2] and self.grid[2] != self.grid[12]):
                    tally2 = tally2 + 3
                elif self.grid[6] == self.grid[9] or (self.grid[6] == self.grid[3] and self.grid[3] != self.grid[13]):
                    tally2 = tally2 + 4
                elif self.grid[6] == self.grid[4] and self.grid[4] != self.grid[14]:
                    tally2 = tally2 + 5
            else:
                if self.grid[1] == self.grid[11]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 11:
                #    tally = tally + 0
                elif (self.grid[1] == self.grid[10] and self.grid[10] != self.grid[0]) or \
                    (self.grid[1] == self.grid[12] and self.grid[12] != self.grid[2]) or self.grid[1] == self.grid[6]:
                    tally2 = tally2 + 1
                elif (self.grid[1] == self.grid[13] and self.grid[13] != self.grid[3]) or \
                    self.grid[1] == self.grid[5] or self.grid[1] == self.grid[7]:
                    tally2 = tally2 + 2
                elif (self.grid[1] == self.grid[14] and self.grid[14] != self.grid[4]) or self.grid[1] == self.grid[8] or \
                    (self.grid[1] == self.grid[0] and self.grid[0] != self.grid[10]) or \
                    (self.grid[1] == self.grid[2] and self.grid[2] != self.grid[12]):
                    tally2 = tally2 + 3
                elif self.grid[1] == self.grid[9] or (self.grid[1] == self.grid[3] and self.grid[3] != self.grid[13]):
                    tally2 = tally2 + 4
                elif self.grid[1] == self.grid[4] and self.grid[4] != self.grid[14]:
                    tally2 = tally2 + 5

            if self.grid[2] == 'e':
                tally2 = tally2 + 1
                if self.grid[7] == self.grid[12]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 12:
                #   tally = tally + 0
                elif (self.grid[7] == self.grid[11] and self.grid[11] != self.grid[1]) or \
                    (self.grid[7] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally2 = tally2 + 1
                elif (self.grid[7] == self.grid[10] and self.grid[10] != self.grid[0]) or \
                    (self.grid[7] == self.grid[14] and self.grid[14] != self.grid[4]) or self.grid[7] == self.grid[6] or \
                    self.grid[7] == self.grid[8]:
                    tally2 = tally2 + 2
                elif self.grid[7] == self.grid[5] or self.grid[7] == self.grid[9] or (self.grid[7] == self.grid[1] and \
                    self.grid[1] != self.grid[11]) or (self.grid[7] == self.grid[3] and self.grid[13] != self.grid[3]):
                    tally2 = tally2 + 3
                elif (self.grid[7] == self.grid[0] and self.grid[0] != self.grid[10]) or \
                    (self.grid[7] == self.grid[4] and self.grid[4] != self.grid[14]):
                    tally2 = tally2 + 4
            else:
                if self.grid[2] == self.grid[12]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 12:
                #   tally = tally + 0
                elif (self.grid[2] == self.grid[11] and self.grid[11] != self.grid[1]) or \
                    (self.grid[2] == self.grid[13] and self.grid[13] != self.grid[3]) or self.grid[2] == self.grid[7]:
                    tally2 = tally2 + 1
                elif (self.grid[2] == self.grid[10] and self.grid[10] != self.grid[0]) or \
                    (self.grid[2] == self.grid[14] and self.grid[14] != self.grid[4]) or self.grid[2] == self.grid[6] or \
                    self.grid[2] == self.grid[8]:
                    tally2 = tally2 + 2
                elif self.grid[2] == self.grid[5] or self.grid[2] == self.grid[9] or (self.grid[2] == self.grid[1] and \
                    self.grid[1] != self.grid[11]) or (self.grid[2] == self.grid[3] and self.grid[13] != self.grid[3]):
                    tally2 = tally2 + 3
                elif (self.grid[2] == self.grid[0] and self.grid[0] != self.grid[10]) or \
                    (self.grid[2] == self.grid[4] and self.grid[4] != self.grid[14]):
                    tally2 = tally2 + 4

            if self.grid[3] == 'e':
                tally2 = tally2 + 1
                if self.grid[8] == self.grid[13]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 13:
                #   tally = tally + 0
                elif (self.grid[8] == self.grid[12] and self.grid[12] != self.grid[2]) or \
                    (self.grid[8] == self.grid[14] and self.grid[14] != self.grid[4]):
                    tally2 = tally2 + 1
                elif (self.grid[8] == self.grid[11] and self.grid[11] != self.grid[1]) or self.grid[8] == self.grid[7] or \
                    self.grid[8] == self.grid[9]:
                    tally2 = tally2 + 2
                elif (self.grid[8] == self.grid[10] and self.grid[10] != self.grid[0]) or self.grid[8] == self.grid[6] or \
                    self.grid[8] == self.grid[2] or (self.grid[8] == self.grid[4] and self.grid[4] != self.grid[14]):
                    tally2 = tally2 + 3
                elif self.grid[8] == self.grid[5] or (self.grid[8] == self.grid[1] and self.grid[1] != self.grid[11]):
                    tally2 = tally2 + 4
                elif (self.grid[8] == self.grid[0] and self.grid[0] != self.grid[10]):
                    tally2 = tally2 + 5

            else:
                if self.grid[3] == self.grid[13]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 13:
                #   tally = tally + 0
                elif (self.grid[3] == self.grid[12] and self.grid[12] != self.grid[2]) or \
                    (self.grid[3] == self.grid[14] and self.grid[14] != self.grid[4]) or self.grid[3] == self.grid[8]:
                    tally2 = tally2 + 1
                elif (self.grid[3] == self.grid[11] and self.grid[11] != self.grid[1]) or self.grid[3] == self.grid[7] or \
                    self.grid[3] == self.grid[9]:
                    tally2 = tally2 + 2
                elif (self.grid[3] == self.grid[10] and self.grid[10] != self.grid[0]) or self.grid[3] == self.grid[6] or \
                    self.grid[3] == self.grid[2] or (self.grid[3] == self.grid[4] and self.grid[4] != self.grid[14]):
                    tally2 = tally2 + 3
                elif self.grid[3] == self.grid[5] or (self.grid[3] == self.grid[1] and self.grid[1] != self.grid[11]):
                    tally2 = tally2 + 4
                elif (self.grid[3] == self.grid[0] and self.grid[0] != self.grid[10]):
                    tally2 = tally2 + 5

            if self.grid[4] == 'e':
                tally2 = tally2 + 1
                if self.grid[9] == self.grid[14]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 14:
                #   tally = tally + 0
                elif (self.grid[9] == self.grid[13] and self.grid[13] != self.grid[3]):
                    tally2 = tally2 + 1
                elif (self.grid[9] == self.grid[12] and self.grid[12] != self.grid[2]) or self.grid[9] == self.grid[8]:
                    tally2 = tally2 + 2
                elif (self.grid[9] == self.grid[11] and self.grid[11] != self.grid[1]) or self.grid[9] == self.grid[7] or \
                    (self.grid[9] == self.grid[3] and self.grid[3] != self.grid[13]):
                    tally2 = tally2 + 3
                elif (self.grid[9] == self.grid[10] and self.grid[10] != self.grid[0]) or self.grid[9] == self.grid[6] or \
                    (self.grid[9] == self.grid[2] and self.grid[2] != self.grid[12]):
                    tally2 = tally2 + 4
                elif self.grid[9] == self.grid[5] or (self.grid[9] == self.grid[1] and self.grid[1] != self.grid[11]):
                    tally2 = tally2 + 5
                elif self.grid[9] == self.grid[0] and self.grid[0] != self.grid[10]:
                    tally2 = tally2 + 6
            else:
                if self.grid[4] == self.grid[14]:
                    tally2 = tally2 + 0
                # elif self.currentLocation == 14:
                #   tally = tally + 0
                elif (self.grid[4] == self.grid[13] and self.grid[13] != self.grid[3]) or self.grid[4] == self.grid[9]:
                    tally2 = tally2 + 1
                elif (self.grid[4] == self.grid[12] and self.grid[12] != self.grid[2]) or self.grid[4] == self.grid[8]:
                    tally2 = tally2 + 2
                elif (self.grid[4] == self.grid[11] and self.grid[11] != self.grid[1]) or self.grid[4] == self.grid[7] or \
                    (self.grid[4] == self.grid[3] and self.grid[3] != self.grid[13]):
                    tally2 = tally2 + 3
                elif (self.grid[4] == self.grid[10] and self.grid[10] != self.grid[0]) or self.grid[4] == self.grid[6] or \
                    (self.grid[4] == self.grid[2] and self.grid[2] != self.grid[12]):
                    tally2 = tally2 + 4
                elif self.grid[4] == self.grid[5] or (self.grid[4] == self.grid[1] and self.grid[1] != self.grid[11]):
                    tally2 = tally2 + 5
                elif self.grid[4] == self.grid[0] and self.grid[0] != self.grid[10]:
                    tally2 = tally2 + 6

            if tally < tally2:
                if self.currentLocation > 4 and self.currentLocation < 9:
                    return tally + 1
                else:
                    return tally
            else:
                if self.currentLocation > 4 and self.currentLocation < 9:
                    return tally2 + 1
                else:
                    return tally2


        # As before, this checks to ensure the move is legal.
        # Otherwise we could end up off the grid, which unlike real life, is unpleasant
    def isLegal(self, move):
        if move == 'r':  # cannot move right if the empty space is in the last column
                if (self.currentLocation == 4 or self.currentLocation == 9 or self.currentLocation == 14):
                    return False
                else:
                    return True
        if move == 'l':  # cannot move left if the empty space is in the first column
                if (self.currentLocation == 0 or self.currentLocation == 5 or self.currentLocation == 10):
                    return False
                else:
                    return True
        if move == 'u':  # cannot move up if the empty space is in the first row
                if (self.currentLocation == 0 or self.currentLocation == 1 or self.currentLocation == 2 or
                        self.currentLocation == 3 or self.currentLocation == 4):
                    return False
                else:
                    return True
        if move == 'd':  # cannot move down if the empty space is in the last row
                if (self.currentLocation == 10 or self.currentLocation == 11 or self.currentLocation == 12
                        or self.currentLocation == 13 or self.currentLocation == 14):
                    return False
                else:
                    return True

        # This creates a set of children. We can rename it if you think the name is in bad taste
        # This only makes a child if the move is legal, and if it's not going back the way it came
    def makeABaby(self):
        if not self.children:
            if (self.isLegal('r') and self.move != 'l'):
                childGrid = self.grid[:]
                child = State(childGrid, self, self.currentLocation, 'r')
                self.children.append(child)

            if (self.isLegal('l') and self.move != 'r'):
                childGrid = self.grid[:]
                child = State(childGrid, self, self.currentLocation, 'l')
                self.children.append(child)

            if (self.isLegal('u') and self.move != 'd'):
                childGrid = self.grid[:]
                child = State(childGrid, self, self.currentLocation, 'u')
                self.children.append(child)

            if (self.isLegal('d') and self.move != 'u'):
                childGrid = self.grid[:]
                child = State(childGrid, self, self.currentLocation, 'd')
                self.children.append(child)

    #Same condition as before. This will let the AI know the goal is met
    def winCondition(self):
        if self.grid[0:5] == self.grid[10:15]:
            return True
        else:
            return False

#The magic happens here baby! Ooooh yeah...
class PathFinder:
    def __init__(self, start_grid):
        self.path = []
        self.solutionPath = []
        self.open = PriorityQueue()
        self.closed = []
        self.start_grid = start_grid
        self.winGrid = []


#This is the method that finds the solution
    def findPath(self):
        root = State(self.start_grid, 0, 0, self.start_grid)
        x = set(root.grid) and set(root.grid)
        #this tells us what kind of level situation we have
        numCandyTypes = len(x) - 1
        count = 0
        self.open.put((0, count, root))
        beginTime = time.time()

        #This is an A algorithm
        while(not self.solutionPath):
            bestState = self.open.get()[2]
            bestState.makeABaby()
            self.closed.append(bestState.grid)
            for child in bestState.children:
                if child.grid not in self.closed:
                    if child.goal:
                        self.path = child.path
                        self.solutionPath = child.solutionPath
                        self.winGrid = child.grid
                        #print("Count is " + str(count))
                        #print(child.grid)
                        break
                    else:
                        count += 1
                        #self.open.put((int(child.distance) + int(child.depth), count, child))
                        if numCandyTypes == 3 and int((time.time() - beginTime) * 1000) < 2000:
                            self.open.put((int(child.distance * 1.1) + int(child.depth/1.06), count, child))
                        elif numCandyTypes == 3 and int((time.time() - beginTime) * 1000) < 4000:
                            self.open.put((int(child.distance * 1.14) + int(child.depth / 1.06), count, child))
                        elif numCandyTypes == 3 and int((time.time() - beginTime) * 1000) < 5000:
                            self.open.put((int(child.distance * 1.19) + int(child.depth / 1.15), count, child))
                        elif numCandyTypes == 3 and int((time.time() - beginTime) * 1000) < 6000:
                            self.open.put((int(child.distance * 1.25) + int(child.depth / 1.25), count, child))
                        elif numCandyTypes == 3:
                            self.open.put((int(child.distance * 1.3) + int(child.depth / 1.3), count, child))

                        if numCandyTypes == 4 and int((time.time() - beginTime) * 1000) < 800:
                            self.open.put((int(child.distance * 1.1) + int(child.depth/1.06), count, child))
                        elif numCandyTypes == 4 and int((time.time() - beginTime) * 1000) < 1800:
                            self.open.put((int(child.distance * 1.14) + int(child.depth / 1.14), count, child))
                        elif numCandyTypes == 4 and int((time.time() - beginTime) * 1000) < 2500:
                            self.open.put((int(child.distance * 1.19) + int(child.depth / 1.19), count, child))
                        elif numCandyTypes == 4 and int((time.time() - beginTime) * 1000) < 3000:
                            self.open.put((int(child.distance * 1.25) + int(child.depth / 1.25), count, child))
                        elif numCandyTypes == 4:
                            self.open.put((int(child.distance * 1.41) + int(child.depth / 1.38), count, child))

                        if numCandyTypes == 5 and int((time.time() - beginTime) * 1000) < 900:
                            self.open.put((int(child.distance * 1.1) + int(child.depth/1.06), count, child))
                        elif numCandyTypes == 5 and int((time.time() - beginTime) * 1000) < 3700:
                            self.open.put((int(child.distance * 1.13) + int(child.depth / 1.07), count, child))
                        elif numCandyTypes == 5 and int((time.time() - beginTime) * 1000) < 4500:
                            self.open.put((int(child.distance * 1.17) + int(child.depth / 1.15), count, child))
                        elif numCandyTypes == 5 and int((time.time() - beginTime) * 1000) < 6750:
                            self.open.put((int(child.distance * 1.25) + int(child.depth / 1.25), count, child))
                        elif numCandyTypes == 5:
                            self.open.put((int(child.distance * 1.41) + int(child.depth / 1.38), count, child))

                        if numCandyTypes == 6 and int((time.time() - beginTime) * 1000) < 1000:
                            self.open.put((int(child.distance * 1.1) + int(child.depth/1.06), count, child))
                        elif numCandyTypes == 6 and int((time.time() - beginTime) * 1000) < 2000:
                            self.open.put((int(child.distance * 1.14) + int(child.depth / 1.13), count, child))
                        elif numCandyTypes == 6 and int((time.time() - beginTime) * 1000) < 3000:
                            self.open.put((int(child.distance * 1.19) + int(child.depth / 1.16), count, child))
                        elif numCandyTypes == 6 and int((time.time() - beginTime) * 1000) < 4500:
                            self.open.put((int(child.distance * 1.25) + int(child.depth / 1.21), count, child))
                        elif numCandyTypes == 6:
                            self.open.put((int(child.distance * 1.41) + int(child.depth / 1.38), count, child))

        return self.solutionPath


#runs the PathFinder
if __name__ == "__main__":
    print('Welcome to the solution finder')
    print(' ')
    print(' ')
    print('Would you like to run the automated pathfinder? (enter y or n)')
    answer = input()
    if answer == 'y':
        allLevels = IO.IO().readInitial('InputFile.txt')
        print("Starting... ")
        solutions = []
        allMoves = []
        completedLevels = []
        startTime = time.time()
        allGrids = []
        for index in range(len(allLevels)):
            currentLevel = allLevels[index]
            #print(index)
            pf = PathFinder(currentLevel)
            pf.findPath()
            #print(a.solutionPath.__len__())
            #print(a.solutionPath)
            solutions.append(pf.solutionPath)
            allMoves.append(pf.solutionPath.__len__())
            completedLevels.append(pf.winGrid)
            allGrids.append(pf.path)

        endTime = time.time()
        totalTime = int((endTime - startTime) * 1000)
        IO.IO().printResult2(solutions, completedLevels, allMoves, allGrids, totalTime)
        print("Total time taken: " + str(totalTime))
        sum = 0
        for index in range(len(allMoves)):
            sum = sum + allMoves[index]
        print("Total number of moves: " + str(sum))
        print('ending...')
    else:
        print("Very well, you can find the path yourself!")
        Game.Game().runProgram()