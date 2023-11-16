from Configurações.config import *
from Configurações import Variaveis_globais
from mobs import Player, Castelo

class VerificarColisoes:  # classe para verificar colisões
    def __init__(self):
        pass

    # função para verificar colisão do jogador com algo
    def colisao_com_player(self):

        # verifica colisões com inimigos e responde de acordo
        for inimigo in Variaveis_globais.grupo_todos_inimigos:
            if pygame.sprite.collide_rect(Player.player, inimigo) and inimigo.contador_ivulnerabilidade <= 0:        
                inimigo.contador_ivulnerabilidade = 10
                inimigo.vida_restante -= Player.player.dano
        
        for projetil_inimigo in Variaveis_globais.grupo_projeteis_inimigos:
            if pygame.sprite.collide_rect(Player.player, projetil_inimigo):
                projetil_inimigo.perfuracoes_restantes -= 1
                Player.player.vida_restante -= projetil_inimigo.dano

        for buff in Variaveis_globais.grupo_todos_efeitos:
            if pygame.sprite.collide_rect(Player.player, buff):
                buff.buff()
                buff.kill()
            
    # função para verificar colisões do castelo com algo
    def colisao_com_castelo(self):

        # verifica colisões com inimigos e responde de acordo
        for inimigo in Variaveis_globais.grupo_todos_inimigos:
            if pygame.sprite.collide_rect(Castelo.castelo, inimigo):

                if  Variaveis_globais.barreira == 0:
                    Variaveis_globais.vidas_castelo -= inimigo.dano
                    if Variaveis_globais.som_ligado:
                        efeito_explosao.play()
                else:

                    if  Variaveis_globais.barreira >= inimigo.dano:
                        Variaveis_globais.barreira -= inimigo.dano
                       
                    else:
                        Castelo.castelo.vida_restante -= (inimigo.dano - Variaveis_globais.barreira)
                        Variaveis_globais.barreira = 0
                    if Variaveis_globais.som_ligado:
                        efeito_defesa.play()

                inimigo.kill()
                Variaveis_globais.inimigos_restantes -= 1

        
        for inimigo in Variaveis_globais.grupo_projeteis_inimigos:
            if pygame.sprite.collide_rect(Castelo.castelo, inimigo):

                if  Variaveis_globais.barreira == 0:
                    Variaveis_globais.vidas_castelo -= inimigo.dano
                    if Variaveis_globais.som_ligado:
                        efeito_explosao.play()
                else:
                    if  Variaveis_globais.barreira >= inimigo.dano:
                        Variaveis_globais.barreira -= inimigo.dano
                    else:
                        Variaveis_globais.vidas_castelo -= (inimigo.dano - Variaveis_globais.barreira)
                        Variaveis_globais.barreira = 0

                inimigo.perfuracoes_restantes -= 1
        
    # função para verificar colisões do projetil do jogador com algo
    def colisao_com_projetil_player(self):

        for projetil_aliado in Variaveis_globais.grupo_projeteis_aliados:

            for inimigo in Variaveis_globais.grupo_todos_inimigos:
                if pygame.sprite.collide_rect(projetil_aliado, inimigo) and inimigo.contador_ivulnerabilidade <= 0:
                    inimigo.vida_restante -= projetil_aliado.dano
                    inimigo.contador_ivulnerabilidade = 10
                    projetil_aliado.perfuracoes_restantes -= 1
                
    def saiu_do_mapa(self):
        objetos_para_apagar = []
        for inimigo in Variaveis_globais.grupo_inimigos1:
            if inimigo.rect.right < 0:
                objetos_para_apagar.append(inimigo)
        for inimigo in Variaveis_globais.grupo_inimigos2:
            if inimigo.rect.right < 0:
                objetos_para_apagar.append(inimigo)
        for efeito in Variaveis_globais.grupo_todos_efeitos:
            if efeito.rect.right < 0:
                objetos_para_apagar.append(efeito)
    

        for objeto in objetos_para_apagar:
            if objeto in Variaveis_globais.grupo_todos_inimigos:

                if Variaveis_globais.barreira == 0:
                    Variaveis_globais.inimigos_restantes -= 1
                    if Variaveis_globais.som_ligado:
                        efeito_morte.play()

                else:
                    Variaveis_globais.barreira -= 1
                    Variaveis_globais.inimigos_restantes -= 1
                    if Variaveis_globais.som_ligado:
                        efeito_defesa.play()

            objeto.kill()


colisoes = VerificarColisoes()