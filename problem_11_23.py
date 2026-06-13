"""
SOAL 11.23
Operasi Thomas vs Gauss
"""

import numpy as np
import matplotlib.pyplot as plt

print("="*60)
print("SOAL 11.23")
print("="*60)

n = np.arange(2,21)

thomas = 5*n - 4

gauss = n**3/3 + n**2

plt.figure(figsize=(8,5))
plt.plot(n,thomas,marker='o',label="Thomas")
plt.plot(n,gauss,marker='s',label="Gauss")

plt.xlabel("n")
plt.ylabel("Jumlah Operasi")
plt.title("Thomas vs Gauss")
plt.grid(True)
plt.legend()

plt.show()