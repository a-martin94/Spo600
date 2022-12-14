import re

def whichOne(line, dataTypes):
    
    for i in range(len(dataTypes)):
        if re.search("^" + dataTypes[i] + ".", line):
            return i

    return -1