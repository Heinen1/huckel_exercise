import time 
import numpy as np
from numpy import linalg as LA
H = np.array([
[0, 1, 0],
[1, 0, 1],
[0, 1, 0]])
time_begin = time.perf_counter()
E, c = LA.eig(H)
time_end= time.perf_counter()
print("Eigenvalues E: \n", E)
print("Eigenvector c: \n", c)
print("Elapsed time: ",time_end-time_begin)

