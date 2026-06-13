"""
SOAL 11.9
Gauss-Seidel Sistem Reaktor
"""

import numpy as np

print("="*60)
print("SOAL 11.9")
print("="*60)

tol = 5

c1=c2=c3=0
ea=100
it=0

while ea > tol:

    o1,o2,o3 = c1,c2,c3

    c1 = (3800 + 3*c2 + c3)/15
    c2 = (1200 + 3*c1 + 6*c3)/18
    c3 = (2350 + 4*c1 + c2)/12

    ea = max(
        abs((c1-o1)/(c1+1e-10))*100,
        abs((c2-o2)/(c2+1e-10))*100,
        abs((c3-o3)/(c3+1e-10))*100
    )

    it += 1

    print(f"\nIterasi {it}")
    print(f"c1={c1:.4f}")
    print(f"c2={c2:.4f}")
    print(f"c3={c3:.4f}")
    print(f"Error={ea:.4f}%")

print("\nHASIL AKHIR")
print(c1,c2,c3)