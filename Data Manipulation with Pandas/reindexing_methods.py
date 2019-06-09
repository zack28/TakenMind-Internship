import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

#create a new series
s1=Series([1,2,3,4],index=['e','f','g','h'])
print(s1)

#creating new indexes using reindex

s2=s1.reindex(['e','f','g','h','i','j'])
print(s2)

#using fill value
s2=s2.reindex(['e','f','g','h','i','j','k'],fill_value=10)
print(s2)

#using ffill
cars=Series(['Audi','BMW','Honda'],index=[0,4,8])
print(cars)
ranger=range(13)
print(ranger)
cars=cars.reindex(ranger,method="ffill")
print(cars)

#create new df suing random
#reindex rows of data frame
df1=DataFrame(randn(25).reshape(5,5),index=['a','b','c','d','e'],columns=['c1','c2','c3','c4','c5'])
print(df1)
df2=df1.reindex(['a','b','c','d','e','f'])
print(df2)
#reindex cols
df3=df2.reindex(columns=['c1','c2','c3','c4','c5','c6'])
print(df3)

#using ix[] to reindex

df4=df1.loc[['a','b','c','d','e','f'],['c1','c2','c3','c4','c5','c6']]
print(df4)