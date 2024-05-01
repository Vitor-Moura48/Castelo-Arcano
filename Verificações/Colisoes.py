from Configurações.config import *
from Configurações import Global
from Objetos import Mobs

class Colisoes:  # classe para verificar colisões
    # função para verificar colisão do jogador com algo
    def colisao_com_player(self):

        # verifica colisões com inimigos e responde de acordo
        for inimigo in Global.grupo_todos_inimigos:
            if pygame.sprite.collide_rect(Mobs.player, inimigo) and inimigo.contador_ivulnerabilidade <= 0:        
                inimigo.contador_ivulnerabilidade = 10
                inimigo.receber_dano(Mobs.player.dano)
        
        for projetil_inimigo in Global.grupo_projeteis_inimigos:
            if pygame.sprite.collide_rect(Mobs.player, projetil_inimigo):
                projetil_inimigo.perfuracoes -= 1
                Mobs.player.vida -= projetil_inimigo.dano

        for buff in Global.grupo_efeitos:
            if pygame.sprite.collide_rect(Mobs.player, buff):
                buff.ativar()
            
    # função para verificar colisões do castelo com algo
    def colisao_com_castelo(self):

        # verifica colisões com inimigos e responde de acordo
        for inimigo in Global.grupo_todos_inimigos:
            if pygame.sprite.collide_rect(Mobs.castelo, inimigo):

                Mobs.castelo.receber_dano(max(0, inimigo.dano - Global.barreira))
                if Global.som_ligado:
                    efeito_explosao.play() if Global.barreira == 0 else efeito_explosao.play()
                Global.barreira -= min(inimigo.dano, Global.barreira)
                inimigo.morrer()     
        
        for inimigo in Global.grupo_projeteis_inimigos:
            if pygame.sprite.collide_rect(Mobs.castelo, inimigo):

                Mobs.castelo.receber_dano(max(0, inimigo.dano - Global.barreira))
                if Global.som_ligado:
                    efeito_explosao.play() if Global.barreira == 0 else efeito_explosao.play()
                Global.barreira -= min(inimigo.dano, Global.barreira)     
                inimigo.perfuracoes -= 1
        
    # função para verificar colisões do projetil do jogador com algo
    def colisao_com_projetil_player(self):

        for projetil_aliado in Global.grupo_projeteis_aliados:
            for inimigo in Global.grupo_todos_inimigos:

                if pygame.sprite.collide_rect(projetil_aliado, inimigo) and inimigo.contador_ivulnerabilidade <= 0:

                    inimigo.receber_dano(Mobs.player.dano)
                    inimigo.contador_ivulnerabilidade = 10
                    projetil_aliado.perfuracoes -= 1
                
    def saiu_do_mapa(self):
        objetos_para_apagar = []
        for objeto in Global.todas_as_sprites:
            if objeto.rect.right < 0:
                objetos_para_apagar.append(objeto)

        for objeto in objetos_para_apagar:
            if objeto in Global.grupo_todos_inimigos:

                Global.inimigos_restantes -= 1
                Mobs.castelo.receber_dano(max(0, objeto.dano - Global.barreira))
                if Global.som_ligado:
                    efeito_explosao.play() if Global.barreira == 0 else efeito_defesa.play()
                Global.barreira -= min(objeto.dano, Global.barreira)     
            objeto.kill()

colisoes = Colisoes()