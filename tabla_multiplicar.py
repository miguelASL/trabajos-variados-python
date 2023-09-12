import time
def obtener_numero():
    while True:
        try:
            numero = int(input("Ingresa un numero entero: "))
            return numero
        except ValueError:
            print("Valor invalido. Ingrese un numero entero valido por favor.")

def mostrar_tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero} es:")
    for i in range(1, 11):
        resultado = numero * i
        time.sleep(1)
        print(f"{numero} * {i} = {resultado} ")

def main():
    print("¡¡¡ Bienvenido a la tabla de multiplicar !!!")
    numero = obtener_numero()
    mostrar_tabla_multiplicar(numero)

if __name__=="__main__":
    main()