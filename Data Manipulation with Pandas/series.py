import pandas as pd
import numpy as np
from pandas import Series

s=Series([5,10,15,20])
print("Series=",s)
print("Values=",s.values)
print("Index=",s.index)

#use numpy arrays to create series
data=np.array(['a','b','c'])
s1=Series(data)
print(s1)

#custom indexes
s1=Series(data,index=[100,101,102])
print("Customized Series Index=",s1)

s=Series(data,index=['A','E','I'])
print(s)

#using real life example

rev=Series([20,80,40,35],index=['Ola','Uber','grap','gojek'])
print(rev)

#using index to access values
print(rev['Ola'])
#usinh condition within series

print(rev[rev>30])

#using boolean conditions

print( 'Ola' in rev)
print('Car' in rev)

#conver series into dictionary

rev_dict=rev.to_dict()
print(rev_dict)

#nan values(not available values)
index2=['Ola','Uber','grap','gojek','lyft']
rev2=Series(rev,index2)
print(rev2)

print(pd.isnull(rev2))
print(pd.notnull(rev2))
#addition of series
print(rev+rev2)

#assigning names
rev2.name="Company Revenues"
rev2.index.name="Company Name"
print(rev2)