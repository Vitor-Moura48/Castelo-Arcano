from Configurações.config import *
from Configurações import Global
from mobs import Player, Castelo

class VerificarColisoes:  # classe para verificar colisões
    def __init__(self):
        pass

    # função para verificar colisão do jogador com algo
    def colisao_com_player(self):

        # verifica colisões com inimigos e responde de acordo
        for inimigo in Global.grupo_todos_inimigos:
            if pygame.sprite.collide_rect(Player.player, inimigo) and inimigo.contador_ivulnerabilidade <= 0:        
                inimigo.contador_ivulnerabilidade = 10
                inimigo.receber_dano(Player.player.dano)
        
        for projetil_inimigo in Global.grupo_projeteis_inimigos:
            if pygame.sprite.collide_rect(Player.player, projetil_inimigo):
                projetil_inimigo.perfuracoes_restantes -= 1
                Player.player.vida_restante -= projetil_inimigo.dano

        for buff in Global.grupo_todos_efeitos:
            if pygame.sprite.collide_rect(Player.player, buff):
                buff.buff()
                buff.kill()
            
    # função para verificar colisões do castelo com algo
    def colisao_com_castelo(self):

        # verifica colisões com inimigos e responde de acordo
        for inimigo in Global.grupo_todos_inimigos:
            if pygame.sprite.collide_rect(Castelo.castelo, inimigo):

                if  Global.barreira == 0:
                    Global.vidas_castelo -= inimigo.dano
                    if Global.som_ligado:
                        efeito_explosao.play()
                else:

                    if  Global.barreira >= inimigo.dano:
                        Global.barreira -= inimigo.dano
                       
                    else:
                        Castelo.castelo.vida_restante -= (inimigo.dano - Global.barreira)
                        Global.barreira = 0
                    if Global.som_ligado:
                        efeito_defesa.play()

                inimigo.kill()
                Global.inimigos_restantes -= 1

        
        for inimigo in Global.grupo_projeteis_inimigos:
            if pygame.sprite.collide_rect(Castelo.castelo, inimigo):

                if  Global.barreira == 0:
                    Global.vidas_castelo -= inimigo.dano
                    if Global.som_ligado:
                        efeito_explosao.play()
                else:
                    if  Global.barreira >= inimigo.dano:
                        Global.barreira -= inimigo.dano
                    else:
                        Global.vidas_castelo -= (inimigo.dano - Global.barreira)
                        Global.barreira = 0

                inimigo.perfuracoes_restantes -= 1
        
    # função para verificar colisões do projetil do jogador com algo
    def colisao_com_projetil_player(self):

        for projetil_aliado in Global.grupo_projeteis_aliados:

            for inimigo in Global.grupo_todos_inimigos:
                if pygame.sprite.collide_rect(projetil_aliado, inimigo) and inimigo.contador_ivulnerabilidade <= 0:

                    inimigo.receber_dano(Player.player.dano)

                    inimigo.contador_ivulnerabilidade = 10
                    projetil_aliado.perfuracoes_restantes -= 1
                
    def saiu_do_mapa(self):
        objetos_para_apagar = []
        for inimigo in Global.grupo_inimigos1:
            if inimigo.rect.right < 0:
                objetos_para_apagar.append(inimigo)
        for inimigo in Global.grupo_inimigos2:
            if inimigo.rect.right < 0:
                objetos_para_apagar.append(inimigo)
        for efeito in Global.grupo_todos_efeitos:
            if efeito.rect.right < 0:
                objetos_para_apagar.append(efeito)
    

        for objeto in objetos_para_apagar:
            if objeto in Global.grupo_todos_inimigos:

                if Global.barreira == 0:
                    Global.inimigos_restantes -= 1
                    if Global.som_ligado:
                        efeito_morte.play()

                else:
                    Global.barreira -= 1
                    Global.inimigos_restantes -= 1
                    if Global.som_ligado:
                        efeito_defesa.play()

            objeto.kill()


colisoes = VerificarColisoes()