import pandas as pd
import numpy as np
from pandas import Series,DataFrame

#revenue of companies

df=pd.read_clipboard()
print(df)
#access indexes and columns
print(df.columns)
print(df['Industry'])

#multiple columns
print(DataFrame(df,columns=['Rank','Industry','Name']))
#nan values
df2=DataFrame(df,columns=['Rank','Industry','Name','Profit'])
print("New dataFrame=")
print(df2)

#head and tail

print(df2.head(4))  #prints first 5 rows
print(df2.tail(4))  #prints last 5 rows

#access rows in dataframe
#print(df.ix[0]) #does not work
print(df.iloc[0])  #first row
print(df.loc[5])  #5th row

#assign values to dataframe
#using numpy
a1=np.array([1,2,3,4,5,6,7,8])
df2['Profit']=a1
print(df2)

#using series

profit=Series([900,100],index=[3,5])
df2['Profit']=profit
print(df2)

#deletion
del df2['Profit']
print(df2)

#use dictionary with dataframe

sample= {
    'Company':['A','B'],
    'Profit':[1000,5000]
}
print(sample)
dict_df=DataFrame(sample)
print(dict_df)