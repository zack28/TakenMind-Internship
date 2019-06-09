import pandas as pd
#exlrd
#openpyxl
ex=pd.ExcelFile('demo2.xlsx')
df=ex.parse('demo2')
print(df)
