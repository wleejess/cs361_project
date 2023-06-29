# Jessica Lee
# Program to read from a file. If the file says "run", generates a 
# random integer between 0-209 (since we have 210 images), and 
# overwrites the current text file to contain the number instead.

import time, random

while True:
    time.sleep(1)       # Sleep for 1 second
    myFile = open("prng-service.txt", "r")
    toDo = myFile.read()

    if toDo == "run":
        myFile.close()
        myFile = open("prng-service.txt", "w")
        val = random.randrange(10000)
        myFile.write(str(val))
    myFile.close()