import qrcode

# Create qr code instance
texto = input("Diga el texto que quiera para generar el QR Code: ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)  

qr.add_data(texto)
qr.make(fit=True) # Ajusta el QR a la imagen

img = qr.make_image(fill='black', back_color='white') # Color del QR

img.save('qr.png')
