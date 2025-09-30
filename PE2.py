import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#fibonnaci sequence, sum of even numbers less than 4M

#Make algo for fibbonnaci
#if number is divisible by 2, add to vector
#while until fibb run is > 4M



def PE2function():
    w=0;
    x=1;
    y=1;
    z=0;
    #FibVector Create
    fibvec = [0]
    #Line_X = [0]
    #Line_Y = [0]
    #Line_X_Axis = list(range(0,1001)
    while y < 4000000:
        fibvec.append(y)
        y=y+fibvec[-2]
        print(fibvec)
        if (y % 2 == 0):
            z += y
    print(z)

PE2function()
