import random

def jugador():
    opciones = ['r', 'p', 't'] # r > s, s > p, p > r
    
    usuario = input("Introduce r para roca, p para papel, o t para tijeras: ").lower()
    ordenador = random.choice(opciones)
    
    if ganar(usuario, ordenador):
        return "¡Has ganado!"
    else:
        return "Has perdido :("

def ganar(jugador, oponente):
    if (jugador == 'r' and oponente == 's') or (jugador == 's' and oponente == 'p') or (jugador == 'p' and oponente == 'r'):
        return True
    else:
        return False

print(jugador())