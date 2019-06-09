import pandas as pd
import numpy as np
from pandas import Series,DataFrame
df=pd.read_csv('demo.csv', header=None)
print(df.head())
df2=pd.read_table('demo.csv',sep=',',header=None)
print(df)

#partial row importing
print(pd.read_csv('demo.csv',nrows=2,header=None))
#dump
df2.to_csv('Output_csv.csv',sep='!')

#select specific file
df.to_csv('Data_Output.csv',columns=[0,1])