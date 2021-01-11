import random

import pygame

pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)
verde = (46, 139, 87)


class Snake:
    cor = (0, 0, 0)
    tamanho = (10, 10)
    velocidade = 0.09

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]

        self.direcao = "direita"

    def blit(self, screen):
        for posicao in self.corpo:
            screen.blit(self.textura, posicao)

    def andar(self):
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        if self.direcao == "direita":
            self.corpo[0] = (x + self.velocidade, y)
        elif self.direcao == "esquerda":
            self.corpo[0] = (x - self.velocidade, y)
        elif self.direcao == "cima":
            self.corpo[0] = (x, y - self.velocidade)
        elif self.direcao == "baixo":
            self.corpo[0] = (x, y + self.velocidade)

    def cima(self):
        if self.direcao != "baixo":
            self.direcao = "cima"

    def baixo(self):
        if self.direcao != "cima":
            self.direcao = "baixo"

    def direita(self):
        if self.direcao != "esquerda":
            self.direcao = "direita"

    def esquerda(self):
        if self.direcao != "direita":
            self.direcao = "esquerda"


class Frutinha:
    cor = (139, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        x = random.randint(0, 49) * 10
        y = random.randint(0, 49) * 10
        self.posicao = (x, y)

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)



frutinha = Frutinha()
cobrinha = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cobrinha.cima()
                break
            elif event.key == pygame.K_DOWN:
                cobrinha.baixo()
                break
            elif event.key == pygame.K_LEFT:
                cobrinha.esquerda()
                break
            elif event.key == pygame.K_RIGHT:
                cobrinha.direita()
                break

        
    cobrinha.andar()
    screen.fill(verde)

    frutinha.blit(screen)
    cobrinha.blit(screen)

    pygame.display.update()