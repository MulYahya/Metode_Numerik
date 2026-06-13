"""
SOAL 11.25
Program Umum Cholesky
"""

import numpy as np

def solve_cholesky(A,b):

    L=np.linalg.cholesky(A)

    y=np.linalg.solve(L,b)

    x=np.linalg.solve(L.T,y)

    return x,L

A=np.array([
    [6,15,55],
    [15,55,225],
    [55,225,979]
],dtype=float)

b=np.array([
    152.6,
    585.6,
    2488.8
])

x,L=solve_cholesky(A,b)

print("L:")
print(L)

print("\nSolusi:")
print(x)