from Configurações.config import *
from Configurações import Variaveis_globais, Controles
from Verificações import Duracao_buffs
import funcoes_main


funcoes_main.chamar_menu_principal()

# laço principal
while True:

    # plano de fundo da  tela
    Variaveis_globais.tela.blit(plano_de_fundo, (-1200, 0))

    Duracao_buffs.conferir_buffs()
    Variaveis_globais.dimensoes_janela = pygame.display.get_surface().get_size()

    funcoes_main.adicioanr_objetos()

    funcoes_main.verificar_colisoes()

    funcoes_main.criar_texto_na_janela()
    
    Variaveis_globais.tempo_de_recarga -= 1
    
    funcoes_main.responder_a_eventos()

    Controles.conferir_teclado()

    # mudança de velocidade dos inimigos
    funcoes_main.gerenciar_waves()

    # resposta para derrota
    if Variaveis_globais.vidas_castelo <= 0:
        funcoes_main.responder_a_derrota()

    # resposta para vitória
    if Variaveis_globais.inimigos_restantes <= 0:
        funcoes_main.responder_a_vitoria()
    
    # atualizar a tela
    display.flip()

    funcoes_main.clock.tick(fps)
