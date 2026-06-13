"""
SOAL 11.28
Sistem Pentadiagonal
"""

import numpy as np

A=np.array([
    [8,-2,-2,0,0],
    [-2,9,-4,-1,0],
    [-1,-3,7,-1,-2],
    [0,-4,-2,12,-5],
    [0,0,-7,-3,15]
],dtype=float)

b=np.array([
    5,
    2,
    0,
    1,
    5
],dtype=float)

x=np.linalg.solve(A,b)

print("="*60)
print("SOAL 11.28")
print("="*60)

for i,val in enumerate(x,start=1):
    print(f"x{i} = {val:.6f}")

print("\nVerifikasi:")
print(A@x)