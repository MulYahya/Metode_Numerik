"""
SOAL 11.20
Vandermonde Matrix 6x6
"""

import numpy as np

print("="*60)
print("SOAL 11.20")
print("="*60)

xdata = np.array([4,2,7,10,3,5])

V = np.vander(xdata,increasing=False)

b = np.sum(V,axis=1)

x = np.linalg.solve(V,b)

cond = np.linalg.cond(V)

print("\nCondition Number:")
print(cond)

print("\nMaximum Error:")
print(np.max(np.abs(x-1)))

print("\nSolusi:")
print(x)