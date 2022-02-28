import numpy as np
a=np.arange(6)
a=a.reshape((2,1,3))
print(a)
b=np.arange(8)
b=b.reshape((2,4,1))
print(b)
c=a+b 
print(c)