#Reshaping Datasets
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(8).reshape(2,4), index=pd.Index(['Uber','Grab'],name="cabs"), columns=pd.Index(['c1','c2','c3','c4'],name="attributes"))
print df1

stackdf1 = df1.stack()
print stackdf1

df1unstack = stackdf1.unstack()
print df1unstack

df3 = stackdf1.unstack('cabs')
print df3

df4 = stackdf1.unstack('attributes')
print df4

#Series

s1 = Series([5,10,15],index=['A','B','C'])
s2 = Series([15,20,25],index=['B','C','D'])

s3 = pd.concat([s1,s2],keys=['k1','k2'])
print s3

df = s3.unstack()
print df

print df.stack()

print df.stack(dropna=False)

