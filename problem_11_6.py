"""
SOAL 11.6
Cholesky Decomposition Manual
"""

import numpy as np

print("="*60)
print("SOAL 11.6")
print("="*60)

A = np.array([
    [8,20,15],
    [20,80,50],
    [15,50,60]
], dtype=float)

b = np.array([
    50,
    250,
    100
], dtype=float)

L = np.linalg.cholesky(A)

print("\nMatriks L:")
print(L)

y = np.linalg.solve(L,b)
x = np.linalg.solve(L.T,y)

print("\nSolusi Sistem")

print(f"x1 = {x[0]:.6f}")
print(f"x2 = {x[1]:.6f}")
print(f"x3 = {x[2]:.6f}")

print("\nVerifikasi")
print(A @ x)