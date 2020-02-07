import time 
import numpy as np
from numpy import linalg as LA

H_a1 = np.array([
[0, np.sqrt(2), np.sqrt(2)],
[np.sqrt(2), 0, 0],
[np.sqrt(2), np.sqrt(2), 1],
])
H_a2 = 0
H_b1 = np.array([
[0, np.sqrt(2)],
[np.sqrt(2), 0]
])
H_b2 = np.array([
[0, np.sqrt(2)],
[np.sqrt(2), -1]
])

time_begin = time.clock()
E_a1, c_a1 = LA.eig(H_a1)
#E_a2, c_a2 = LA.eig(H_a2)
E_b1, c_b1 = LA.eig(H_b1)
E_b2, c_b2 = LA.eig(H_b2)
time_end= time.clock()
print("Eigenvalues E_a1: \n", E_a1)
print("Eigenvector c_a1: \n", c_a1)
print("Elapsed time: ",time_end-time_begin)

