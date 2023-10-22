from Configurações.config import *
from Configurações import Variaveis_globais, Controles
from mobs import Player, Inimigos, Castelo
from Efeitos import buff_01, buff_02, animacoes
from Verificações import Colisoes

# função para definir o modo de jogo e outras coisas
def iniciar_jogo():

    Variaveis_globais.ganhou = False
    Variaveis_globais.perdeu = False
    Variaveis_globais.vidas_castelo = 10

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


def adicioanr_objetos():
    # adicionar objetos
    if len(Variaveis_globais.grupo_inimigos1) < 2 and len(Variaveis_globais.grupo_todos_inimigos) < Variaveis_globais.inimigos_restantes:
        for i in range(1):
            inimigo1 = Inimigos.SpritesInimigo1()
            Variaveis_globais.todas_as_sprites.add(inimigo1)
            Variaveis_globais.grupo_inimigos1.add(inimigo1)
            Variaveis_globais.grupo_todos_inimigos.add(inimigo1)

    if len(Variaveis_globais.grupo_inimigos2) < 1 and len(Variaveis_globais.grupo_todos_inimigos) < Variaveis_globais.inimigos_restantes:
        for i in range(1):
            inimigo2 = Inimigos.SpritesInimigo2()
            Variaveis_globais.todas_as_sprites.add(inimigo2)
            Variaveis_globais.grupo_inimigos2.add(inimigo2)
            Variaveis_globais.grupo_todos_inimigos.add(inimigo2)

    # porcentagem de aparecimento a cada iteração
    chance = 0.05
    chance1 = uniform(0, 100)

    if len(Variaveis_globais.grupo_todos_efeitos) < 2 and chance1 <= chance:
        efeito_buff1 = buff_01.SpritesEfeito1()
        Variaveis_globais.todas_as_sprites.add(efeito_buff1)
        Variaveis_globais.grupo_efeito1.add(efeito_buff1)
        Variaveis_globais.grupo_todos_efeitos.add(efeito_buff1)

    chance2 = uniform(0, 100)

    if len(Variaveis_globais.grupo_todos_efeitos) < 2 and chance2 <= chance:
        efeito_buff2 = buff_02.SpritesEfeito2()
        Variaveis_globais.todas_as_sprites.add(efeito_buff2)
        Variaveis_globais.grupo_efeito2.add(efeito_buff2)
        Variaveis_globais.grupo_todos_efeitos.add(efeito_buff2)

    # adiconar objetos sprites na tela
    Variaveis_globais.todas_as_sprites.draw(Variaveis_globais.tela)
    Variaveis_globais.todas_as_sprites.update()


def verificar_colisoes():
    Colisoes.colisoes.colisao_com_player()
    Colisoes.colisoes.colisao_com_castelo()
    Colisoes.colisoes.colisao_com_projetil_player()
    Colisoes.colisoes.saiu_do_mapa()


def criar_texto_na_janela():
    
    mensagem_kills = f"inimigos restantes: {Variaveis_globais.inimigos_restantes}"
    mensagem_kills_para_tela = fonte.render(mensagem_kills, True, (80, 80, 255))

    mensagem_vidas_castelo = f"vidas restantes: {Variaveis_globais.vidas_castelo}"
    mensagem_vidas_castelo_para_tela = fonte.render(mensagem_vidas_castelo, True, (247, 24, 14))

    mensagem_barreira = f'defesa: {Variaveis_globais.barreira}'
    mensagem_barreira_para_tela = fonte.render(mensagem_barreira, True, (255, 100, 20))


    # colocar o texto na janela
    Variaveis_globais.tela.blit(mensagem_kills_para_tela, (Variaveis_globais.dimensoes_janela[0] - 340, 20))
    Variaveis_globais.tela.blit(mensagem_vidas_castelo_para_tela, (20, 20))
    if Variaveis_globais.barreira > 0:
        Variaveis_globais.vidas_castelo
        Variaveis_globais.tela.blit(mensagem_barreira_para_tela, (80, 80))


