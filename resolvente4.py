import math

def disc_cubica(b0,b1,b2):
    print()
    Dg = -4*(b2**3)*b0 + (b1*b2)**2 - 18*b0*b1*b2 - 4*(b1**3) - 27*(b0**2)
    print(f"g= x^3 + {b2}x^2 + {b1}x + {b0}")
    print()
    return Dg

print("grado: ")
grado = int(input())

if grado == 4:
    print("a3=")
    a3 = int(input())

    print("a2=")
    a2 = int(input())

    print("a1=")
    a1 = int(input())

    print("a0=")
    a0 = int(input())

    b2 = -a2
    b1 = a1*a3 - 4*a0
    b0 = -(a3**2)*a0 - a1**2 + 4*a0*a2

    Dg = disc_cubica(b0,b1,b2)

else:
    print("a2=")
    a2 = int(input())

    print("a1=")
    a1 = int(input())

    print("a0=")
    a0 = int(input())

    Dg = disc_cubica(a0,a1,a2)



print(f"Discriminante: {Dg}")

resultado = math.sqrt(abs(Dg))

if math.trunc(resultado) == resultado:
    print(f"Es un cuadrado: {resultado}")
    print()
else:
    print("No es un cuadrado")
    print()

#print(type(resultado))

