"""
SOAL 11.17

Sistem Nonlinear
"""

import numpy as np
from scipy.optimize import fsolve

print("="*60)
print("SOAL 11.17")
print("="*60)

def fungsi(v):

    x,y = v

    f = 4 - y - 2*x**2
    g = 8 - y**2 - 4*x

    return [f,g]

tebakan = [
    (-2,-4),
    (1,2),
    (2,-1),
    (-1,3)
]

solusi = []

for g in tebakan:

    s = fsolve(fungsi,g)

    solusi.append(s)

print("\nSolusi yang ditemukan:")

for s in solusi:
    print(np.round(s,6))