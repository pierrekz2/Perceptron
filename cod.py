
import numpy as np 


numEpocas = 10000 #70000
numAmostras = 6

peso = np.array([113, 122, 107, 98, 115, 120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])

normaliza = False
if normaliza:
    peso = peso/np.linalg.norm(peso)
    pH = pH/np.linalg.norm(peso)



bias = 1

X = np.vstack((peso, pH))   # Ou X = np.asarray([peso, pH])
Y = np.array([-1, 1, -1, -1, 1, 1])


eta = 0.1

e = np.zeros(6)

W = np.ones([1,3])

for j in range(numEpocas):
    for k in range(numAmostras):
     Xb = np.hstack((bias, X[:,k]))
     
     V = np.dot(W, Xb)
     
     Yr = np.sign(V)
     
     e[k] = Y[k] - Yr
     
     W = W + eta*e[k]*Xb
     
print("Vetor de errors (e) = " + str(e))