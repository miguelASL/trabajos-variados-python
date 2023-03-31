texto = input("Introduzca el texto : ")
palabras = texto.split()

for palabra in palabras:
    vocales = 0
    consonantes = 0
    for letra in palabra:
        if letra.lower() in ["a", "e", "i", "o", "u"]:
            vocales += 1
        else:
            consonantes += 1
            
    print(f"{palabra} tiene {vocales} vocales y {consonantes} consonantes")