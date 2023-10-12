import pandas
import pygame
from pygame import *
import sys
from random import randint, uniform
import os
import numpy


# iniciar o pygame
pygame.init()

# iniciar joisticks
pygame.joystick.init()

# variáveis
plano_de_fundo = pygame.image.load("imagens/cenário.jpg")
plano_de_fundo = pygame.transform.scale(plano_de_fundo, (3000, 1000))

pygame.mixer.music.set_volume(0.9)
musica_fundo = pygame.mixer.music.load("sons/musica de fundo.wav")
pygame.mixer.music.play(-1)

efeito_explosao = pygame.mixer.Sound("sons/explosão.wav")
efeito_morte = pygame.mixer.Sound("sons/morte inimigos.wav")
efeito_vitoria = pygame.mixer.Sound('sons/vitoria.wav')
efeito_derrota = pygame.mixer.Sound('sons/derrota.wav')
efeito_defesa = pygame.mixer.Sound('sons/defesa mágica.wav')

efeito_derrota.set_volume(0.1)
efeito_explosao.set_volume(0.5)
efeito_vitoria.set_volume(0.7)


fonte = pygame.font.SysFont("arial", 30, True, False)

# obter a resulução da tela do pc
informacao_da_tela = pygame.display.Info()

largura_do_monitor = informacao_da_tela.current_w
altura_do_monitor = informacao_da_tela.current_h

largura_da_janela = int(informacao_da_tela.current_w * 0.9)
altura_da_janela = int(informacao_da_tela.current_h * 0.65)

# dimensão base: 1500 x 500
proporcao = largura_da_janela * altura_da_janela / (1500 * 500)

fps = 120

velocidade_base_player = 3
velocidade_base_projetil = 10
velocidade_base_inimigo = 6

dificuldade = 0

# criar a tela
tela = display.set_mode((largura_da_janela, altura_da_janela), pygame.RESIZABLE)


# definir cor da tela
tela.fill((000, 000, 000))

# definir título da tela
display.set_caption("Castelo Arcano")