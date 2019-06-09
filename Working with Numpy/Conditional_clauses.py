import numpy as np
x=np.array([100,200,300,400]) #each member as a
y=np.array([400,500,600,700]) #each member as b
condition=np.array([True,True,False,False]) #each member cond
#if true take x else y
z= [a if cond else b for a,cond, b in zip(x,condition,y)]
print(z)

#same opeartion usiing numpy
#np.where(#condition,#value for yes,#value for no)
z2=np.where(condition,x,y)

z3=np.where(x>200,0,1) #if x is > 200 replace it by 0 else 1
print(z3)

#sum
print(x.sum())

n=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("N=",n)
#colomun sum
print("Sum of Coloums=",n.sum(0))
#row sum
print("Sum of Rows=",n.sum(1))

#mean
mean=x.mean()
print("Mean=",mean)
#std deviation
std_dev=x.std()
print("Standard Deviation=",std_dev)

#varinace
var=x.var()
print("Variane=",var)

#logical operations

condition2=np.array([True,False,True])
print("OR operator",condition2.any())
print("AND operator",condition2.all())

#sorting in numpy arrays
unsorted=np.array([2,5,9,4,-6,3,1])
print("Unsorted Array=",unsorted)
unsorted.sort()
print("Sorted Array=",unsorted)

s=np.array(["Solid","Solid","Liquid","Liquid","Liquid","Gas","Gas"])
n=np.array([1,2,3,1,2,4,4,8,9,9,3,4,4])
print(np.unique(s))
print(np.unique(n))

print(np.in1d([2,6,9],n))
