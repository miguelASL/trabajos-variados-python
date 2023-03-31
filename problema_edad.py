"""
A una fiesta asistieron persoanas de diferentes edades y sexos.
construir un algoritmo dadas las edades y generos de las personas.
Calcular:
- Cantidad de personas que asistieron a la fiesta.
- Cantidad de hobres y mujeres.
- Promedio de edades por generos.
- La edad de la persona mas joven que asistio.
Ingresa datos hasta una edad sea cero. 
"""


cp = 0 #cantidad de personas
ch = 0 #cantidad de hombres
cm = 0 #cantidad de mujeres
lista_h = [] #lista de edades de hombres
lista_m = [] #lista de edades de mujeres 
mas_joven = 150
edad = 1

while (edad > 0):
    edad = int(input("Ingresa tu edad: "))
    if edad > 0:
        cp += 1
        if edad < mas_joven:
            edad_joven = edad
        genero = ""
        while (genero not in ["h", "m"]):
            genero = input("Cual es tu genero? H/M: ")
            if genero in ["H", "h"]:
                ch += 1
                lista_h.append(edad)
            elif genero in ["M", "m"]:
                cm += 1
                lista_m.append(edad)
            else:
                print("Introduce bien el genero")
                
print("Cantidad de personas: ", cp)
print("Cantidad de hombre: ", ch)
print("Cantidad de mujeres: ", cm)
print("lista de edades de hombre: ", lista_h)
print("Lista de edades de mujeres: ", lista_m)   
print(f"La edad de la persona mas joven es {mas_joven} de edad")    
print("El promedio de edad en hombre es: ", sum(lista_h / len(lista_h)))
print("El promedio de edad en mujeres es: ", sum(lista_m / len(lista_m))) 