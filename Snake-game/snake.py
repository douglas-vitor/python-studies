import pygame

pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)

verde = (46, 139, 87)
screen.fill(verde)
pygame.display.update()

class frutinha:
    cor = (255, 0, 0)
    posicao = (200, 200)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

frutinha = frutinha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    screen.blit(frutinha.textura, frutinha.posicao)
    pygame.display.update()