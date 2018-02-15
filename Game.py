import IO

class Game:

    numOfMoves = 0
    currentGameArray = [[0 for x in range(5)] for y in range(3)]

    #Loads all the levels from the file
    def loadFile(fileName):
        tempList = IO.IO().readInitial(fileName)
        return tempList

    #Loads the particular level for the game in a 2D array
    def loadLevel(levelArray):
        for index in range(len(levelArray)): #Checks for 'e' in the array and turns it into an empty string
            if levelArray[index] == 'e':
                levelArray[index] = ' '       
        temparray = [[0 for x in range(5)] for y in range(3)] 
        temparray[0][0] = levelArray[0]
        temparray[0][1] = levelArray[1]
        temparray[0][2] = levelArray[2]
        temparray[0][3] = levelArray[3]
        temparray[0][4] = levelArray[4]
        temparray[1][0] = levelArray[5]
        temparray[1][1] = levelArray[6]
        temparray[1][2] = levelArray[7]
        temparray[1][3] = levelArray[8]
        temparray[1][4] = levelArray[9]
        temparray[2][0] = levelArray[10]
        temparray[2][1] = levelArray[11]
        temparray[2][2] = levelArray[12]
        temparray[2][3] = levelArray[13]
        temparray[2][4] = levelArray[14]
        Game.numOfMoves = 0
        Game.currentGameArray = temparray
        return temparray
    
    #Outputs the current game board so that the user sees what state the game is in.
    def outputCurrentGame():
        print('Number of moves: ' + str(Game.numOfMoves))
        print('---------------------')
        print('| ' + Game.currentGameArray[0][0] + ' | ' + Game.currentGameArray[0][1] + ' | ' + Game.currentGameArray[0][2] + ' | ' + Game.currentGameArray[0][3] + ' | ' + Game.currentGameArray[0][4] + ' |')
        print('---------------------')
        print('| ' + Game.currentGameArray[1][0] + ' | ' + Game.currentGameArray[1][1] + ' | ' + Game.currentGameArray[1][2] + ' | ' + Game.currentGameArray[1][3] + ' | ' + Game.currentGameArray[1][4] + ' |')
        print('---------------------')
        print('| ' + Game.currentGameArray[2][0] + ' | ' + Game.currentGameArray[2][1] + ' | ' + Game.currentGameArray[2][2] + ' | ' + Game.currentGameArray[2][3] + ' | ' + Game.currentGameArray[2][4] + ' |')
        print('---------------------')
        return ' '

    #Checks to make sure the move is legal (based on the empty space movement)
    def isLegal(move):
        if move == 'r': #cannot move if the empty space is in the last column
            if(Game.currentGameArray[0][4] == ' ' or Game.currentGameArray[1][4] == ' ' or Game.currentGameArray[2][4] == ' '):
                print('This is an illegal move, try again')
                print(' ')
                return False
            else:
                return True
        if move == 'l': #cannot move if the empty space is in the first column
            if(Game.currentGameArray[0][0] == ' ' or Game.currentGameArray[1][0] == ' ' or Game.currentGameArray[2][0] == ' '):
                print('This is an illegal move, try again')
                print(' ')
                return False
            else:
                return True
        if move == 'u': #cannot move if the empty space is in the first row
            if(Game.currentGameArray[0][0] == ' ' or Game.currentGameArray[0][1] == ' ' or Game.currentGameArray[0][2] == ' ' or Game.currentGameArray[0][3] == ' ' or Game.currentGameArray[0][4] == ' '):
                print('This is an illegal move, try again')
                print(' ')
                return False
            else:
                return True
        if move == 'd': #cannot move if the empty space is in the last row
            if(Game.currentGameArray[2][0] == ' ' or Game.currentGameArray[2][1] == ' ' or Game.currentGameArray[2][2] == ' ' or Game.currentGameArray[2][3] == ' ' or Game.currentGameArray[2][4] == ' '):
                print('This is an illegal move, try again')
                print(' ')
                return False
            else:
                return True
 
print('Welcome to the Game')
print(' ')
print(' ')
levelNum = 0 #used to indicate current level
stop = 'n' #used to indicate when user wants to quit or all levels are done
allLevels = Game.loadFile('InputFile.txt')#Loads all levels from file


#loops each complete level, allows user to quit in between levels.
while stop == 'n':
    hasWon = False
    move = ' '
    print('==============')
    print('Level ' + str(levelNum + 1))
    print('==============')
    print(' ')
    print(' ')
    currentLevel = Game.loadLevel(allLevels[levelNum]) #loads level
    print(Game.outputCurrentGame())
    while hasWon == False:                              #Keeps looping until player has won
        print('Make a move based on the blank space (r,l,u,d): ') #player can move based on empty space 
        move = input()
        if(Game.isLegal(move) == True):
            print('Legal move')
            print(' ')
            Game.numOfMoves = Game.numOfMoves + 1
            print(Game.outputCurrentGame())
            
    print(' ')
    print(' ')
    if len(allLevels) > (levelNum + 1):      #Asks player if they'd like to quit
        print('Would you like to quit? (enter y or n)')
        stop = input()
    else:
        print('No more levels!')            #Quits since there are no more levels
        stop = ' '
    print(' ')
    levelNum = levelNum + 1
    if stop != 'n':
        print('Thanks for playing!')
    
print()
print()
input('Press ENTER to exit')
