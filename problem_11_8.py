"""
SOAL 11.8
Gauss-Seidel dengan Overrelaxation
λ = 1.2
εs = 5%
"""

import numpy as np

print("="*60)
print("SOAL 11.8")
print("="*60)

lam = 1.2
tol = 5

x1=x2=x3=0
ea=100
iterasi=0

while ea > tol:

    old1,old2,old3 = x1,x2,x3

    gs1 = (41 + 0.4*x2)/0.8
    x1 = lam*gs1 + (1-lam)*old1

    gs2 = (25 + 0.4*x1 + 0.4*x3)/0.8
    x2 = lam*gs2 + (1-lam)*old2

    gs3 = (105 + 0.4*x2)/0.8
    x3 = lam*gs3 + (1-lam)*old3

    ea = max(
        abs((x1-old1)/(x1+1e-10))*100,
        abs((x2-old2)/(x2+1e-10))*100,
        abs((x3-old3)/(x3+1e-10))*100
    )

    iterasi += 1

    print(f"\nIterasi {iterasi}")
    print(f"x1={x1:.4f}")
    print(f"x2={x2:.4f}")
    print(f"x3={x3:.4f}")
    print(f"Error={ea:.4f}%")

print("\nHASIL AKHIR")
print(x1,x2,x3)