import numpy as np
a=np.arange(5)
b=np.ones_like(a)
b[:]=a[:]
print(b)
print(a)
b[3]=235
print("con slot diversi di memoria")
print(b)
print(a)
c=a
c[2]=1000
print(" con stesso slot di memoria allocato:" )
print(c)
print(a)