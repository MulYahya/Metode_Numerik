"""
SOAL 11.18

Produksi Elektronik
"""

import numpy as np

print("="*60)
print("SOAL 11.18")
print("="*60)

A = np.array([
    [4,3,2],
    [1,3,1],
    [2,1,3]
],dtype=float)

b = np.array([
    960,
    510,
    610
],dtype=float)

x = np.linalg.solve(A,b)

print("\nProduksi Mingguan")

print(f"Transistor      = {x[0]:.0f}")
print(f"Resistor        = {x[1]:.0f}")
print(f"Computer Chip   = {x[2]:.0f}")

print("\nVerifikasi")

print(A @ x)