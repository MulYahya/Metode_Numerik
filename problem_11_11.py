"""
SOAL 11.11
Gauss-Seidel
es = 5%
"""

print("="*60)
print("SOAL 11.11 - GAUSS SEIDEL")
print("="*60)

tol = 5

x1 = x2 = x3 = 0
ea = 100
iterasi = 0

while ea > tol:

    old1, old2, old3 = x1, x2, x3

    x1 = (27 - 2*x2 + x3)/10
    x2 = (61.5 - 3*x1 + 2*x3)/6
    x3 = (-21.5 - x1 - x2)/5

    ea = max(
        abs((x1-old1)/(x1+1e-10))*100,
        abs((x2-old2)/(x2+1e-10))*100,
        abs((x3-old3)/(x3+1e-10))*100
    )

    iterasi += 1

    print(f"\nIterasi {iterasi}")
    print(f"x1 = {x1:.6f}")
    print(f"x2 = {x2:.6f}")
    print(f"x3 = {x3:.6f}")
    print(f"Error = {ea:.4f}%")

print("\nHASIL AKHIR")
print(f"x1 = {x1:.6f}")
print(f"x2 = {x2:.6f}")
print(f"x3 = {x3:.6f}")