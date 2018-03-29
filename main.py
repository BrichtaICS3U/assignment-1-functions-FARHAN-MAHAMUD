# Assignment 1
# ICS3U
# <Farhan Mahamud>
# March 28, 2018

import math

###### uncomment this when you are ready to work on it
def CtoF (C):
    """ C = Celsius, this function is used to convert degrees celsius into degrees Fahrenheit"""
    F = (1.8)*C+32
    return round(F)


###### uncomment this when you are ready to work on it
def FtoC (F):
    """F = Fahrenheit, this function is to convert degrees Fahrenheit into degrees celsius"""
    C = (0.55556)*(F-32)
    return round(C)
    if C <= -273.15:
        print("Invalid Value")


Redo = int(input("1 to do another temperature convertion, 2 to stop: "))
while Redo == 1:
    user = int(input("1 for CtoF, 2 for FtoC: "))
    temperature = int(input('Enter your temperature in Celsius: '))
    while (CtoF(temperature)) >= -459.67:
        if user == 1 and Redo == 1:
            if(CtoF(temperature)) >= -459.67:
                print(CtoF(temperature))
            elif(CtoF(temperature)) <= -459.67:
                print("Invalid Value")
        elif user == 2:
            if (FtoC(temperature)) >= -273.15:
                print(FtoC(temperature))
            elif (FtoC(temperature)) <= -273.15:
                print("Invalid Value")
        Redo = int(input("1 to do another temperature convertion, 2 to stop: "))
        if Redo == 2:
            print("SHUT DOWN")
