user_ = "admin" #Elegir el nombre del usuario
pwd_ = "123" #Elegir la contraseña del usuario
print("Bienvenido ingrese sus datos por favor")
print("Usuario: ")
user = input()
print("Contraseña: ")
pwd = input()
if user == user_ and pwd == pwd_:
    print("¡Bienvenido al programa!")
else:
    print("¡Usuario o contraseña invalido!")