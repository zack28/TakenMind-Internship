from pandas import Series,DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

array1 = np.array([[10,np.nan,20],[30,40,np.nan]])
print (array1)
df1 = DataFrame(array1,index=[1,2],columns=list('ABC'))
print (df1)

#sum()
print ("Sum of cols",df1.sum()) #sums along each column
print(df1.sum(axis=1)) #sum along indexes

print ("Min",df1.min())
print ("Max",df1.max())

print(df1.idxmax())
print (df1.cumsum())
print (df1.describe())

df2 = DataFrame(randn(9).reshape(3,3),index=[1,2,3],columns=list('ABC'))
print (df2)

plt.plot(df2)
plt.legend(df2.columns,loc="lower right")
plt.savefig('samplepic.png')
plt.show()

ser1 = Series(list('abcccaabd'))
print (ser1.unique())

print (ser1.value_counts())
