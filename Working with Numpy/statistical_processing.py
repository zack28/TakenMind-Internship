import numpy as np
import matplotlib.pyplot as plt
a=np.arange(-100,100,10)
print(a)

dx, dy = np.meshgrid(a,a) #groups the point with every other point
#print("Dx",dx)
#print("Dy",dy)
function=2*dx+3*dy
function2=np.cos(dx)+np.cos(dy)
print("Function",function)
print("Function 2",function2)
plt.imshow(function)
plt.title('Function Plot of 2dx+3dy')
plt.colorbar()
plt.savefig('MyFig.png')

plt.imshow(function2)
plt.title('Function of Cos(dx)+Cos(dy)')
plt.colorbar()
plt.savefig('MyFig2.png')