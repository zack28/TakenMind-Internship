import pandas as pd
import numpy as np
from pandas import DataFrame,read_html
#url='https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets'
excel=pd.ExcelFile('InputFile.xlsx')

#read excel file
df1=pd.read_excel(excel,'Sheet1')
#convert excel to csv
df1.to_csv('csv1.csv',sep=',')
csv1=pd.read_csv('csv1.csv')

#read excel file
df2=pd.read_excel(excel,'Sheet2')
#convert excel to csv
df2.to_csv('csv2.csv',sep=',')
csv2=pd.read_csv('csv2.csv')

#read excel file
df3=pd.read_excel(excel,'Sheet3')
#convert excel to csv
df3.to_csv('csv3.csv',sep=',')
csv3=pd.read_csv('csv3.csv')

#read excel file
df4=pd.read_excel(excel,'Sheet4')
#convert excel to csv
df4.to_csv('csv4.csv',sep=',')
csv4=pd.read_csv('csv4.csv')

#read excel file
df5=pd.read_excel(excel,'Sheet5')
#convert excel to csv
df5.to_csv('csv5.csv',sep=',')
csv5=pd.read_csv('csv5.csv')

#read excel file
df6=pd.read_excel(excel,'Sheet6')
#convert excel to csv
df6.to_csv('csv6.csv',sep=',')
csv6=pd.read_csv('csv6.csv')

#read excel file
df7=pd.read_excel(excel,'Sheet7')
#convert excel to csv
df7.to_csv('csv7.csv',sep=',')
csv7=pd.read_csv('csv7.csv')

#read excel file
df8=pd.read_excel(excel,'Sheet8')
#convert excel to csv
df8.to_csv('csv8.csv',sep=',')
csv8=pd.read_csv('csv8.csv')

#read excel file
df9=pd.read_excel(excel,'Sheet9')
#convert excel to csv
df9.to_csv('csv9.csv',sep=',')
csv9=pd.read_csv('csv9.csv')

#read excel file
df10=pd.read_excel(excel,'Sheet10')
#convert excel to csv
df10.to_csv('csv10.csv',sep=',')
csv10=pd.read_csv('csv10.csv')

print(csv1)