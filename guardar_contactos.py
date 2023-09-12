def guardar_contactos():
    contactos = {}

    while True:
        nombre = input("Ingresa el nombre del contacto (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break

        telefono = input("Ingresa el numero de telefono -> ")
        contactos[nombre] =  telefono
    return contactos

def mostrar_contactos(contactos):
    print("Listar contactos")
    for nombre, telefono in contactos.items():
        print(f"{nombre} -> {telefono}")

def main():
    print("¡¡¡ Bienvenido a la agenda de contactos !!!")
    agenda = guardar_contactos()
    mostrar_contactos(agenda)

if __name__ == "__main__":
    main()