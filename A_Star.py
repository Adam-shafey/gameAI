from queue import PriorityQueue
import IO
import time

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
            self.depth = len(self.path)
            self.currentLocation = currentLocation
            self.swap(move, grid)
            self.path.append(grid)
            self.solutionPath = parent.solutionPath[:]
            self.solutionPath.append(move)
            self.start = parent.start
            self.goal = self.winCondition()
            self.dist = self.Distance()
        #this is the root node, the starting state
        else:
            self.path = [grid]
            self.depth = len(self.path)
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
        if self.goal == True:
            return 0
        elif self.currentLocation < 5:
            tally = 0

            if self.grid[0] == self.grid[10]:
                    tally = tally + 0
                    # no addition if empty space
                    #   elif self.currentLocation == 0:
                    #       tally = tally + 0

                    # they don't match, so we calculate nearest distance to x[0]
            elif (self.grid[10] == self.grid[1] or self.grid[10] == self.grid[5]):
                    tally = tally + 1
            elif self.grid[10] == self.grid[2] or self.grid[10] == self.grid[6]:
                    tally = tally + 2
            elif self.grid[10] == self.grid[3] or self.grid[10] == self.grid[7] or self.grid[10] == self.grid[11]:
                    tally = tally + 3
            elif self.grid[10] == self.grid[4] or self.grid[10] == self.grid[8] or self.grid[10] == self.grid[12]:
                    tally = tally + 4
            elif self.grid[10] == self.grid[9] or self.grid[10] == self.grid[13]:
                    tally = tally + 5
            elif self.grid[10] == self.grid[14]:
                    tally = tally + 6

            if self.grid[1] == self.grid[11]:
                    tally = tally + 0
                    #  elif self.currentLocation == 1:
                    #     tally = tally + 0
            elif self.grid[11] == self.grid[0] or self.grid[11] == self.grid[2] or self.grid[11] == self.grid[6]:
                    tally = tally + 1
            elif self.grid[11] == self.grid[3] or self.grid[11] == self.grid[5] or self.grid[11] == self.grid[7]:
                    tally = tally + 2
            elif self.grid[11] == self.grid[4] or self.grid[11] == self.grid[8] or self.grid[11] == self.grid[10] or self.grid[11] == self.grid[12]:
                    tally = tally + 3
            elif self.grid[11] == self.grid[9] or self.grid[11] == self.grid[13]:
                    tally = tally + 4
            elif self.grid[11] == self.grid[14]:
                    tally = tally + 5

            if self.grid[2] == self.grid[12]:
                    tally = tally + 0
                    # elif self.currentLocation == 2:
                    #   tally = tally + 0
            elif self.grid[12] == self.grid[1] or self.grid[12] == self.grid[3] or self.grid[12] == self.grid[7]:
                    tally = tally + 1
            elif self.grid[12] == self.grid[0] or self.grid[12] == self.grid[4] or self.grid[12] == self.grid[6] or self.grid[12] == self.grid[8]:
                    tally = tally + 2
            elif self.grid[12] == self.grid[5] or self.grid[12] == self.grid[9] or self.grid[12] == self.grid[11] or self.grid[12] == self.grid[13]:
                    tally = tally + 3
            elif self.grid[12] == self.grid[10] or self.grid[12] == self.grid[14]:
                    tally = tally + 4

            if self.grid[3] == self.grid[13]:
                    tally = tally + 0
                    # elif self.currentLocation == 3:
                    #   tally = tally + 0
            elif self.grid[13] == self.grid[2] or self.grid[13] == self.grid[4] or self.grid[13] == self.grid[8]:
                    tally = tally + 1
            elif self.grid[13] == self.grid[1] or self.grid[13] == self.grid[7] or self.grid[13] == self.grid[9]:
                    tally = tally + 2
            elif self.grid[13] == self.grid[0] or self.grid[13] == self.grid[6] or self.grid[13] == self.grid[12] or self.grid[13] == self.grid[14]:
                    tally = tally + 3
            elif self.grid[13] == self.grid[5] or self.grid[13] == self.grid[11]:
                    tally = tally + 4
            elif self.grid[13] == self.grid[10]:
                    tally = tally + 5

            if self.grid[4] == self.grid[14]:
                    tally = tally + 0
                    # elif self.currentLocation == 4:
                    #   tally = tally + 0
            elif self.grid[14] == self.grid[3] or self.grid[14] == self.grid[9]:
                    tally = tally + 1
            elif self.grid[14] == self.grid[2] or self.grid[14] == self.grid[8]:
                    tally = tally + 2
            elif self.grid[14] == self.grid[1] or self.grid[14] == self.grid[7] or self.grid[14] == self.grid[13]:
                    tally = tally + 3
            elif self.grid[14] == self.grid[0] or self.grid[14] == self.grid[6] or self.grid[14] == self.grid[12]:
                    tally = tally + 4
            elif self.grid[14] == self.grid[5] or self.grid[14] == self.grid[11]:
                    tally = tally + 5
            elif self.grid[14] == self.grid[10]:
                    tally = tally + 6
            if tally == 0:
                tally = tally + 1
            return tally
        else:
            tally2 = 0
                #Both side's scores are compared
            if self.grid[0] == self.grid[10]:
                    tally2 = tally2 + 0
                    # elif self.currentLocation == 10:
                    #   tally = tally + 0
                    # they don't match
            elif self.grid[0] == self.grid[11] or self.grid[0] == self.grid[5]:
                    tally2 = tally2 + 1
            elif self.grid[0] == self.grid[12] or self.grid[0] == self.grid[6]:
                    tally2 = tally2 + 2
            elif self.grid[0] == self.grid[13] or self.grid[0] == self.grid[7] or self.grid[0] == self.grid[1]:
                    tally2 = tally2 + 3
            elif self.grid[0] == self.grid[14] or self.grid[0] == self.grid[8] or self.grid[0] == self.grid[2]:
                    tally2 = tally2 + 4
            elif self.grid[0] == self.grid[9] or self.grid[0] == self.grid[3]:
                    tally2 = tally2 + 5
            elif self.grid[0] == self.grid[4]:
                    tally2 = tally2 + 6

            if self.grid[1] == self.grid[11]:
                    tally2 = tally2 + 0
                    # elif self.currentLocation == 11:
                    #    tally = tally + 0
            elif self.grid[1] == self.grid[10] or self.grid[1] == self.grid[12] or self.grid[1] == self.grid[6]:
                    tally2 = tally2 + 1
            elif self.grid[1] == self.grid[13] or self.grid[1] == self.grid[5] or self.grid[1] == self.grid[7]:
                    tally2 = tally2 + 2
            elif self.grid[1] == self.grid[14] or self.grid[1] == self.grid[8] or self.grid[1] == self.grid[0] or self.grid[1] == self.grid[2]:
                    tally2 = tally2 + 3
            elif self.grid[1] == self.grid[9] or self.grid[1] == self.grid[3]:
                    tally2 = tally2 + 4
            elif self.grid[1] == self.grid[4]:
                    tally2 = tally2 + 5

            if self.grid[2] == self.grid[12]:
                    tally2 = tally2 + 0
                    # elif self.currentLocation == 12:
                    #   tally = tally + 0
            elif self.grid[2] == self.grid[11] or self.grid[2] == self.grid[13] or self.grid[2] == self.grid[7]:
                    tally2 = tally2 + 1
            elif self.grid[2] == self.grid[10] or self.grid[2] == self.grid[14] or self.grid[2] == self.grid[6] or self.grid[2] == self.grid[8]:
                    tally2 = tally2 + 2
            elif self.grid[2] == self.grid[5] or self.grid[2] == self.grid[9] or self.grid[2] == self.grid[1] or self.grid[2] == self.grid[3]:
                    tally2 = tally2 + 3
            elif self.grid[2] == self.grid[0] or self.grid[2] == self.grid[4]:
                    tally2 = tally2 + 4

            if self.grid[3] == self.grid[13]:
                    tally2 = tally2 + 0
                    # elif self.currentLocation == 13:
                    #   tally = tally + 0
            elif self.grid[3] == self.grid[12] or self.grid[3] == self.grid[14] or self.grid[3] == self.grid[8]:
                    tally2 = tally2 + 1
            elif self.grid[3] == self.grid[11] or self.grid[3] == self.grid[7] or self.grid[3] == self.grid[9]:
                    tally2 = tally2 + 2
            elif self.grid[3] == self.grid[10] or self.grid[3] == self.grid[6] or self.grid[3] == self.grid[2] or self.grid[3] == self.grid[4]:
                    tally2 = tally2 + 3
            elif self.grid[3] == self.grid[5] or self.grid[3] == self.grid[1]:
                    tally2 = tally2 + 4
            elif self.grid[3] == self.grid[0]:
                    tally2 = tally2 + 5

            if self.grid[4] == self.grid[14]:
                    tally2 = tally2 + 0
                    # elif self.currentLocation == 14:
                    #   tally = tally + 0
            elif self.grid[4] == self.grid[13] or self.grid[4] == self.grid[9]:
                    tally2 = tally2 + 1
            elif self.grid[4] == self.grid[12] or self.grid[4] == self.grid[8]:
                    tally2 = tally2 + 2
            elif self.grid[4] == self.grid[11] or self.grid[4] == self.grid[7] or self.grid[4] == self.grid[3]:
                    tally2 = tally2 + 3
            elif self.grid[4] == self.grid[10] or self.grid[4] == self.grid[6] or self.grid[4] == self.grid[2]:
                    tally2 = tally2 + 4
            elif self.grid[4] == self.grid[5] or self.grid[4] == self.grid[1]:
                    tally2 = tally2 + 5
            elif self.grid[4] == self.grid[0]:
                    tally2 = tally2 + 6

            if tally2 == 0:
                tally2 = tally2 + 1
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
        if (self.grid[0] == self.grid[10] and
                self.grid[1] == self.grid[11] and
                self.grid[2] == self.grid[12] and
                self.grid[3] == self.grid[13] and
                self.grid[4] == self.grid[14]):
            return True
        else:
            return False

