from funcoes_main import *
from Telas import menu_principal
from Componentes import botoes, icones
import funcoes_main

def tela_opcoes():
    selecionou = False

    while not selecionou:
        for componente in Variaveis_globais.componentes:
            componente.kill()

        icone_de_fundo = icones.IconeBackground((Variaveis_globais.dimensoes_janela[0] // 2,
                                                Variaveis_globais.dimensoes_janela[1] // 2), 
                                                (Variaveis_globais.dimensoes_janela[0] * 0.4, Variaveis_globais.dimensoes_janela[1] * 0.6))
        botao_continuar = botoes.Botao("Continuar", 
                                       (255, 50, 50), 
                                       (Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.30)), 
                                       (300, 60))
        botao_reiniciar = botoes.Botao("Reiniciar",
                                        (255, 50, 50), 
                                        (Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.45)), 
                                        (300, 60))
        botao_menu = botoes.Botao("Menu Principal", 
                                    (255, 50, 50), 
                                    (Variaveis_globais.dimensoes_janela[0] // 2, (Variaveis_globais.dimensoes_janela[1] * 0.60)), 
                                    (300, 60))
    
        Variaveis_globais.componentes.add(icone_de_fundo)
        Variaveis_globais.componentes.add(botao_continuar)
        Variaveis_globais.componentes.add(botao_reiniciar)
        Variaveis_globais.componentes.add(botao_menu)
        
        Variaveis_globais.componentes.draw(Variaveis_globais.tela)
        Variaveis_globais.componentes.update()

        display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                funcoes_main.ajustar_tela()
        
            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                posicao_mouse = pygame.mouse.get_pos()

                if botao_continuar.rect.collidepoint(posicao_mouse):
                    selecionou = True

                if botao_reiniciar.rect.collidepoint(posicao_mouse):
                    selecionou = True

                    for sprite in Variaveis_globais.todas_as_sprites:
                        if sprite in Variaveis_globais.grupo_todos_inimigos or sprite in Variaveis_globais.grupo_todos_efeitos or sprite in Variaveis_globais.grupo_projeteis_aliados:
                            sprite.kill()

                    Variaveis_globais.ganhou = False
                    Variaveis_globais.perdeu = False
                    Variaveis_globais.vidas_castelo = 10
                    Variaveis_globais.barreira = 0

                    Player.player.rect.center = (Variaveis_globais.dimensoes_janela[0] // 2, Variaveis_globais.dimensoes_janela[1] // 2)

                    if Variaveis_globais.dificuldade == 1:

                        Variaveis_globais.inimigos_totais = 60
                        Variaveis_globais.inimigos_restantes = Variaveis_globais.inimigos_totais
                        Variaveis_globais.velocidade_inimigo = velocidade_base_inimigo * 0.70 * Variaveis_globais.proporcao
                    if Variaveis_globais.dificuldade == 2:

                        Variaveis_globais.inimigos_totais = 80
                        Variaveis_globais.inimigos_restantes = Variaveis_globais.inimigos_totais
                        Variaveis_globais.velocidade_inimigo = velocidade_base_inimigo * Variaveis_globais.proporcao

                    if Variaveis_globais.dificuldade == 3:

                        Variaveis_globais.inimigos_totais = 120
                        Variaveis_globais.inimigos_restantes = Variaveis_globais.inimigos_totais
                        Variaveis_globais.velocidade_inimigo = velocidade_base_inimigo * 1.15 * Variaveis_globais.proporcao

                    pygame.mixer_music.play(-1)
                                    

                if botao_menu.rect.collidepoint(posicao_mouse):
                    selecionou = True

                    menu_principal.menu_principal()
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True

            