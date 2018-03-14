from queue import PriorityQueue
from queue import LifoQueue
import IO
import time
import Game

#each state of the grid, which is our array
class State(object):
    def __init__(self, grid, parent, currentLocation, move = 0, start = 0):
        self.children = []
        self.parent = parent
        self.grid = grid
        self.dist = 0
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
            self.start = parent.start
            self.goal = self.winCondition()
            self.dist = self.Distance()
        #this is the root node, the starting state
        else:
            self.path = [grid]
            self.depth = 0
            self.start = start
            self.currentLocation = self.getCurrentLoc()
            self.goal = self.winCondition()
            self.dist = self.Distance()
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
    def Distance(self):
        #The distance is zero if the goal is met
        if self.goal == True:
            return 0
        #if empty space is in the first five spaces, it takes the last 5 spaces,
        #then compares the distance of the matching value to the first 5 spaces
        else:
            tally = 0

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

            if tally > tally2:
                #if self.currentLocation > 4 and self.currentLocation < 9:
                    return tally #+ 1
                #else:
                 #   return tally
            else:
                #if self.currentLocation > 4 and self.currentLocation < 9:
                    return tally2 #+ 1
                #else:
                 #   return tally2


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
    def __init__(self, start):
        self.path = []
        self.solutionPath = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.open = []
        self.start = start
        self.stack = LifoQueue()
        self.winGrid = []

#This is the method that finds the solution
    def Solve(self):
        startState = State(self.start, 0, 0, self.start)
        x = set(startState.grid) and set(startState.grid)
        #this tells us what kind of level situation we have
        numCandyTypes = len(x) - 1
        count = 0
        self.priorityQueue.put((0, count, startState))
        beginTime = time.time()

        #This is an A algorithm
        while(not self.path):
            nearestChild = self.priorityQueue.get()[2]
            nearestChild.makeABaby()
           # print(len(closestChild.path))
            self.visitedQueue.append(nearestChild.grid)
            for child in nearestChild.children:
                if child.grid not in self.visitedQueue:
                    count += 1
                    if child.goal:
                        self.path = child.path
                        self.solutionPath = child.solutionPath
                        self.winGrid = child.grid
                        #print(child.grid)
                        break
                    else:
                        self.priorityQueue.put((child.dist + child.depth, count, child))
            #These will break the loop if any solution is taking too long
            #level1
            if numCandyTypes == 3 and int((time.time() - beginTime) * 1000) > 50000:
                break
            #level2
            if numCandyTypes == 4 and int((time.time() - beginTime) * 1000) > 11000:
                break
            #level3
            if numCandyTypes == 5 and int((time.time() - beginTime) * 1000) > 7900:
                break
            #level4
            if numCandyTypes == 6 and int((time.time() - beginTime) * 1000) > 5000:
                break
        #This only happens if the loop above gets broken without a solution
        #It is nearly identical except this time it is a best first search
        if not self.path:
            self.visitedQueue = []
            self.priorityQueue = PriorityQueue()
            count = 0
            self.priorityQueue.put((0, count, startState))
            while (not self.path):
                nearestChild = self.priorityQueue.get()[2]
                nearestChild.makeABaby()
                self.visitedQueue.append(nearestChild.grid)
                for child in nearestChild.children:
                    if child.grid not in self.visitedQueue:
                        count += 1
                        if child.goal:
                            self.path = child.path
                            self.solutionPath = child.solutionPath
                            self.winGrid = child.grid
                            print("OptionalPath")
                            #print(child.grid)
                            break
                        else:
                            self.priorityQueue.put((child.dist, count, child))
        return self.solutionPath


#runs the PathFinder
if __name__ == "__main__":
    print('Welcome to the solution finder')
    print(' ')
    print(' ')
    print('Would you like to run the automated pathfinder? (enter y or n)')
    answer = input()
    if answer == 'y':
        start1 = IO.IO().readInitial('InputFile.txt')
        print("Starting... ")
        starter = start1[0]
        solutions = []
        allMoves = []
        completedLevels = []
        startTime = time.time()
        for index in range(len(start1)):
            starter = start1[index]
            #print(index)
            a = PathFinder(starter)
            a.Solve()
            #print(a.solutionPath.__len__())
            #print(a.solutionPath)
            solutions.append(a.solutionPath)
            allMoves.append(a.solutionPath.__len__())
            completedLevels.append(a.winGrid)

        endTime = time.time()
        totalTime = int((endTime - startTime) * 1000)
        IO.IO().printResult2(solutions, completedLevels, allMoves, totalTime)
        print("Total time taken: " + str(totalTime))
        sum = 0
        for index in range(len(allMoves)):
            sum = sum + allMoves[index]
        print("Total number of moves: " + str(sum))
        print('ending...')
    else:
        print("Very well, you can find the path yourself!")
        Game.Game().runProgram()