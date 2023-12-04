import phonenumbers
from phonenumbers import geocoder

number = input("Introduce un número de teléfono con el prefijo internacional: ")
if number[0] != "+":
    number = "+" + number
    
    phone = phonenumbers.parse(number)
    print(geocoder.description_for_number(phone, "es"))