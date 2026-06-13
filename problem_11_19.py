"""
SOAL 11.19
Hilbert Matrix 10x10
Condition Number Spektral
"""

import numpy as np

print("="*60)
print("SOAL 11.19")
print("="*60)

n = 10

H = np.array([
    [1/(i+j+1) for j in range(n)]
    for i in range(n)
],dtype=float)

b = np.sum(H,axis=1)

x = np.linalg.solve(H,b)

cond = np.linalg.cond(H)

digits_lost = np.log10(cond)

print("\nCondition Number:")
print(cond)

print("\nPerkiraan Digit Hilang:")
print(digits_lost)

print("\nMaks Error:")
print(np.max(np.abs(x-1)))

print("\nSolusi:")
print(x)