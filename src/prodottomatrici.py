import numpy as np

input=np.loadtxt("src/matrix.dat", dtype='i', delimiter=', ')
a=np.array([input])
print(a)
input=np.loadtxt("src/matrix1.dat", dtype='i', delimiter=', ')
b=np.array([input])
c=np.matmul(a,b)
print("Prodotto di matrici con la funzione matmul di numpy")
print(c)