import random

abecedario_minuscula = "abcdefghijklmnñopqrstuvwxyz"

abecedario_mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

numbers = "1234567890"

simbolos = "!·@#$%&*()."

string = abecedario_minuscula + abecedario_mayuscula + numbers + simbolos

tamaño = 16

password = "".join(random.sample(string, tamaño))

print("Your new Password is ->", password)