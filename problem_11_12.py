"""
SOAL 11.12
Gauss-Seidel
Tanpa Relaxasi
dan λ = 0.95
"""

def gauss_seidel(relax=1.0):

    x1 = x2 = x3 = 0
    tol = 5
    ea = 100
    it = 0

    while ea > tol:

        o1,o2,o3 = x1,x2,x3

        gs1 = (3 + x2 + x3)/6
        x1 = relax*gs1 + (1-relax)*o1

        gs2 = (40 - 6*x1 - x3)/9
        x2 = relax*gs2 + (1-relax)*o2

        gs3 = (50 + 3*x1 - x2)/12
        x3 = relax*gs3 + (1-relax)*o3

        ea = max(
            abs((x1-o1)/(x1+1e-10))*100,
            abs((x2-o2)/(x2+1e-10))*100,
            abs((x3-o3)/(x3+1e-10))*100
        )

        it += 1

    return x1,x2,x3,it

print("="*60)
print("SOAL 11.12")
print("="*60)

a = gauss_seidel(1.0)
b = gauss_seidel(0.95)

print("\nTanpa Relaxasi")
print(a)

print("\nDengan λ = 0.95")
print(b)