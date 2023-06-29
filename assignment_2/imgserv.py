# Jessica Lee
# Program to read from a file. If the file contains a number,
# uses the mod operation to ensure that it is within range[0, 209].
# Afterwards, updates the file to contain the resulting value.

import time

while True:
    time.sleep(1)       # Sleep for 1 second
    myFile = open("image-service.txt", "r")
    toDo = myFile.read()

    if toDo.isnumeric():
        myNum = int(toDo)
        myFile.close()
        myFile = open("image-service.txt", "w")
        myNum = str(myNum % 209)
        if len(myNum) == 1:
            modifiedNum = "000" + str(myNum)
        elif len(myNum) == 2:
            modifiedNum = "00" + str(myNum)
        elif len(myNum) == 3:
            modifiedNum = "0" + str(myNum)
        filePath = "images/" + modifiedNum + ".png"
        print(filePath)
        myFile.write(filePath)
    myFile.close()