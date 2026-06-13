"""
SOAL 11.5
Cholesky Decomposition dan Penyelesaian Sistem
"""

import numpy as np

print("="*60)
print("SOAL 11.5")
print("="*60)

A = np.array([
    [6,15,55],
    [15,55,225],
    [55,225,979]
], dtype=float)

b = np.array([
    152.6,
    585.6,
    2488.8
], dtype=float)

L = np.linalg.cholesky(A)

print("\nMatriks L:")
print(L)

# Forward substitution
y = np.linalg.solve(L,b)

print("\nVektor y:")
print(y)

# Back substitution
x = np.linalg.solve(L.T,y)

print("\nHASIL")

print(f"a0 = {x[0]:.6f}")
print(f"a1 = {x[1]:.6f}")
print(f"a2 = {x[2]:.6f}")

print("\nVerifikasi Ax")
print(A @ x)