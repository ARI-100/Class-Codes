import pygame
pygame.init()

screen = pygame.display.set_mode((500, 400))
turquoise = (64, 224, 208)
screen.fill()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()