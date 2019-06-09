import pandas as pd
import numpy as np
from pandas import  Series, DataFrame

s1= Series([100,200,300],index=['A','B','C'])
print(s1)
#access element of series

print(s1['A'])
#access multiple elements
print(s1[['A','B']])

#number indexes
print(s1[0]) #equivalent to s1['A']
#aceesing multiple elements
print(s1[0:2])
print(s1[0:4])

#conditional indexes
print(s1[s1>150])
print(s1[s1==300])

#using datframes
df1=DataFrame(np.arange(9).reshape(3,3),index=['Car','Bike','Cycle'],columns=['A','B','C'])
print(df1)

#col wise
print(df1['A'])
print(df1[['A','B']]) #multiple values

print(df1>5)

#access elements using ix function

print(df1.loc['Bike'])
