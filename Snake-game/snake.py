import pygame

pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)

verde = (46, 139, 87)
screen.fill(verde)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()