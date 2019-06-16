import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from numpy import random

B1 = np.arange(25).reshape(5,5)
A1 = random.randn(25).reshape(5,5)

print B1
print A1
print "output for axis-1"
print np.concatenate([A1,B1],axis=1)
print np.concatenate([A1,B1],axis=0)

#Series

s1 = Series([100,200,300],index=['A','B','C'])
s2 = Series([400,500],index=['D','E'])

print pd.concat([s1,s2])
print "axis 1"
print pd.concat([s1,s2],axis=1)

#Dataframes

df1 = DataFrame(random.rand(4,3),columns=['A','B','C'])
df2 = DataFrame(random.rand(3,3),columns=['B','D','A'])

print "pd.concat dataframes"
print pd.concat([df1,df2])
print "pd.concat dataframe - continuous index"
print pd.concat([df1,df2],ignore_index=True)

url = "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html"