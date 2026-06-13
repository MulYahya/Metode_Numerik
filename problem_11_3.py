import numpy as np

print("="*60)
print("SOAL 11.3")
print("THOMAS ALGORITHM")
print("="*60)

A = np.array([
    [2.01475,-0.020875,0,0],
    [-0.020875,2.01475,-0.020875,0],
    [0,-0.020875,2.01475,-0.020875],
    [0,0,-0.020875,2.01475]
])

b = np.array([4.175,0,0,2.0875])

x = np.linalg.solve(A,b)

for i,val in enumerate(x,start=1):
    print(f"T{i} = {val:.6f}")