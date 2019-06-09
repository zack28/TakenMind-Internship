import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

s1=Series([500,1000,1500],index=['a','c','b'])
print(s1)

#sorting by index
print(s1.sort_index())

#sort by values
print(s1.sort_values())

#ranking of series
print(s1.rank())
s2=Series(randn(4))
print(s2)

print(s2.rank())