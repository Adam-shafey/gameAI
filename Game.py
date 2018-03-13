import IO
import time


class Game(object):
    def __init__(self):
        self.numOfMoves = 0
        self.currentGameArray = []
        self.level = 0
        self.completedLevels = []
        self.currentSolution = []
        self.solutions = []
        self.allMoves = []
        self.currentLocation = 0
        self.gameTime = []

    # Loads all the levels from the file
    def loadFile(self, fileName):
        tempList = IO.IO().readInitial(fileName)
        return tempList

    # Loads the particular level for the game in a 2D array
    def loadLevel(self, levelArray):
        self.level = self.level + 1
        self.numOfMoves = 0
        self.currentGameArray = levelArray
        self.currentSolution = []
        return self.currentGameArray

    # Loops through a level until the player wins
    def startAIGameLoop(self, currentArray):
        self.getCurrentLocAI()
        root = self.currentGameArray


    def startGameLoop(self, currentLevel):
        self.getCurrentLoc()
        hasWon = False
        move = ' '
        print(self.outputCurrentGame())
        startTime = time.time()
        while hasWon == False:  # Keeps looping until player has won
            print('Make a move based on the blank space (r,l,u,d): ')  # player can move based on empty space
            move = input()
            if (self.isLegal(move) == True):  # Checks if legal
                print(' ')
                self.swap(move)
                #adding 65 to the int in chr will give you the correct A-O ascii
                self.currentSolution.append(chr(self.currentLocation + 65))
                self.numOfMoves = self.numOfMoves + 1
                print(self.outputCurrentGame())
            if (self.winCondition() == True):  # Win condition
                endTime = time.time()
                #times one thousand to get millisecs because the current time is in seconds with decimals
                #then the float is converted to an int
                totalTime = int((endTime - startTime) * 1000)
                self.gameTime.append(totalTime)
                print(' ')
                print('You won Puzzle ' + str(self.level) + '!')
                tempArray = self.currentSolution
                self.currentGameArray[self.currentLocation] = 'e'
                self.completedLevels.append(self.currentGameArray)  # stores the completed states of the puzzles
                self.solutions.append(tempArray)  # stores solution
                self.allMoves.append(self.numOfMoves)  # stores number of moves
                print(' ')
                hasWon = True

    # Outputs the current game board so that the user sees what state the game is in.
    def outputCurrentGame(self):
        print('Puzzle: ' + str(self.level))
        print('Number of moves: ' + str(self.numOfMoves))
        print('---------------------')
        print('| ' + self.currentGameArray[0] + ' | ' + self.currentGameArray[1] + ' | ' + self.currentGameArray[
            2] + ' | ' + self.currentGameArray[3] + ' | ' + self.currentGameArray[4] + ' |')
        print('---------------------')
        print('| ' + self.currentGameArray[5] + ' | ' + self.currentGameArray[6] + ' | ' + self.currentGameArray[
            7] + ' | ' + self.currentGameArray[8] + ' | ' + self.currentGameArray[9] + ' |')
        print('---------------------')
        print('| ' + self.currentGameArray[10] + ' | ' + self.currentGameArray[11] + ' | ' + self.currentGameArray[
            12] + ' | ' + self.currentGameArray[13] + ' | ' + self.currentGameArray[14] + ' |')
        print('---------------------')
        return ' '

    # Checks to make sure the move is legal (based on the empty space movement)
    def isLegal(self, move):
        if move == 'r':  # cannot move right if the empty space is in the last column
            if (self.currentLocation == 4 or self.currentLocation == 9 or self.currentLocation == 14):
                print('**This is an illegal move, try again**')
                print(' ')
                return False
            else:
                return True
        if move == 'l':  # cannot move left if the empty space is in the first column
            if (self.currentLocation == 0 or self.currentLocation == 5 or self.currentLocation == 10):
                print('**This is an illegal move, try again**')
                print(' ')
                return False
            else:
                return True
        if move == 'u':  # cannot move up if the empty space is in the first row
            if (self.currentLocation == 0 or self.currentLocation == 1 or self.currentLocation == 2 or
                    self.currentLocation == 3 or self.currentLocation == 4):
                print('**This is an illegal move, try again**')
                print(' ')
                return False
            else:
                return True
        if move == 'd':  # cannot move down if the empty space is in the last row
            if (self.currentLocation == 10 or self.currentLocation == 11 or self.currentLocation == 12
                    or self.currentLocation == 13 or self.currentLocation == 14):
                print('**This is an illegal move, try again**')
                print(' ')
                return False
            else:
                return True

    #finds current location of empty space. Only needs to be used once
    def getCurrentLoc(self):
        for index in range(len(self.currentGameArray)):
            if self.currentGameArray[index] == 'e':
                self.currentGameArray[index] = ' '
                self.currentLocation = index

    # Swaps the empty space with the other element (moving piece)
    def swap(self, move):

        if move == 'r':
            position = self.currentLocation
            self.currentGameArray[position] = self.currentGameArray[position + 1]
            position = position + 1
            self.currentGameArray[position] = ' '
            self.currentLocation = position
        if move == 'l':
            position = self.currentLocation
            self.currentGameArray[position] = self.currentGameArray[position - 1]
            position = position - 1
            self.currentGameArray[position] = ' '
            self.currentLocation = position

        if move == 'u':
            position = self.currentLocation
            self.currentGameArray[position] = self.currentGameArray[position - 5]
            position = position - 5
            self.currentGameArray[position] = ' '
            self.currentLocation = position

        if move == 'd':
            position = self.currentLocation
            self.currentGameArray[position] = self.currentGameArray[position + 5]
            position = position + 5
            self.currentGameArray[position] = ' '
            self.currentLocation = position

    # Winning condition: the first row is the same as the last row
    def winCondition(self):
        return (self.currentGameArray[0:5]==self.currentGameArray[10:15])


# ===================================Main Program================================================

    def runProgram(self):
        print('Welcome to the Game')
        print(' ')
        print(' ')
        levelNum = 0  # used to indicate current level
        stop = 'n'  # used to indicate when user wants to quit or all levels are done
        #g = Game()
        x = 'InputFile.txt'
        allLevels = self.loadFile(x)  # Loads all levels from file

        while stop == 'n':  # loops each complete level, allows user to quit in between levels.

            print('==============')
            print('Puzzle ' + str(levelNum + 1))
            print('==============')
            print(' ')
            print(' ')

            currentLevel = self.loadLevel(allLevels[levelNum])  # loads level
            self.startGameLoop(currentLevel)  # Starts game loop of current level
            print(' ')
            print(' ')

            if len(allLevels) > (levelNum + 1):  # Asks player if they'd like to quit
                print('Would you like to quit? (enter y or n)')
                stop = input()
            else:
                print('No more puzzles!')  # Quits since there are no more puzzles
                stop = ' '

            print(' ')
            print(' ')
            levelNum = levelNum + 1
        if stop != 'n':
            IO.IO().printResult(self.solutions, self.completedLevels, self.allMoves, self.gameTime)  # Prints to output file
            print('Thanks for playing!')

        print()
        print()
        input('Press ENTER to exit')
