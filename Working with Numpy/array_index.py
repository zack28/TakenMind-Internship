import numpy as np
a=np.arange(0,12)
print(a)

print(a[0]) #prints the first element
print(a[0:5]) #prints the first 5 elements
a[0:5]=20 #assigns value 20 to the first 5 elements of the array
acopy=a.copy()
print(a[0:5])
print(a)
#interesting thing
a2=a[0:6]
print(a2)
a2[:]=29 #all the elements
print(a2)
print(a)
#no extra copy is created when using numpy

#creating new array copy


print(acopy)
acopy=a.copy()