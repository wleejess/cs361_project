import time, os

myStatus = True

while myStatus:
    print("Enter 1 to generate a new image, or 2 to exit.")
    time.sleep(1)
    option = input('Select your option: \n')

    if option == "1":
        makeRun = open("prng-service.txt", "w")
        makeRun.write("run")
        time.sleep(5)

        readVal = open("prng-service.txt", "r")
        myNum = readVal.read()
        putNum = open("image-service.txt", "w")
        strNum = str(myNum)
        putNum.write(strNum)
        time.sleep(5)

        myFile = open("image-service.txt", "r")
        pathURL = myFile.read()
        print("Your image path URL is:", pathURL)
        myFile.close()
        makeRun.close()
    elif option == "2":
        myStatus = False
    else:
        print("Unknown option selected. Please try again.")