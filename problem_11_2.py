import numpy as np

print("="*60)
print("SOAL 11.2")
print("INVERS MATRIKS DENGAN LU")
print("="*60)

A = np.array([
    [2,1,-1],
    [-3,-1,2],
    [-2,1,2]
],dtype=float)

A_inv = np.linalg.inv(A)

print("\nMatriks A")
print(A)

print("\nA^-1")
print(A_inv)

print("\nVerifikasi")
print(A@A_inv)