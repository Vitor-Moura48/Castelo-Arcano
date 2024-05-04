import pandas
import pygame
from pygame import *
import sys
from random import randint, uniform, choice
import os
import numpy

# iniciar o pygame
pygame.init()

# iniciar joisticks
pygame.joystick.init()

# variáveis
plano_de_fundo = pygame.image.load("dados/imagens/cenário.jpg")
plano_de_fundo = pygame.transform.scale(plano_de_fundo, (3000, 1000))

pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load("dados/sons/musica de fundo.wav")

efeito_explosao = pygame.mixer.Sound("dados/sons/explosão.wav")
efeito_morte = pygame.mixer.Sound("dados/sons/morte inimigos.wav")
efeito_vitoria = pygame.mixer.Sound('dados/sons/vitoria.wav')
efeito_derrota = pygame.mixer.Sound('dados/sons/derrota.wav')
efeito_defesa = pygame.mixer.Sound('dados/sons/defesa mágica.wav')

efeito_derrota.set_volume(0.1)
efeito_explosao.set_volume(0.5)
efeito_vitoria.set_volume(0.7)

informacoes_tela = pygame.display.Info()
dimensao_base = (informacoes_tela.current_w * 0.7, informacoes_tela.current_h * 0.7)

# para cada 1 y de altura, tem n x de alrgura
proporcao_altura_largura =  dimensao_base[0] / dimensao_base[1]

fps = 120

velocidade_base_player = 4 
velocidade_base_projetil = 16
velocidade_base_inimigo = 6

# definir título da tela
display.set_caption("Castelo Arcano")