def responder_a_eventos():
    # responder a eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            print("game over")
            dados = pandas.DataFrame(Variaveis_globais.maior_recorde)

            dados.to_csv('records/recorde_difícil.csv', index=False)
            print(dados)
            quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and Variaveis_globais.tempo_de_recarga <= 0:
            projetil_player = Player.Projetil()
            Variaveis_globais.grupo_projeteis_aliados.add(projetil_player)
            Variaveis_globais.todas_as_sprites.add(projetil_player)
            projetil_player.atirar()
            Variaveis_globais.tempo_de_recarga = 60

        # responde aos eventos do controle
        if event.type == JOYAXISMOTION:
            Controles.controle.movimento(event)

        if event.type == JOYDEVICEADDED:
            Controles.controle.__init__()
        
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

            Variaveis_globais.proporcao = Variaveis_globais.dimensoes_janela[0] / dimensao_base[0]

            Castelo.castelo.rect_ajustado = pygame.Rect.inflate(Castelo.castelo.rect, int(Castelo.castelo.rect_base.width * Variaveis_globais.proporcao - Castelo.castelo.rect.width), int(Castelo.castelo.rect_base.height * Variaveis_globais.proporcao - Castelo.castelo.rect.height))
            Castelo.castelo.rect = Castelo.castelo.rect_ajustado

            retangulo_ajustado = pygame.Rect.inflate(Player.player.rect, int(Player.player.rect_base.width * Variaveis_globais.proporcao - Player.player.rect.width), int(Player.player.rect_base.height * Variaveis_globais.proporcao - Player.player.rect.height))
            Player.player.rect = retangulo_ajustado

def gerenciar_waves(): 
    if Variaveis_globais.inimigos_restantes <= Variaveis_globais.inimigos_totais * 0.8 and not Variaveis_globais.mudanca_de_velocidade[0]:
            Variaveis_globais.velocidade_inimigo *= 1.04
            Variaveis_globais.mudanca_de_velocidade[0] = True

    elif Variaveis_globais.inimigos_restantes <= Variaveis_globais.inimigos_totais * 0.6 and not Variaveis_globais.mudanca_de_velocidade[1]:
        Variaveis_globais.velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[1] = True

    elif Variaveis_globais.inimigos_restantes <= Variaveis_globais.inimigos_totais * 0.4 and not Variaveis_globais.mudanca_de_velocidade[2]:
        Variaveis_globais.velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[2] = True

    elif Variaveis_globais.inimigos_restantes <= Variaveis_globais.inimigos_totais * 0.2 and not Variaveis_globais.mudanca_de_velocidade[3]:
        Variaveis_globais.velocidade_inimigo *= 1.04
        Variaveis_globais.mudanca_de_velocidade[3] = True
    
