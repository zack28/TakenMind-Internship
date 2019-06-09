import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[0]) #prints the first row

#accessing each element
print(a[0][2])
#slices in an array
slice1=a[0:1,0:2]
print("Slice1=",slice)

slice2=a[:2,2:]
print("Slice2=",slice1)

b=[[0,0,0],[0,0,0],[0,0,0]]
a_len=a.shape[0]
print(a.shape)
print(a_len)

for i in range(a_len):
    for j in range(a_len):
        b[i][j]=j
    #b[i]=a[i]*a[i]

print(b)
#another way of accessing elements
#print(a[[0,2]])