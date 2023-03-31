"""
Determina si un numero X es perfecto, un numero es perfecto si la suma de sus DIVISORES es el mismo numero.
por ejemplo el 6 es perfecto ya que 1 + 2 + 3 = 6
"""

x = int(input("Introduce x: "))
sumador = 0

for i in range(1, x):
    if x % i == 0:
        sumador += i

if sumador == x :
    print("Es perfecto")
else:
    print("No es perfecto")
        