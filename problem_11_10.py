"""
SOAL 11.10
Metode Jacobi
Sistem Reaktor
"""

import numpy as np

print("="*60)
print("SOAL 11.10")
print("="*60)

tol = 5

c1=c2=c3=0
ea=100
it=0

while ea > tol:

    old1,old2,old3 = c1,c2,c3

    n1 = (3800 + 3*old2 + old3)/15
    n2 = (1200 + 3*old1 + 6*old3)/18
    n3 = (2350 + 4*old1 + old2)/12

    c1,c2,c3 = n1,n2,n3

    ea = max(
        abs((c1-old1)/(c1+1e-10))*100,
        abs((c2-old2)/(c2+1e-10))*100,
        abs((c3-old3)/(c3+1e-10))*100
    )

    it += 1

    print(f"\nIterasi {it}")
    print(f"c1={c1:.4f}")
    print(f"c2={c2:.4f}")
    print(f"c3={c3:.4f}")
    print(f"Error={ea:.4f}%")

print("\nHASIL AKHIR")
print(c1,c2,c3)