from Configurações.config import *
from Configurações import Controles, Global
from Verificações import Duracao_buffs
import funcoes_main

funcoes_main.conferir_arquivos_csv()
funcoes_main.chamar_menu_principal()
    
# laço principal
while True:

    # plano de fundo da  tela
    Global.tela.blit(plano_de_fundo, (-1200, 0))

    Duracao_buffs.conferir_buffs()
    Global.dimensoes_janela = pygame.display.get_surface().get_size()

    funcoes_main.adicioanr_objetos()

    funcoes_main.verificar_colisoes()

    funcoes_main.criar_texto_na_janela()

    funcoes_main.contabilizar_tempo_recargas()

    funcoes_main.responder_a_eventos()

    Controles.conferir_teclado()

    # mudança de velocidade dos inimigos
    funcoes_main.gerenciar_waves()

    # resposta para derrota
    funcoes_main.verificar_derrota_vitoria()
    
    # atualizar a tela
    display.flip()

    funcoes_main.clock.tick(fps)
