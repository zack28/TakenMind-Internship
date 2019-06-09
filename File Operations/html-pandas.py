import pandas as pd
from pandas import DataFrame,read_html
url='https://countrycode.org/'
dflist=pd.io.html.read_html(url)
df=dflist[0]
print(df)
print(df.columns.values)
df.to_excel('ex1.xlsx')

