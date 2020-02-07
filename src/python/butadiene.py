import numpy as np
from numpy import linalg as LA
H = np.array([
[0, 1, 0, 0],
[1, 0, 1, 0],
[0, 1, 0, 1],
[0, 0, 1, 0]])
E, c = LA.eig(H)
print("Eigenvalues E: \n", E)
print("Eigenvector c: \n", c)
