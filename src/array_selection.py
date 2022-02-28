import numpy as np
a=np.array([4,5,7,2])
b=np.array([1,7,3,7])
c=np.array([2,3,4,2])
d=np.array([3,12,7,9])
mat=np.array([a,b,c,d])
print(mat)
sel1=mat[2,:]
print(sel1)
sel2=mat[:,1]
print(sel2)