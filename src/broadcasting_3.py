import numpy as np
a=np.arange(30)
a=a.reshape((2,5,3))
print(a)
b=np.arange(8)
b=b.reshape((2,4,1))
print(b)
c=a+b #qui dà errore perchè fare broadcasting in questo caso non è possibile
print(c)