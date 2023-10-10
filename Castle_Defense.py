from Configurações.config import *
from Configurações import Variaveis_globais, Controles
import Player
import Inimigos
import Castelo
from Efeitos import buff_01, buff_02, animacoes
from Verificações import Duracao_buffs, Colisoes




# função para definir o modo de jogo e outras coisas
def iniciar_jogo():

    Variaveis_globais.ganhou = False
    Variaveis_globais.perdeu = False
    Variaveis_globais.vidas_castelo = 10

    if Variaveis_globais.dificuldade == 1:

        Variaveis_globais.inimigos_totais = 50
        Variaveis_globais.inimigos_restantes = Variaveis_globais.inimigos_totais
        Variaveis_globais.velocidade_inimigo = 500 / fps

    if Variaveis_globais.dificuldade == 2:

        Variaveis_globais.inimigos_totais = 70
        Variaveis_globais.inimigos_restantes = Variaveis_globais.inimigos_totais
        Variaveis_globais.velocidade_inimigo = 700 / fps

    if Variaveis_globais.dificuldade == 3:

        Variaveis_globais.inimigos_totais = 100
        Variaveis_globais.inimigos_restantes = Variaveis_globais.inimigos_totais
        Variaveis_globais.velocidade_inimigo = 800 / fps

    

    pygame.mixer_music.play(-1)






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

mensagem_ajustar_tela = 'Ajustar dimensões'
mensagem_ajustar_tela_para_tela = fonte.render(mensagem_ajustar_tela, True, (50, 50, 255))

selecionou = False

while not selecionou:

    # retangulos visuais
    pygame.draw.rect(tela, (140, 140, 140), (655, 140, 200, 50))
    pygame.draw.rect(tela, (100, 100, 100), (655, 240, 200, 50))
    pygame.draw.rect(tela, (60, 60, 60), (655, 340, 200, 50))

    pygame.draw.rect(tela, (200, 200, 200), (135, 140, 300, 50))

    # retangulos para colisão
    facil_rect = pygame.Rect(655, 140, 200, 50)
    medio_rect = pygame.Rect(655, 240, 200, 50)
    dificil_rect = pygame.Rect(655, 340, 200, 50)

    ajuste_rect = pygame.Rect(135, 140, 300, 50)

    # desenhar mensagens
    tela.blit(mensagem_dificuldade_para_tela, (600, 70))
    tela.blit(mensagem_facil_para_tela, (720, 150))
    tela.blit(mensagem_medio_para_tela, (705, 250))
    tela.blit(mensagem_dificil_para_tela, (715, 350))

    tela.blit(mensagem_ajustar_tela_para_tela, (150, 145))

    display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()

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
                largura_da_tela = int(largura_da_tela * 0.95)
                altura_da_tela = int(altura_da_tela * 0.55)
                proprocao = largura_da_tela * altura_da_tela / 750000
                tela = display.set_mode((largura_da_tela, altura_da_tela))

iniciar_jogo()
# laço principal
while True:

    # plano de fundo da  tela 'fluido'
    tela.blit(plano_de_fundo, (-1200, 0))

    Duracao_buffs.conferir_buffs()

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

    if len(Variaveis_globais.grupo_efeito1) < 1 and chance1 <= chance:
        efeito_buff1 = buff_01.SpritesEfeito1()
        Variaveis_globais.todas_as_sprites.add(efeito_buff1)
        Variaveis_globais.grupo_efeito1.add(efeito_buff1)

    chance2 = uniform(0, 100)

    if len(Variaveis_globais.grupo_efeito2) < 1 and chance2 <= chance:
        efeito_buff2 = buff_02.SpritesEfeito2()
        Variaveis_globais.todas_as_sprites.add(efeito_buff2)
        Variaveis_globais.grupo_efeito2.add(efeito_buff2)

    # adiconar objetos sprites na tela
    Variaveis_globais.todas_as_sprites.draw(tela)
    Variaveis_globais.todas_as_sprites.update()

    # verificar colisões
    Colisoes.colisoes.colisao_com_player()
    Colisoes.colisoes.colisao_com_castelo()
    Colisoes.colisoes.colisao_com_projetil_player()

    # para criar texto na janela
    mensagem_kills = f"inimigos restantes: {Variaveis_globais.inimigos_restantes}"
    mensagem_kills_para_tela = fonte.render(mensagem_kills, True, (80, 80, 255))

    mensagem_vidas_castelo = f"vidas restantes: {Variaveis_globais.vidas_castelo}"
    mensagem_vidas_castelo_para_tela = fonte.render(mensagem_vidas_castelo, True, (247, 24, 14))

    mensagem_barreira = f'defesa: {Variaveis_globais.barreira}'
    mensagem_barreira_para_tela = fonte.render(mensagem_barreira, True, (255, 100, 20))

    mensagem_derrota = "você perdeu, pressione enter para continuar"
    mensagem_derrota_para_tela = fonte.render(mensagem_derrota, False,  (200, 0, 0))

    mensagem_vitoria = "você ganhou! pressione enter para continuar"
    mensagem_vitoria_para_tela = fonte.render(mensagem_vitoria, True, (255, 255, 0))

    # responder a eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            print("game over")
            dados = pandas.DataFrame(Variaveis_globais.maior_recorde)

            dados.to_csv('records/recorde_difícil.csv', index=False)
            print(dados)
            quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and not Player.projetil_player.clicou:
            Player.projetil_player.clicou = True
            Player.projetil_player.atirar()

        # responde aos eventos do controle
        if event.type == JOYAXISMOTION:
            Controles.controle.movimento(event)

        if event.type == JOYDEVICEADDED:
            Controles.controle.__init__()

    # para mover player ao pressionar tecla, ou joystick
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT] or Variaveis_globais.eixo_x_joystick >= 0.4:
        Variaveis_globais.x_player -= Variaveis_globais.velocidade_player
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT] or Variaveis_globais.eixo_x_joystick >= 0.4:
        Variaveis_globais.x_player += Variaveis_globais.velocidade_player
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] or Variaveis_globais.eixo_y_joystick >= 0.4:
        Variaveis_globais.y_player -= Variaveis_globais.velocidade_player
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN] or Variaveis_globais.eixo_y_joystick >= 0.4:
        Variaveis_globais.y_player += Variaveis_globais.velocidade_player

    # mudança de velocidade dos inimigos
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

    # resposta para derrota
    if Variaveis_globais.vidas_castelo <= 0:
        Variaveis_globais.perdeu = True
        efeito_derrota.play()

        while Variaveis_globais.perdeu:
            tela.blit(mensagem_derrota_para_tela, (450, 20))
            display.flip()

            pygame.mixer_music.fadeout(100)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        iniciar_jogo()

    # resposta para vitória
    if Variaveis_globais.inimigos_restantes <= 0:
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
            tela.blit(mensagem_vitoria_para_tela, (450, 20))
            display.flip()

            pygame.mixer_music.fadeout(100)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        iniciar_jogo()

    # colocar o texto na janela
    tela.blit(mensagem_kills_para_tela, (650, 20))
    tela.blit(mensagem_vidas_castelo_para_tela, (20, 20))
    if Variaveis_globais.barreira > 0:
        tela.blit(mensagem_barreira_para_tela, (80, 80))

    # atualizar a tela
    display.flip()

    clock.tick(fps)
