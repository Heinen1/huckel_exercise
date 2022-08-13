import time 
import numpy as np
from numpy import linalg as LA

hamiltonian = np.array([
[0,             np.sqrt(2)],
[np.sqrt(2),    0]])

time_begin = time.perf_counter()
E, c = LA.eig(hamiltonian)
time_end= time.perf_counter()

print("Eigenvalues E: \n", E)
print("Eigenvector c: \n", c)
print("Elapsed time: ",time_end-time_begin)

