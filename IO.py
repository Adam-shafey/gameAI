class IO(object):

    @staticmethod
    def readInitial(fileName=None): #defaults to Untitled.txt
        data=[]
        if fileName:
            filename=fileName
        else:
            filename="Untitled.txt"
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