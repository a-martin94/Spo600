import re

fileName = "function_ifunc.c"
f = open("function.c", "r")
#x = open("function.c", "r")

orgLine =""
name = ""
dataType = ""
topPart =""
bottomPart = ""
count = 0

for line in f:
    count = count + 1
    a = line.strip()
    if re.search("^void.", a):
        orgLine = a
        dataType = re.split("\s", a, 1) 
        print(dataType[0])
        name = re.split("\(", dataType[1], 1)
        #print("Name of func is " + name[0])

        nextLine = f.readline()

        while not re.search(".{.?", nextLine):
            orgLine += nextLine.strip() + " "
            nextLine = f.readline()   
        
      
        l = re.split(".{.?", nextLine, 1)
        orgLine += l[0].strip() 
        print(orgLine)
        a = ""
        break

    topPart += a + "\n"

#testing
protoType = "#include <sys/auxv.h>\n#include <stdio.h>\n\n" + orgLine + " __attribute__(( ifunc(\"magic_resolver\") ));" + "\n\n"


# will store the contents of file
content = ""

typeCount = 3
# suffix for each function
types = ["sve2", "sve", "asimd"]
targets = ["#pragma GCC target \"arch=armv8-a+sve2\"", "#pragma GCC target \"arch=armv8-a+sve\"", "#pragma GCC target \"arch=armv8-a\""]

bustedUp = re.split("\(", orgLine, 1)
paramList = "(" + bustedUp[1]
#lineToInsert = dataType[0] + " " + name[0] + paramList + "\n"
lineToInsert = ""
# get all lines under prototype of function
for line in f:
    bottomPart += line


#only out put the top half

output = open(fileName, "w")
output.write(protoType)

for x in range(typeCount):
    lineToInsert += targets[x] + "\n\n" 
    lineToInsert += topPart + "\n\n"
    lineToInsert += dataType[0] + " " + name[0] + "_" + types[x] +  paramList + "{"+ "\n"
    content += "\n" + lineToInsert + bottomPart 
    content += "\n\n\n"
    lineToInsert = ""

output.write(content)
output.close()

f = open("resolver.c", "r")
output = open(fileName, "a")
content =""
for line in f :
    content += line


output.write(content)
f.close()
output.close()