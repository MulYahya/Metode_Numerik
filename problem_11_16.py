"""
SOAL 11.16

Solusi
Inverse
Condition Number
"""

import numpy as np

print("="*60)
print("SOAL 11.16")
print("="*60)

A = np.array([
    [14,9,4],
    [9,16,9],
    [4,9,16]
],dtype=float)

b = np.array([27,34,29],dtype=float)

x = np.linalg.solve(A,b)

Ainv = np.linalg.inv(A)

cond = np.linalg.cond(A,np.inf)

print("\nSolusi")
print(x)

print("\nInverse")
print(Ainv)

print("\nCondition Number")
print(cond)