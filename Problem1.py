import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#QUESTION: If we list all numbers below 10 that are multiples of 3 or 5, we get 3,5,6, and 9. the sum of these multiples is 23. 
#find the sum of all multiples of 3 or 5 below 1000.

#STEPS
#while Y is < 1000
    #if Y is divisible by 3, add Y to X, Y+
    #else
        #if y is divisible by 5, add Y to X, Y+
        #else
            #Y+
#define Global Variable X
#define running variable Y to execute following:

def PE1afunction():
    x=0;
    y=0;
    while y < 1000:
        if (y % 3) == 0:
            x=x+y
            print(y)
        else: 
            if (y % 5) == 0:
                x=x+y
                print(y)
        y+=1
    print(x)

#mPE1function() remove # to execute

#New Function! Let's try to plot it as well. import matplotlib.pyplot

def PE1bfunction():
    x=0;
    y=0;
    Line_X = [0]
    Line_Y = [0]
    Line_X_Axis = list(range(0,1001)
    while y < 1000:
        if (y % 3) == 0:
            x=x+y
            print(y)
        else: 
            if (y % 5) == 0:
                x=x+y
                print(y)
        y+=1
    print(x)
    
