import sys
infile='matrix.dat'
outfile='outdata.dat'
outdata=open(outfile,'w')
for i in range(1,10):
  outdata.write(str(i))

print("Lavoriamo con delle matrici")
l = []
with open('src/matrix.dat', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) > 0 :
     l.append(list(map(int, line.split(', '))))
     print(l)
import numpy as np
input=np.loadtxt("src/matrix.dat", dtype='i', delimiter=', ')
print("con NumPy otteniamo:")
print(input)