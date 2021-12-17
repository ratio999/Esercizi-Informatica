print("Esercizi list")
l=[]
import math
k=["Giuseppe","Troian"]
print(k[1])
m=[0,1,2,3,4]
print(m[0:3])
print(m[-4])
m[0:3]
print(m)
a=range(8)
b=[int((x*3)+math.pi) for x in a]
c=[x*3 for x in a]
print(b[0:6])
print(c[0:6])
import time
print("Quanto impiega ad estendere una lista?")
l=list(range(1000000))
f=list(range(2000000))
print(type(f))
t1=time.perf_counter()
kk=l+f
t2=time.perf_counter()
print(t2-t1)
t3=time.perf_counter()
l.extend(f)
t4=time.perf_counter()
print(t4-t3)
print("Esercizietto LIFOFIFO")
stack=list(range(1,5))
print("initial stack: ", stack)
j=list(range(5,7))
stack.extend(j)
print("new stack: ", stack)
stack.pop(0)
print("popd0: ", stack)
stack.pop()
print("popd: ", stack)
print("prove con tuple")
karma=()
print("karma: ", type(karma), karma)

print("Dizionari")
dict1={1:"bardo", "cane":16, 2:4, 3:9}
print(dict1["cane"])
print(dict1.pop(1), "and then: ", dict1)
