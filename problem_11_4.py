"""
SOAL 11.4
Verifikasi Dekomposisi Cholesky

Konfirmasi bahwa:
A = L @ L.T

untuk matriks:

A = [[6,15,55],
     [15,55,225],
     [55,225,979]]
"""

import numpy as np

print("="*60)
print("SOAL 11.4 - VERIFIKASI CHOLESKY")
print("="*60)

A = np.array([
    [6,15,55],
    [15,55,225],
    [55,225,979]
], dtype=float)

L = np.linalg.cholesky(A)

print("\nMatriks L:")
print(L)

print("\nL.T:")
print(L.T)

hasil = L @ L.T

print("\nL @ L.T =")
print(hasil)

print("\nMatriks A Asli:")
print(A)

print("\nApakah sama?")
print(np.allclose(A, hasil))