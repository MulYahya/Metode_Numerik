"""
SOAL 11.22
Matrix Form
Transpose
Inverse
"""

import numpy as np

print("="*60)
print("SOAL 11.22")
print("="*60)

A = np.array([
    [0,-7,5],
    [0,4,7],
    [-4,3,-7]
],dtype=float)

b = np.array([
    50,
    -30,
    40
],dtype=float)

x = np.linalg.solve(A,b)

print("\nSolusi:")
print(x)

print("\nTranspose:")
print(A.T)

print("\nInverse:")
print(np.linalg.inv(A))