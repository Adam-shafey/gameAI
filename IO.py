class IO(object):

    @staticmethod
    def readInitial(fileName=None): #defaults to Untitled.txt
        data = []
        if fileName:
            filename=fileName
        else:
            filename = "Untitled.txt"
        with open(filename, 'r') as fobj:
            for line in fobj:
                lineData = [letter for letter in line.split()]
                data.append(lineData)
                #print(data)
        return data

    #solution is a list of arrays with the solution path
    #result is a list of arrays that contain letters (state of the solution)
    #numOfMoves is an array of the num of moves performed in each puzzle
    #time is optional.
    @staticmethod
    def printResult(solution, result, numOfMoves, timeTaken):
        thefile = open('Output.txt', 'w')
        for index in range(len(solution)): #Loops through solutions
            thefile.write("Puzzle: " + str(index + 1))
            thefile.write("\n")
            thefile.write("Solution: ")
            for item in solution[index]:
                thefile.write(item.capitalize())
                thefile.write(' ')
            thefile.write("\n")
            thefile.write("Result: ")
            for item in result[index]:
                thefile.write(item.capitalize())
                thefile.write(' ')
            if(timeTaken):
                thefile.write("\n" + "Time: ")
                thefile.write("%s" % timeTaken[index] + "ms")
            thefile.write("\n")
            thefile.write("Number of Moves: " + str(numOfMoves[index]))
            thefile.write("\n")
            thefile.write("\n")
        thefile.write("\n")

    @staticmethod
    def printResult2(solution, result, numOfMoves, allGrids, *timeTaken):
        thefile = open('Output.txt', 'w')
        for index in range(len(solution)): #Loops through solutions
            for i in range(len(allGrids)):
                thefile.write('Number of moves: ' + str(i))
                thefile.write('---------------------' + '\n')
                thefile.write(
                    '| ' + allGrids[i][0] + ' | ' + allGrids[i][1] + ' | ' + allGrids[i][
                        2] + ' | ' + allGrids[i][3] + ' | ' + allGrids[i][4] + ' |' + '\n')
                thefile.write('---------------------' + '\n')
                thefile.write(
                    '| ' + allGrids[i][5] + ' | ' + allGrids[i][6] + ' | ' + allGrids[i][
                        7] + ' | ' + allGrids[i][8] + ' | ' + allGrids[i][9] + ' |' + '\n')
                thefile.write('---------------------' + '\n')
                thefile.write('| ' + allGrids[i][10] + ' | ' + allGrids[i][11] + ' | ' +
                      allGrids[i][
                          12] + ' | ' + allGrids[i][13] + ' | ' + allGrids[i][14] + ' |' + '\n')
                thefile.write('---------------------' + '\n')
                thefile.write("\n")


            thefile.write("Puzzle: " + str(index + 1))
            thefile.write("\n")
            thefile.write("Solution: ")
            for item in solution[index]:
                thefile.write(item.capitalize())
                thefile.write(' ')
            thefile.write("\n")
            thefile.write("Result: ")
            for item in result[index]:
                thefile.write(item.capitalize())
                thefile.write(' ')
            thefile.write("\n")
            thefile.write("Number of Moves: " + str(numOfMoves[index]))
            thefile.write("\n")
            thefile.write("\n")
        thefile.write("\n")
        if (timeTaken):
            thefile.write("\n" + "Time: ")
            thefile.write("%s" % timeTaken + "ms")
        thefile.write("\n")
        sum = 0
        for index in range(len(numOfMoves)):
            sum = sum + numOfMoves[index]
        thefile.write("Total Number of Moves: " + str(sum))
        thefile.write("\n")