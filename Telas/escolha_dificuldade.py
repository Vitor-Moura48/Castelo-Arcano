from funcoes_main import *
from Telas import menu_principal
from Componentes import botoes
import funcoes_main

# função para definir o modo de jogo e outras coisas
def iniciar_jogo():
    
    # fazer uma tela inicial
    mensagem_dificuldade = 'Selecione a dificuldade'
    mensagem_dificuldade_para_tela = fonte.render(mensagem_dificuldade, True, (255, 50, 50))

    selecionou = False

    for componente in Global.componentes:
        componente.kill()

    botao_facil = botoes.Botao_1("Fácil", 
                                (255, 50, 50), 
                                (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.25)), 
                                (300, 60))
    botao_normal = botoes.Botao_1("Normal", 
                                (255, 50, 50), 
                                (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.40)), 
                                (300, 60))
    botao_dificil = botoes.Botao_1("Dificil", 
                                    (255, 50, 50),
                                    (Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.55)), 
                                    (300, 60))

    Global.componentes.add(botao_facil)
    Global.componentes.add(botao_normal)
    Global.componentes.add(botao_dificil)

    while not selecionou:
        Global.tela.fill((000, 000, 000))

        for sprite in Global.todas_as_sprites:
            if sprite in Global.grupo_todos_inimigos or sprite in Global.grupo_todos_efeitos or sprite in Global.grupo_projeteis_aliados or sprite in Global.grupo_projeteis_inimigos:
                sprite.kill()

        Global.componentes.draw(Global.tela)
        Global.componentes.update()

        # desenhar mensagens
        Global.tela.blit(mensagem_dificuldade_para_tela, (Global.dimensoes_janela[0] // 2 - 160, 70 * Global.proporcao))
    
        display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                funcoes_main.ajustar_tela()

                botao_facil.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.25)))
                botao_normal.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.40)))
                botao_dificil.ajustar_posicoes((Global.dimensoes_janela[0] // 2, (Global.dimensoes_janela[1] * 0.55)))

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()

                if botao_facil.rect.collidepoint(posicao_mouse):
                    Global.dificuldade = 1
                    selecionou = True

                if botao_normal.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    Global.dificuldade = 2

                if botao_dificil.rect.collidepoint(posicao_mouse):
                    selecionou = True
                    Global.dificuldade = 3
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    selecionou = True
                    menu_principal.menu_principal()

    Global.ganhou = False
    Global.perdeu = False
    Global.vidas_castelo = 10
    Player.player.vida_restante = 5
    Global.barreira = 0

    Player.player.rect.center = (Global.dimensoes_janela[0] // 2, Global.dimensoes_janela[1] // 2)

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

    if Global.som_ligado:
        pygame.mixer_music.play(-1)
