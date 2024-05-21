from Configurações.config import pygame
from Configurações import Global

class Texto():
    def __init__(self, texto, cor, tamanho, ponto_inicio, limite_fim, espacamento=5):

        self.ponto_inicio = ponto_inicio
        self.limite_fim = limite_fim
        self.tamanho = tamanho
        self.texto = texto
        self.cor = cor
        self.espacamento = espacamento
        
        self.ajustar_posicoes()
        self.update()

    def ajustar_posicoes(self):
        self.distancia = int(Global.dimensoes_janela[0] * self.limite_fim) - int(Global.dimensoes_janela[0] * self.ponto_inicio[0])
        self.fonte = pygame.font.SysFont("arial", int(self.tamanho * Global.proporcao), True, False)

        # para armazenar as linhas necessarias
        self.linhas = []
        distancia_atual = 0
        linha_atual = ''

        # obtem as linhas necessarias
        self.palavras = self.texto.split(" ")
        for palavra in self.palavras:
            if (self.fonte.size(palavra)[0] + distancia_atual) < self.distancia:
                linha_atual += palavra + ' '
                distancia_atual += self.fonte.size(palavra)[0]
            else:
                self.linhas.append(linha_atual)
                linha_atual = palavra + ' '
                distancia_atual = self.fonte.size(palavra)[0]
        self.linhas.append(linha_atual)
        
        # renderiza as linhas
        self.linhas_renderizadas = [self.fonte.render(linha, True, self.cor) for linha in self.linhas]

    def update(self):
        espacamento_y = 0
        for linha in self.linhas_renderizadas:
            Global.tela.blit( linha, (int(Global.dimensoes_janela[0] * self.ponto_inicio[0]), int(Global.dimensoes_janela[1] * self.ponto_inicio[1] + espacamento_y)) ) # desenhar mensagens
            espacamento_y += self.espacamento + self.fonte.size('')[1]