# Jessica Lee
# Assignment 2: Microservices Warm Up

import time, random

while True:
    time.sleep(1)       # Sleep for 1 second
    myFile = open("prng-service.txt", "r")
    toDo = myFile.read()

    if toDo == "run":
        val = random.randrange(10000)
        myNum = val % 209
        myFile.write(myNum)
    myFile.close()