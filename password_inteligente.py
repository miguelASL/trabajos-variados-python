import secrets
import string

# Esta función genera una contraseña aleatoria de 20 caracteres
def password_inteligente():
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alfabeto) for i in range(20))
    return password

print(password_inteligente())