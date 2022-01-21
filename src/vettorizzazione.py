import numpy as np
a=np.arange(0,4*np.pi,0.1)
y=np.zeros(len(a))
for i in range (len(a)):
 y[i]=np.sin(a[i])*2
 print(y[i])