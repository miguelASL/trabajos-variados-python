import random

def adivina_el_numero_ordenador(x):
    print("======================")
    print(" Bienvenidoa al juego ")
    print("======================")
    print(f"Selecciona un número entre 1 y {x} para que el ordenador intente adivinarlo.")
    
    limite_inferior= 1
    limite_superior= x
    
    respuesta=""
    while respuesta != "c":
        #Generar una predicción.
        if limite_inferior != limite_superior:
            prediccion= random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #Tambien podría ser el limite_superior.
            
        #Obtener respuesta del usuario.
        respuesta= input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()
        
        if respuesta =="a":
            limite_superior= prediccion - 1
        elif respuesta =="b":
            limite_inferior= prediccion + 1
    
    print(f"! Siiiii ¡ El ordenador adivino tu número correctamente: {prediccion}")
    
    
adivina_el_numero_ordenador(10) #elije el numero final del rango.