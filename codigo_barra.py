from barcode import EAN13
from barcode.writer import ImageWriter

#Este código genera un código de barras a partir de un número introducido por el usuario.
#Y lo guarda en la carpeta donde se encuentra el archivo .py

number : str = input("Introduce un número de código de barras: ")
my_code = EAN13(number, writer=ImageWriter())
my_code.save("codigo_barra")