def responder_a_derrota():
    Variaveis_globais.perdeu = True
    efeito_derrota.play()

    while Variaveis_globais.perdeu:
        Variaveis_globais.tela.blit(mensagem_derrota_para_tela, ((Variaveis_globais.dimensoes_janela[0] // 2 - 290), 80))
        display.flip()

        pygame.mixer_music.fadeout(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    iniciar_jogo()


def responder_a_vitoria():
    Variaveis_globais.ganhou = True
    efeito_vitoria.play()

    if Variaveis_globais.dificuldade == 1:
        novo_dataframe = pandas.DataFrame(data=[Variaveis_globais.vidas_castelo], columns=['Recorde'])
        novo_dataframe.to_csv('records/recorde_fácil.csv', mode='a', index=False, header=False)
    if Variaveis_globais.dificuldade == 2:
        novo_dataframe = pandas.DataFrame()
        novo_dataframe.to_csv('records/recorde_médio.csv', mode='a', index=False, header=False)
    if Variaveis_globais.dificuldade == 3:
        novo_dataframe = pandas.DataFrame(Variaveis_globais.maior_recorde)
        novo_dataframe.to_csv('records/recorde_difícil.csv', mode='a', index=False, header=False)

    while Variaveis_globais.ganhou:
        Variaveis_globais.tela.blit(mensagem_vitoria_para_tela, ((Variaveis_globais.dimensoes_janela[0] // 2 - 290), 80))
        display.flip()

        pygame.mixer_music.fadeout(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    iniciar_jogo()

# criar um clock de atualização em fps
clock = time.Clock()

# fazer uma tela inicial
mensagem_dificuldade = 'Selecione a dificuldade'
mensagem_dificuldade_para_tela = fonte.render(mensagem_dificuldade, True, (255, 50, 50))

mensagem_facil = 'Fácil'
mensagem_facil_para_tela = fonte.render(mensagem_facil, True, (255, 50, 50))

mensagem_medio = 'Normal'
mensagem_medio_para_tela = fonte.render(mensagem_medio, True, (255, 50, 50))

mensagem_dificil = 'Difícil'
mensagem_dificil_para_tela = fonte.render(mensagem_dificil, True, (255, 50, 50))

mensagem_ajustar_tela = 'Tela Cheia'
mensagem_tela_cheia = fonte.render(mensagem_ajustar_tela, True, (50, 50, 255))

selecionou = False


while not selecionou:

    # retangulos visuais
    pygame.draw.rect(Variaveis_globais.tela, (140, 140, 140), ((Variaveis_globais.dimensoes_janela[0] // 2) - (200 // 2), 140, 200, 50))
    pygame.draw.rect(Variaveis_globais.tela, (100, 100, 100), ((Variaveis_globais.dimensoes_janela[0] // 2) - (200 // 2), 240, 200, 50))
    pygame.draw.rect(Variaveis_globais.tela, (60, 60, 60), ((Variaveis_globais.dimensoes_janela[0] // 2) - (200 // 2), 340, 200, 50))

    pygame.draw.rect(Variaveis_globais.tela, (200, 200, 200), ((Variaveis_globais.dimensoes_janela[0] // 2) - (300 // 2), 440, 300, 50))

    # retangulos para colisão
    facil_rect = pygame.Rect((Variaveis_globais.dimensoes_janela[0] // 2) - (200 // 2), 140, 200, 50)
    medio_rect = pygame.Rect((Variaveis_globais.dimensoes_janela[0] // 2) - (200 // 2), 240, 200, 50)
    dificil_rect = pygame.Rect((Variaveis_globais.dimensoes_janela[0] // 2) - (200 // 2), 340, 200, 50)

    ajuste_rect = pygame.Rect((Variaveis_globais.dimensoes_janela[0] // 2) - (300 // 2), 440, 300, 50)

    # desenhar mensagens
    Variaveis_globais.tela.blit(mensagem_dificuldade_para_tela, (Variaveis_globais.dimensoes_janela[0] // 2 - 160, 70))
    Variaveis_globais.tela.blit(mensagem_facil_para_tela, ((Variaveis_globais.dimensoes_janela[0] // 2) - 35, 150))
    Variaveis_globais.tela.blit(mensagem_medio_para_tela, ((Variaveis_globais.dimensoes_janela[0] // 2) - 50, 250))
    Variaveis_globais.tela.blit(mensagem_dificil_para_tela, ((Variaveis_globais.dimensoes_janela[0] // 2) - 42, 350))

    Variaveis_globais.tela.blit(mensagem_tela_cheia, ((Variaveis_globais.dimensoes_janela[0] // 2) - 70, 450))

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

            if facil_rect.collidepoint(posicao_mouse):
                Variaveis_globais.dificuldade = 1
                selecionou = True

            if medio_rect.collidepoint(posicao_mouse):
                selecionou = True
                Variaveis_globais.dificuldade = 2

            if dificil_rect.collidepoint(posicao_mouse):
                selecionou = True
                Variaveis_globais.dificuldade = 3

            if ajuste_rect.collidepoint(posicao_mouse):
                tela = display.set_mode((informacoes_tela.current_w, informacoes_tela.current_h), pygame.FULLSCREEN, 32)
                Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()
                Variaveis_globais.proporcao = Variaveis_globais.dimensoes_janela[0] / dimensao_base[0]

                Castelo.castelo.rect_ajustado = pygame.Rect.inflate(Castelo.castelo.rect, int(Castelo.castelo.rect_base.width * Variaveis_globais.proporcao - Castelo.castelo.rect.width), int(Castelo.castelo.rect_base.height * Variaveis_globais.proporcao - Castelo.castelo.rect.height))
                Castelo.castelo.rect = Castelo.castelo.rect_ajustado

                retangulo_ajustado = pygame.Rect.inflate(Player.player.rect, int(Player.player.rect_base.width * Variaveis_globais.proporcao - Player.player.rect.width), int(Player.player.rect_base.height * Variaveis_globais.proporcao - Player.player.rect.height))
                Player.player.rect = retangulo_ajustado
    