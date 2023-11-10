from Configurações.config import *
from Configurações import Variaveis_globais
from mobs import Player, Castelo
from Efeitos import buff_01, buff_02, buff_03, animacoes


class VerificarColisoes:  # classe para verificar colisões
    def __init__(self):
        pass

    # função para verificar colisão do jogador com algo
    def colisao_com_player(self):
        mobs_ativos = [len(Variaveis_globais.grupo_inimigos1), len(Variaveis_globais.grupo_inimigos2)]
        
        colisoes_player_inimigo1 = pygame.sprite.spritecollide(Player.player, Variaveis_globais.grupo_inimigos1, True)
        colisoes_player_inimigo2 = pygame.sprite.spritecollide(Player.player, Variaveis_globais.grupo_inimigos2, True)
        colisoes_player_buff1 = pygame.sprite.spritecollide(Player.player, Variaveis_globais.grupo_efeito1, True)
        colisoes_player_buff2 = pygame.sprite.spritecollide(Player.player, Variaveis_globais.grupo_efeito2, True)
        colisoes_player_buff3 = pygame.sprite.spritecollide(Player.player, Variaveis_globais.grupo_efeito3, True)

        # verifica colisões com inimigos e responde de acordo
        if colisoes_player_inimigo1:
            Variaveis_globais.inimigos_restantes -= mobs_ativos[0] - len(Variaveis_globais.grupo_inimigos1)
            efeito_morte.play()

        if colisoes_player_inimigo2:
            Variaveis_globais.inimigos_restantes -= mobs_ativos[1] - len(Variaveis_globais.grupo_inimigos2)
            efeito_morte.play()

        # verifica colisões com buffs e responde de acordo
        if colisoes_player_buff1:
            buff_01.efeito_buff1.buff()

        if colisoes_player_buff2:
            buff_02.efeito_buff2.buff() 

            efeito_animacao = animacoes.EfeitosAnimacao()
            Variaveis_globais.todas_as_sprites.add(efeito_animacao)
            efeito_animacao.animar1()
        
        if colisoes_player_buff3:
            buff_03.efeito_buff3.buff()
            

    # função para verificar colisões do castelo com algo
    def colisao_com_castelo(self):
        mobs_ativos = [len(Variaveis_globais.grupo_inimigos1), len(Variaveis_globais.grupo_inimigos2)]

        # verifica colisões com inimigos e responde de acordo
        colisoes_castelo_inimigo1 = pygame.sprite.spritecollide(Castelo.castelo, Variaveis_globais.grupo_inimigos1, True)
        colisoes_castelo_inimigo2 = pygame.sprite.spritecollide(Castelo.castelo, Variaveis_globais.grupo_inimigos2, True)

        if colisoes_castelo_inimigo1:
            if  Variaveis_globais.barreira == 0:
                Variaveis_globais.vidas_castelo -= mobs_ativos[0] - len(Variaveis_globais.grupo_inimigos1)
                efeito_explosao.play()
            else:
                Variaveis_globais.barreira -= 1
                efeito_defesa.play()

            Variaveis_globais.inimigos_restantes -= mobs_ativos[0] - len(Variaveis_globais.grupo_inimigos1)

        if colisoes_castelo_inimigo2:
            if  Variaveis_globais.barreira == 0:
                Variaveis_globais.vidas_castelo -= mobs_ativos[0] - len(Variaveis_globais.grupo_inimigos1)
                efeito_explosao.play()
            else:
                Variaveis_globais.barreira -= 1
                efeito_defesa.play()

            Variaveis_globais.inimigos_restantes -= mobs_ativos[0] - len(Variaveis_globais.grupo_inimigos1)

    # função para verificar colisões do projetil do jogador com algo
    def colisao_com_projetil_player(self):
        mobs_ativos = [len(Variaveis_globais.grupo_inimigos1), len(Variaveis_globais.grupo_inimigos2)]

        for projetil_aliado in Variaveis_globais.grupo_projeteis_aliados:
            colisoes_projetil_inimigo1 = pygame.sprite.spritecollide(projetil_aliado, Variaveis_globais.grupo_inimigos1, True)
            colisoes_projetil_inimigo2 = pygame.sprite.spritecollide(projetil_aliado, Variaveis_globais.grupo_inimigos2, True)

            # verifica colisões com inimigos e responde de acordo
            if colisoes_projetil_inimigo1:
                Variaveis_globais.inimigos_restantes -= mobs_ativos[0] - len(Variaveis_globais.grupo_inimigos1)
                efeito_morte.play()
                
                projetil_aliado.kill()

            if colisoes_projetil_inimigo2:
                Variaveis_globais.inimigos_restantes -= mobs_ativos[0] - len(Variaveis_globais.grupo_inimigos2)
                efeito_morte.play()

                projetil_aliado.kill()
    
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
                Variaveis_globais.vidas_castelo -= 1
                Variaveis_globais.inimigos_restantes -= 1
                efeito_morte.play()

            objeto.kill()



colisoes = VerificarColisoes()