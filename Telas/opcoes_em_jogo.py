from funcoes_main import *
from Telas import menu_principal
from Objetos.Componentes import botoes, icones
import funcoes_main

def tela_opcoes():
    selecionou = False

    for componente in Global.componentes:
        componente.kill()

    icone_de_fundo = icones.IconeBackground((Global.dimensoes_janela[0] // 2,
                                            Global.dimensoes_janela[1] // 2), 
                                            (Global.dimensoes_janela[0] * 0.4, Global.dimensoes_janela[1] * 0.6))
    botao_continuar = botoes.Botao_1("Continuar", 
                                    (255, 50, 50), 
                                    (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.30)), 
                                    (300, 60))
    botao_reiniciar = botoes.Botao_1("Reiniciar",
                                    (255, 50, 50), 
                                    (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.45)), 
                                    (300, 60))
    botao_menu = botoes.Botao_1("Menu Principal", 
                                (255, 50, 50), 
                                (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.60)), 
                                (300, 60))

    Global.componentes.add(icone_de_fundo)
    Global.componentes.add(botao_continuar)
    Global.componentes.add(botao_reiniciar)
    Global.componentes.add(botao_menu)

    while not selecionou:
        
        Global.componentes.draw(Global.tela)
        Global.componentes.update()

        display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                funcoes_main.ajustar_tela()

                icone_de_fundo.ajustar_posicoes((Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2),
                                                (Global.dimensoes_janela[0] * 0.4, Global.dimensoes_janela[1] * 0.6))
                botao_continuar.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.30)))
                botao_reiniciar.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.45)))
                botao_menu.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.60)))
        
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                posicao_mouse = pygame.mouse.get_pos()

                if botao_continuar.rect.collidepoint(posicao_mouse):
                    selecionou = True

                if botao_reiniciar.rect.collidepoint(posicao_mouse):
                    selecionou = True

                    for sprite in Global.todas_as_sprites:
                        if sprite in Global.grupo_todos_inimigos or sprite in Global.grupo_todos_efeitos or sprite in Global.grupo_projeteis_aliados:
                            sprite.kill()

                    Global.ganhou = False
                    Global.perdeu = False
                    Global.barreira = 0

                    Global.player.rect.center = (Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2)

                    if Global.dificuldade == 1:

                        Global.inimigos_totais = 60
                        Global.inimigos_restantes = Global.inimigos_totais
                        Global.velocidade_inimigo = velocidade_base_inimigo * 0.70 * Global.proporcao
                    if Global.dificuldade == 2:

                        Global.inimigos_totais = 80
                        Global.inimigos_restantes = Global.inimigos_totais
                        Global.velocidade_inimigo = velocidade_base_inimigo * Global.proporcao

                    if Global.dificuldade == 3:

                        Global.inimigos_totais = 120
                        Global.inimigos_restantes = Global.inimigos_totais
                        Global.velocidade_inimigo = velocidade_base_inimigo * 1.15 * Global.proporcao

                    pygame.mixer_music.play(-1)
                                    

                if botao_menu.rect.collidepoint(posicao_mouse):
                    selecionou = True

                    menu_principal.menu_principal()
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True

            