import IO


class Game:
    numOfMoves = 0
    currentGameArray = []
    level = 0
    completedLevels = []
    currentSolution = []
    solutions = []
    allMoves = []
    currentLocation = 0

    # Loads all the levels from the file
    def loadFile(fileName):
        tempList = IO.IO().readInitial(fileName)
        return tempList

    # Loads the particular level for the game in a 2D array
    def loadLevel(levelArray):
        Game.level = Game.level + 1
        for index in range(len(levelArray)):  # Checks for 'e' in the array and turns it into an empty string
            if levelArray[index] == 'e':
                levelArray[index] = ' '
        Game.numOfMoves = 0
        Game.currentGameArray = levelArray
        Game.currentSolution = []
        return Game.currentGameArray

    # Loops through a level until the player wins
    def startGameLoop(currentLevel):
        Game.getCurrentLoc()
        hasWon = False
        move = ' '
        print(Game.outputCurrentGame())
        while hasWon == False:  # Keeps looping until player has won
            print('Make a move based on the blank space (r,l,u,d): ')  # player can move based on empty space
            move = input()
            if (Game.isLegal(move) == True):  # Checks if legal
                print(' ')
                Game.swap(move)
                Game.currentSolution.append(chr(Game.currentLocation + 65))
                Game.numOfMoves = Game.numOfMoves + 1
                print(Game.outputCurrentGame())
            if (Game.winCondition() == True):  # Win condition
                print(' ')
                print('You won Puzzle ' + str(Game.level) + '!')
                tempArray = Game.currentSolution
                for index in range(len(Game.currentGameArray)):  # Checks for ' ' in the array and turns it into 'e'
                    if Game.currentGameArray[index] == ' ':
                        Game.currentGameArray[index] = 'e'
                Game.completedLevels.append(Game.currentGameArray)  # stores the completed states of the puzzles
                Game.solutions.append(tempArray)  # stores solution
                Game.allMoves.append(Game.numOfMoves)  # stores number of moves
                print(' ')
                hasWon = True

    # Outputs the current game board so that the user sees what state the game is in.
    def outputCurrentGame():
        print('Puzzle: ' + str(Game.level))
        print('Number of moves: ' + str(Game.numOfMoves))
        print('---------------------')
        print('| ' + Game.currentGameArray[0] + ' | ' + Game.currentGameArray[1] + ' | ' + Game.currentGameArray[
            2] + ' | ' + Game.currentGameArray[3] + ' | ' + Game.currentGameArray[4] + ' |')
        print('---------------------')
        print('| ' + Game.currentGameArray[5] + ' | ' + Game.currentGameArray[6] + ' | ' + Game.currentGameArray[
            7] + ' | ' + Game.currentGameArray[8] + ' | ' + Game.currentGameArray[9] + ' |')
        print('---------------------')
        print('| ' + Game.currentGameArray[10] + ' | ' + Game.currentGameArray[11] + ' | ' + Game.currentGameArray[
            12] + ' | ' + Game.currentGameArray[13] + ' | ' + Game.currentGameArray[14] + ' |')
        print('---------------------')
        return ' '

    # Checks to make sure the move is legal (based on the empty space movement)
    def isLegal(move):
        if move == 'r':  # cannot move right if the empty space is in the last column
            if (Game.currentLocation == 4 or Game.currentLocation == 9 or Game.currentLocation == 14):
                print('**This is an illegal move, try again**')
                print(' ')
                return False
            else:
                return True
        if move == 'l':  # cannot move left if the empty space is in the first column
            if (Game.currentLocation == 0 or Game.currentLocation == 5 or Game.currentLocation == 10):
                print('**This is an illegal move, try again**')
                print(' ')
                return False
            else:
                return True
        if move == 'u':  # cannot move up if the empty space is in the first row
            if (Game.currentLocation == 0 or Game.currentLocation == 1 or Game.currentLocation == 2 or
                    Game.currentLocation == 3 or Game.currentLocation == 4):
                print('**This is an illegal move, try again**')
                print(' ')
                return False
            else:
                return True
        if move == 'd':  # cannot move down if the empty space is in the last row
            if (Game.currentLocation == 10 or Game.currentLocation == 11 or Game.currentLocation == 12
                    or Game.currentLocation == 13 or Game.currentLocation == 14):
                print('**This is an illegal move, try again**')
                print(' ')
                return False
            else:
                return True

    #finds current location of empty space. Only needs to be used once
    def getCurrentLoc():
        tempArray = Game.currentGameArray
        for index in range(len(tempArray)):
            if tempArray[index] == ' ':
                Game.currentLocation = index


    # Swaps the empty space with the other element (moving piece)
    def swap(move):

        if move == 'r':
            position = Game.currentLocation
            Game.currentGameArray[position] = Game.currentGameArray[position + 1]
            position = position + 1
            Game.currentGameArray[position] = ' '
            Game.currentLocation = position
        if move == 'l':
            position = Game.currentLocation
            Game.currentGameArray[position] = Game.currentGameArray[position - 1]
            position = position - 1
            Game.currentGameArray[position] = ' '
            Game.currentLocation = position

        if move == 'u':
            position = Game.currentLocation
            Game.currentGameArray[position] = Game.currentGameArray[position - 5]
            position = position - 5
            Game.currentGameArray[position] = ' '
            Game.currentLocation = position

        if move == 'd':
            position = Game.currentLocation
            Game.currentGameArray[position] = Game.currentGameArray[position + 5]
            position = position + 5
            Game.currentGameArray[position] = ' '
            Game.currentLocation = position


    # Winning condition: the first row is the same as the last row
    def winCondition():
        if (Game.currentGameArray[0] == Game.currentGameArray[10] and
                Game.currentGameArray[1] == Game.currentGameArray[11] and
                Game.currentGameArray[2] == Game.currentGameArray[12] and
                Game.currentGameArray[3] == Game.currentGameArray[13] and
                Game.currentGameArray[4] == Game.currentGameArray[14]):
            return True
        else:
            return False


# ===================================Main Program================================================
print('Welcome to the Game')
print(' ')
print(' ')
levelNum = 0  # used to indicate current level
stop = 'n'  # used to indicate when user wants to quit or all levels are done
allLevels = Game.loadFile('InputFile.txt')  # Loads all levels from file

while stop == 'n':  # loops each complete level, allows user to quit in between levels.

    print('==============')
    print('Puzzle ' + str(levelNum + 1))
    print('==============')
    print(' ')
    print(' ')

    currentLevel = Game.loadLevel(allLevels[levelNum])  # loads level
    Game.startGameLoop(currentLevel)  # Starts game loop of current level
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
        IO.IO().printResult(Game.solutions, Game.completedLevels, Game.allMoves)  # Prints to output file
        print('Thanks for playing!')

print()
print()
input('Press ENTER to exit')
