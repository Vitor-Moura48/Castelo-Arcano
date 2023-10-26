from funcoes_main import *
from Telas import menu_principal
from Componentes import botoes


# função para definir o modo de jogo e outras coisas
def iniciar_jogo():
    
    # fazer uma tela inicial
    mensagem_dificuldade = 'Selecione a dificuldade'
    mensagem_dificuldade_para_tela = fonte.render(mensagem_dificuldade, True, (255, 50, 50))

    selecionou = False

    while not selecionou:
        Variaveis_globais.tela.fill((000, 000, 000))

        for sprite in Variaveis_globais.todas_as_sprites:
            if sprite in Variaveis_globais.grupo_todos_inimigos or sprite in Variaveis_globais.grupo_todos_efeitos or sprite in Variaveis_globais.grupo_projeteis_aliados:
                sprite.kill()
        for componente in Variaveis_globais.componentes:
            componente.kill()

        botao_facil = botoes.Botao("Fácil", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 30, 145 * Variaveis_globais.proporcao), (Variaveis_globais.dimensoes_janela[0] // 2, 160 * Variaveis_globais.proporcao), (300, 60))
        botao_normal = botoes.Botao("Normal", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 45, 245 * Variaveis_globais.proporcao), (Variaveis_globais.dimensoes_janela[0] // 2, 260 * Variaveis_globais.proporcao), (300, 60))
        botao_dificil = botoes.Botao("Dificil", (255, 50, 50), (Variaveis_globais.dimensoes_janela[0] // 2 - 40, 345 * Variaveis_globais.proporcao), (Variaveis_globais.dimensoes_janela[0] // 2, 360 * Variaveis_globais.proporcao), (300, 60))
    
        Variaveis_globais.componentes.add(botao_facil)
        Variaveis_globais.componentes.add(botao_normal)
        Variaveis_globais.componentes.add(botao_dificil)

        Variaveis_globais.componentes.draw(Variaveis_globais.tela)
        Variaveis_globais.componentes.update()

        # desenhar mensagens
        Variaveis_globais.tela.blit(mensagem_dificuldade_para_tela, (Variaveis_globais.dimensoes_janela[0] // 2 - 160, 70 * Variaveis_globais.proporcao))
    
        display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()

                # se o x for muito maior que o y
                if Variaveis_globais.dimensoes_janela[0] / Variaveis_globais.dimensoes_janela[1] > proporcao_altura_largura:

                    # se eu diminui o y
                    if Variaveis_globais.dimensoes_janela[0] * Variaveis_globais.dimensoes_janela[1] / (dimensao_base[0] * dimensao_base[1]) < Variaveis_globais.proporcao:
                        Variaveis_globais.tela = display.set_mode((Variaveis_globais.dimensoes_janela[1] * proporcao_altura_largura, Variaveis_globais.dimensoes_janela[1]), pygame.RESIZABLE)
                    # se eu aumentei o x
                    else:
                        Variaveis_globais.tela = display.set_mode((Variaveis_globais.dimensoes_janela[0], Variaveis_globais.dimensoes_janela[0] / proporcao_altura_largura), pygame.RESIZABLE)
                    
                    Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()

                # se o y for muito maior que o x
                elif Variaveis_globais.dimensoes_janela[0] / Variaveis_globais.dimensoes_janela[1] < proporcao_altura_largura:

                    # se eu diminui o x
                    if Variaveis_globais.dimensoes_janela[0] * Variaveis_globais.dimensoes_janela[1] / (dimensao_base[0] * dimensao_base[1]) < Variaveis_globais.proporcao:
                        Variaveis_globais.tela = display.set_mode((Variaveis_globais.dimensoes_janela[0], Variaveis_globais.dimensoes_janela[0] / proporcao_altura_largura), pygame.RESIZABLE)
                    # se eu aumentei o y
                    else:
                        Variaveis_globais.tela = display.set_mode((Variaveis_globais.dimensoes_janela[1] * proporcao_altura_largura, Variaveis_globais.dimensoes_janela[1]), pygame.RESIZABLE)
                    
                    Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()

                Variaveis_globais.proporcao = Variaveis_globais.proporcao = Variaveis_globais.dimensoes_janela[0] / dimensao_base[0]

                Castelo.castelo.rect_ajustado = pygame.Rect.inflate(Castelo.castelo.rect, int(Castelo.castelo.rect_base.width * Variaveis_globais.proporcao - Castelo.castelo.rect.width), int(Castelo.castelo.rect_base.height * Variaveis_globais.proporcao - Castelo.castelo.rect.height))
                Castelo.castelo.rect = Castelo.castelo.rect_ajustado

                retangulo_ajustado = pygame.Rect.inflate(Player.player.rect, int(Player.player.rect_base.width * Variaveis_globais.proporcao - Player.player.rect.width), int(Player.player.rect_base.height * Variaveis_globais.proporcao - Player.player.rect.height))
                Player.player.rect = retangulo_ajustado

              
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()

                if botao_facil.rect.collidepoint(posicao_mouse):
                    Variaveis_globais.dificuldade = 1
                    selecionou = True

                if botao_normal.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    Variaveis_globais.dificuldade = 2

                if botao_dificil.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    Variaveis_globais.dificuldade = 3
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True
                    menu_principal.menu_principal()

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
