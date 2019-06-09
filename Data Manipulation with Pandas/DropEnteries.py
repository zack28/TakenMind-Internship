import pandas as pd
import numpy as np
from pandas import Series,DataFrame

cars=Series(['BMW','Audi','Honda'],index=['a','b','c'])
print(cars)

#drop enteries
cars=cars.drop('a')
print(cars)
#df
cars_df=DataFrame(np.arange(9).reshape(3,3),index=['BMW','Audi','Honda'],columns=['rev','profit','expenses'])
print(cars_df)

#drop rows
cars_df=cars_df.drop('BMW',axis=0)
print(cars_df)
#drop cols
cars_df=cars_df.drop('profit',axis=1)  #axis=0 for index
print(cars_df)                         #axis=1 for columns
