import numpy as np
list1= [1,2,3,4]
list2=[5,6,7,8]
myArray=np.array([list1,list2])
print("List 1=",list1)
print("List 2=",list2)
print(myArray)

print(myArray.shape)
print(myArray.dtype)

# zeros,ones,empty, eye,arrange
new_array=np.zeros(5)
new_array1=np.ones([3,3])
new_array2=np.empty(5)
new_array3=np.eye(3)
new_array4=np.arange(0,20,2)
print(new_array)
print(new_array1)
#print(new_array2)
print(new_array3)
print(new_array4)