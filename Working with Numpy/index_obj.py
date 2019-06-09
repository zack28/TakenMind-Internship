import numpy as np
import pandas as pd
from pandas import Series,DataFrame

s1=Series([10,20,30,40],index=['A','B','C','D'])
print(s1)

index1=s1.index
print(index1)

#index operations
print(index1[2])
print(index1[2:])

#negative indexes
print(index1[-2:]) #ignores the first 2 elemnts and prints the rest
print(index1[:-2]) #ignores the last 2 elemnts and prints the rest

#range of indexes
print(index1[1:4])

#interesting

#index1[0]='a'  #index cannot be changed using =  operator
#print(index1)