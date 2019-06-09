import pandas as pd
import  numpy as np
from pandas import Series,DataFrame
s1= Series([100,200,300],index=['A','B','C'])
s2= Series([300,400,500,600],index=['A','B','C','D'])
print("Sum of Series=",s1+s2)

#datframe
df1=DataFrame(np.arange(4).reshape(2,2),index=['Car','Bike'],columns=['A','B'])
df2=DataFrame(np.arange(9).reshape(3,3),index=['Car','Bike','Boat'],columns=['A','B','C'])
print("Df1\n",df1)
print("Df2\n",df2)
print("Sum of DataFrames\n",df1+df2)

df1=df1.add(df2,fill_value=0)
print(df1)

s3=df2.iloc[0]
print(df2-s3)