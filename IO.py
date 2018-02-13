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
                print(data)
        return data

    @staticmethod
    def printResult(result, timeTaken=None):#time is optional & result is an array of letters in the form of strings
        thefile = open('Output.txt', 'w')
        for item in result:
            thefile.write(item.capitalize())
        if(timeTaken):
            thefile.write("\n")
            thefile.write("%s" % timeTaken + "ms")
        thefile.write("\n")
