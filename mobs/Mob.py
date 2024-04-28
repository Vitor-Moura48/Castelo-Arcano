from Configurações import Global
from Configurações.config import efeito_morte

class Mob:
    def __init__(self, vida, dano):

        self.vida = vida
        self.dano = dano
        self.contador_ivulnerabilidade = 0
    
    def receber_dano(self, dano):
        self.vida -= dano
    
    def conferir_vida(self):
        if self.vida <= 0:
            return True
    
    def contar_vulnerabilidade(self):
        if self.contador_ivulnerabilidade > 0:
            self.contador_ivulnerabilidade -= 1

    def morrer(self):
        if Global.som_ligado:
            efeito_morte.play()
        self.kill()
        Global.inimigos_restantes -= 1
