"""
SOAL 11.13
Gauss-Seidel
λ = 1.2
"""

def solve(relax=1.0):

    x1=x2=x3=0
    ea=100
    tol=5
    it=0

    while ea > tol:

        o1,o2,o3=x1,x2,x3

        gs1=(20 + x2 - 2*x3)/8
        x1=relax*gs1+(1-relax)*o1

        gs2=(38 + 2*x1 - x3)/6
        x2=relax*gs2+(1-relax)*o2

        gs3=(-34 + 3*x1 + x2)/7
        x3=relax*gs3+(1-relax)*o3

        ea=max(
            abs((x1-o1)/(x1+1e-10))*100,
            abs((x2-o2)/(x2+1e-10))*100,
            abs((x3-o3)/(x3+1e-10))*100
        )

        it+=1

    return x1,x2,x3,it

print("="*60)
print("SOAL 11.13")
print("="*60)

print("\nTanpa Relaxasi")
print(solve(1.0))

print("\nDengan λ=1.2")
print(solve(1.2))