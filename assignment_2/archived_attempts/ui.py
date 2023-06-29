import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

myStatus = True

while myStatus:
    print("Enter 1 to generate a new image, or 2 to exit.")
    time.sleep(0.5)
    option = input('Select your option: \n')

    if option == "1":
        makeRun = open("prng-service.txt", "w")
        makeRun.write("run")
        makeRun.close()
        time.sleep(10)

        readVal = open("prng-service.txt", "r")
        myNum = readVal.read()
        readVal.close()
        putNum = open("image-service.txt", "w")
        strNum = str(myNum)
        putNum.write(strNum)
        putNum.close()
        time.sleep(5)

        myFile = open("image-service.txt", "r")
        pathURL = myFile.read()
        myFile.close()
        print("Your image path URL from the current folder is:", pathURL)

    elif option == "2":
        myStatus = False
    else:
        print("Unknown option selected. Please try again.")