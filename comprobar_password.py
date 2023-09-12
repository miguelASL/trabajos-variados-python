#Condiciones para que la contraseña sea segura:
"""
-> Tiene mas de 8 caracteres
-> Tiene al menos una letro mayuscula
-> Tiene al menos un numero
"""
def comprobar_password(password):
    largo = False
    mayuscula = False
    numero = False
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayuscula = True
        if password[i].isnumeric():
            numero = True
    if largo and numero and mayuscula:
        return True
    else:
        return False

password = input("Ingrese una contraseña -> ")
verificacion = comprobar_password(password)
if verificacion:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")