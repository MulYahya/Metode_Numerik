"""
SOAL 11.27
PDE Kanal 1D
"""

import numpy as np
import matplotlib.pyplot as plt

A=np.array([
    [-1.2,0.75,0,0],
    [0.25,-1.2,0.75,0],
    [0,0.25,-1.2,0.75],
    [0,0,0.25,-1.2]
],dtype=float)

b=np.array([
    -20,
    0,
    0,
    -15
],dtype=float)

c_internal=np.linalg.solve(A,b)

x=np.array([0,2,4,6,8,10])

c=np.concatenate([
    [80],
    c_internal,
    [20]
])

print("Profil Konsentrasi:")
for xi,ci in zip(x,c):
    print(f"x={xi:2.0f} m --> c={ci:.4f}")

plt.figure(figsize=(8,5))
plt.plot(x,c,marker='o')
plt.xlabel("Jarak (m)")
plt.ylabel("Konsentrasi")
plt.title("Profil Konsentrasi Kanal")
plt.grid(True)
plt.show()