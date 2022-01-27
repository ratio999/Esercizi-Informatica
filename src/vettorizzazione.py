import numpy as np
import time
a=np.arange(0,4*np.pi,0.1)
y=np.zeros(len(a))
t1=time.perf_counter()
for i in range (len(a)):
 y[i]=np.sin(a[i])*2
t2=time.perf_counter()
print("Senza vettorizzazione ho: ", t2-t1) 
t3=time.perf_counter()
z=np.sin(a)*2
t4=time.perf_counter()
print("Con la vettorizzazione ho: ", t4-t3)
if ((t4-t3)>(t2-t1)):
  print("Meglio il ciclo for!")
else:
  print("Meglio la vettorizzazione!")