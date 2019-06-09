import numpy as np
import pandas as pd
from pandas import Series,DataFrame
s1=Series(['A','B','C','D','E',np.nan])
print(s1)
#validate
print(s1.isnull())
#drop unavailbale values
print(s1.dropna())

df=DataFrame([[1,2,3],[4,5,np.nan],[7,np.nan,10],[np.nan,np.nan,np.nan]])
print(df)
#drona in dataframe
#print(df.dropna()) #delets the entire row that has atleast one nan entry
print(df.dropna(how="all"))

#dropna corresponding to columns

print(df.dropna(axis=1)) #column vise deletion

df2=DataFrame([[1,2,3,np.nan],[4,5,6,7],[8,9,np.nan,np.nan],[12,np.nan,np.nan,np.nan]])
print(df2)

print(df2.dropna(thresh=3)) #should contain atleast 3 data values (for rows)
print(df2.dropna(thresh=3,axis=1)) #for cols

#fillna

print(df2.fillna('-'))  #fills all the null values by 0
print(df2.fillna({0:0,1:50,2:100,3:200}))  #replaces null value in col 1 by 0, col2 by 50, col3 by 100 and col4 by 200