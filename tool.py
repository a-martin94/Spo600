import re

f = open("function.c", "r")
count = 0
'''for x in f:
    count += 1

print(count)
f.seek(0)
for line in f:
    print(line)
'''

orgLine =""
name = ""
dataType = ""
#topPart =""


for line in f:
    count = count + 1
    a = line.strip()
    if re.search("^void.", a):
        orgLine = a
        dataType = re.split("\s", a, 1) 
        print(dataType[0])
        name = re.split("\(", dataType[1], 1)
        print("Name of func is " + name[0])
        
        
        
        '''nextLine = f.readline()
        orgLine += nextLine
        print(orgLine)
        
        '''
        '''if re.search(".{.?", "orgLine{"):
            print("Found")
        else:
            print("not found")
        break
        '''
        
        nextLine = f.readline()

        while not re.search(".{.?", nextLine):
            orgLine += nextLine.strip() + " "
            nextLine = f.readline()   
        
      
        l = re.split(".{.?", nextLine, 1)
        orgLine += l[0].strip() 
        print("Prototype: " + orgLine)
        break




f = open("header.c", "w")
content = "__attribute__ (( ifunc(magic_resolver) )) ("+ orgLine + ") " + "\n\n#pragma GCC target arch=armv8-a"
f.write(content)



code = open("function.c", "r")
f = open("header.c", 'a+')
f.write(code.read())

#to add suffex
sve = "_sve"
sveTwo = "_sve2"
asmid = "asmid"
r = re.split("\(", orgLine)
#print(dataType[0] + " " + name[0] + sve + "(" + r[1])
sve_ = dataType[0] + " " + name[0] + sve + "(" + r[1]
sveTwo = dataType[0] + " " + name[0] + sveTwo + "(" + r[1]
sveTwo = dataType[0] + " " + name[0] + asmid + "(" + r[1]

includes = " #include <stdio.h>\n #include <stdlib.h>\n #include <stdint.h>\n // -------------------------------------------------------------------- Naive implementation in C\n #if ADJUST_CHANNEL_IMPLEMENTATION == 1\n #include <sys/param.h>\n"
loopStatment = "       for (int i = 0; i < x_size * y_size * 3; i += 3) {\n image[i]   = MIN((float)image[i]   * red_factor,   255);\nimage[i+1] = MIN((float)image[i+1] * blue_factor,  255);\nimage[i+2] = MIN((float)image[i+2] * green_factor, 255);\n}\n}"

#Append the prefix to the name.

code = open("function.c", "r")
f = open("header.c", 'a+')
f.write(code.read() + includes + "\n" + sve_ + " {" + "\n\n" + loopStatment)

code = open("function.c", "r")
f = open("header.c", 'a+')
f.write(code.read() + includes + "\n" + sveTwo + " {" + "\n\n" + loopStatment)

code = open("function.c", "r")
f = open("header.c", 'a+')
f.write(code.read() + includes + "\n" + asmid + " {" + "\n\n" + loopStatment)



#for line in range(count):


        


        
