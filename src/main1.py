print("Hello: here are some exercises with math.py")
a=3
b=5
import math
print("pi= ", math.pi)
print(math.sin(a+b))
import lib.lib1
print(lib.lib1.diff(a,b))
print("Serie per calcolare PI")
ad=0.0
for k in range(1,100):
 ad=ad+lib.lib1.frac(1,lib.lib1.quad(k))
print(math.sqrt(6*ad))
print(lib.lib1.diff(math.pi, math.sqrt(6*ad)))
print("Esercizi su stringhe")