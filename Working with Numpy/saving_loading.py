import numpy as np
a=np.arange(10)
print(a)

#save numpy array
np.save("saved",a)
#new file is craeted with name saved.npy

new_a=np.load("saved.npy")  #load the saved file
print(new_a)

#saving multiple arrays as zip or archive file
a1=np.arange(25)
a2=np.arange(30)
np.savez("saved_archive.npz",x=a1,y=a2) #savez is used for saving multiple arrays
load_npz=np.load("saved_archive.npz")
print(load_npz['x'])
print(load_npz['y'])

#save the arrays to textfile

np.savetxt('text.txt',a1,delimiter=',')
#loading of txt files

load_txt=np.loadtxt('text.txt',delimiter=',')
print("Text File=",load_txt)
#convets an integrer into a float number



