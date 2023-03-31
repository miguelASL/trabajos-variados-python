import time
class Luchador:
    
    def __init__(self, nombre, chakra, sharingan, ataque, defensa, vida):
        self.nombre= nombre
        self.chakra= chakra
        self.sharingan= sharingan
        self.ataque= ataque
        self.defensa= defensa
        self.vida= vida
        print("El luchador", nombre, "esta listo para luchar !!!")
        
    def atacar(self, enemigo):
        diferencia_de_ataque = self.ataque - enemigo.defensa
        enemigo.vida = enemigo.vida - diferencia_de_ataque
        print(
            f"{self.nombre} ataco a {enemigo.nombre} con {diferencia_de_ataque} de ataque"
        )
        print(
            f"La vida de {enemigo.nombre} es : {enemigo.vida}"
        )
        
class Batalla:
    
    turno = "1"
    
    def __init__(self, luchador1, luchador2):
        self.luchador1 = luchador1
        self.luchador2 = luchador2
        
    def comienza_batalla(self):
        while self.luchador1.vida > 0 and self.luchador2.vida > 0:
            time.sleep(1)
            if self.turno == "1":
                self.luchador1.atacar(self.luchador2)
                self.turno = "2"
            else:
                self.luchador2.atacar(self.luchador1)
                self.turno = "1"
        if self.luchador1.vida <= 0:
            print(" El ganador es: ", self.luchador2.nombre)
        else:
            print("El ganador es el todopoderoso: ", self.luchador1.nombre)                
                
itachi = Luchador("Itachi", 7000, True, 1000, 500, 1000)
luffi = Luchador("Luffi", 7500, False, 700, 700, 1500)

itachi.atacar(luffi)
#luffi.atacar(itachi)      
        
Batalla(itachi, luffi).comienza_batalla()