#The magic happens here baby! Ooooh yeah...
class AStar_Solver:
    def __init__(self, start):
        self.path = []
        self.solutionPath = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start

    #I made this one to return the path of each state
    #May need to be renamed?
    def Solve(self):
        startState = State(self.start, 0, 0, self.start)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path):
            closestChild = self.priorityQueue.get()[2]
            closestChild.makeABaby()
            self.visitedQueue.append(closestChild.grid)
            for child in closestChild.children:
                if child.grid not in self.visitedQueue:
                    count += 1
                    if child.dist == 0:
                        self.path = child.path
                        self.solutionPath = child.solutionPath
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("Goal of " + self.goal + " is not possible!")
        return self.path

    #The one returns the solution path (l, u, d...)

    def Solve2(self):
        startState = State(self.start, 0, 0, self.start)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path):
            closestChild = self.priorityQueue.get()[2]
            closestChild.makeABaby()
           # print(len(closestChild.path))
            self.visitedQueue.append(closestChild.grid)
            for child in closestChild.children:
                if child.grid not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        self.solutionPath = child.solutionPath
                        break
                    self.priorityQueue.put((child.dist + child.depth, count, child))
        if not self.path:
            print("Goal of " + self.goal + " is not possible!")
        return self.solutionPath

#runs the AStar_Solver
if __name__ == "__main__":
    start1 = IO.IO().readInitial('level4.txt')
    startTime = time.time()
    starter = start1[0]
    print('testing')

    for index in range(len(start1)):
        starter = start1[index]
        print(index)
        a = AStar_Solver(starter)
        a.Solve2()
        print(a.solutionPath.__len__())
        print(a.solutionPath)
    endTime = time.time()
    totalTime = int((endTime - startTime) * 1000)
    print(totalTime)
    print('ending...')