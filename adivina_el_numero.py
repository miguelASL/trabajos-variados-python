import random

def adivina_el_numero(x):    
    print("=========================")
    print(" ¡ Bienvenido al juego ! ")
    print("=========================")
    print(" Tu meta es adivinar el número generado por el ordenador ")
    
    numero_aleatorio = random.randint(1, x) #número aleatoria entre 1 y x.
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        #El usuario ingresa un número.
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))
        
        if prediccion < numero_aleatorio:
            print("Intenta otra vez, este numero es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("Intentalo otra vez, este numero es muy grande")
    
    print(f"¡ Felicidades! adivinaste el numero {numero_aleatorio} correctamente. ")
    
    
adivina_el_numero(10) #Introduce un número que será hasta donde puede llegar (1, x).