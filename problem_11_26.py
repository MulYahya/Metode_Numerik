"""
SOAL 11.26
Program Umum Gauss-Seidel
"""

import numpy as np

def gauss_seidel(A,b,tol=1e-5,maxiter=100):

    n=len(b)

    x=np.zeros(n)

    for k in range(maxiter):

        old=x.copy()

        for i in range(n):

            s1=np.dot(A[i,:i],x[:i])

            s2=np.dot(A[i,i+1:],old[i+1:])

            x[i]=(b[i]-s1-s2)/A[i,i]

        err=np.linalg.norm(x-old,np.inf)

        if err<tol:
            return x,k+1

    return x,maxiter

A=np.array([
    [10,2,-1],
    [-3,-6,2],
    [1,1,5]
],dtype=float)

b=np.array([
    27,
    -61.5,
    -21.5
])

x,it=gauss_seidel(A,b)

print("Iterasi:",it)
print("Solusi:",x)