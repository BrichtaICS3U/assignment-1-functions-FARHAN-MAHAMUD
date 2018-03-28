# Assignment 1
# ICS3U
# <Farhan Mahamud>
# March 28, 2018

import math

###### uncomment this when you are ready to work on it
def CtoF (C):
    """ C = Celsius, this function is used to convert degrees celsius into degrees Fahrenheit"""
    F = (1.8)*C+32
    return math.ceil(F)


###### uncomment this when you are ready to work on it
def FtoC (F):
    """F = Fahrenheit, this function is to convert degrees Fahrenheit into degrees celsius"""
    C = (0.55556)*(F-32)
    return math.ceil(C)
    if C <= -273.15:
        print("Invalid Value")


user = int(input("1 for CtoF, 2 for FtoC: "))
temperature = int(input('Enter your temperature in Celsius: '))
if user == 1:
           print(CtoF(temperature))
elif user == 2:
    if (FtoC(temperature)) >= -273.15:
        print(FtoC(temperature))
    elif (FtoC(temperature)) <= -273.15:
               print("Invalid Value")
