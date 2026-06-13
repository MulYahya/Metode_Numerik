import numpy as np

print("="*60)
print("SOAL 11.1")
print("SISTEM TRIDIAGONAL")
print("="*60)

A = np.array([
    [0.8, -0.4, 0],
    [-0.4, 0.8, -0.4],
    [0, -0.4, 0.8]
], dtype=float)

b = np.array([41,25,105], dtype=float)

print("\nMatriks A:")
print(A)

print("\nVektor b:")
print(b)

x = np.linalg.solve(A,b)

print("\nHASIL")
print(f"x1 = {x[0]:.4f}")
print(f"x2 = {x[1]:.4f}")
print(f"x3 = {x[2]:.4f}")

print("\nVerifikasi A.x")
print(A@x)