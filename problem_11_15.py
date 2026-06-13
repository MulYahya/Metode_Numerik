"""
SOAL 11.15

Identifikasi Sistem
yang Tidak Konvergen
"""

import numpy as np

print("="*60)
print("SOAL 11.15")
print("="*60)

set1 = np.array([
    [8,3,1],
    [-6,0,7],
    [2,4,-1]
])

set2 = np.array([
    [1,1,5],
    [1,4,-1],
    [3,1,-1]
])

set3 = np.array([
    [2,3,5],
    [-2,4,-5],
    [0,2,-1]
])

def diagonal_dominan(A):

    for i in range(len(A)):
        diag = abs(A[i,i])
        lain = np.sum(np.abs(A[i])) - diag

        if diag <= lain:
            return False

    return True

print("Set 1 :", diagonal_dominan(set1))
print("Set 2 :", diagonal_dominan(set2))
print("Set 3 :", diagonal_dominan(set3))