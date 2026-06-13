"""
SOAL 11.7
Cholesky untuk Matriks Diagonal
"""

import numpy as np

print("="*60)
print("SOAL 11.7")
print("="*60)

A = np.array([
    [900,0,0],
    [0,25,0],
    [0,0,4]
], dtype=float)

L = np.linalg.cholesky(A)

print("\nMatriks A:")
print(A)

print("\nMatriks L:")
print(L)

print("\nVerifikasi")
print(L @ L.T)