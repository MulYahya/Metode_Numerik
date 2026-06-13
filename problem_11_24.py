"""
SOAL 11.24
Program Umum Thomas Algorithm
"""

import numpy as np

def thomas(a,b,c,d):

    n=len(d)

    c_=np.zeros(n-1)
    d_=np.zeros(n)

    c_[0]=c[0]/b[0]
    d_[0]=d[0]/b[0]

    for i in range(1,n-1):

        den=b[i]-a[i-1]*c_[i-1]

        c_[i]=c[i]/den

        d_[i]=(d[i]-a[i-1]*d_[i-1])/den

    d_[n-1]=(d[n-1]-a[n-2]*d_[n-2]) / (
        b[n-1]-a[n-2]*c_[n-2]
    )

    x=np.zeros(n)

    x[-1]=d_[-1]

    for i in range(n-2,-1,-1):
        x[i]=d_[i]-c_[i]*x[i+1]

    return x

a=np.array([-1,-1,-1],dtype=float)
b=np.array([4,4,4,4],dtype=float)
c=np.array([-1,-1,-1],dtype=float)
d=np.array([5,5,10,23],dtype=float)

x=thomas(a,b,c,d)

print("Solusi:")
print(x)