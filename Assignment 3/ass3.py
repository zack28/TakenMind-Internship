import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import seaborn as sb
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

df1=pd.read_csv('FiveYearData.csv')  #read the csv file
print(df1)
print(df1.duplicated().value_counts())
df2=df1[['continent','year','lifeExp']]  #extract the needed columns from the dataset
print(df2)

df3=pd.pivot_table(df2,index='continent',columns='year',values='lifeExp')  #create a pivot table
print(df3)

sb.heatmap(df3,annot=True).get_figure().savefig('HeatMap.png')  #create a heatmap of the pivot table.