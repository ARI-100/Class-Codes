import pygame
pygame.init()

w = 600
l = 600
display = pygame.display.set_mode((w, l))
pygame.display.set_caption("C10 Snake Game")


snx = 250
sny = 250



pygame.event.get()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    snx += 2
    sny += 2

    display.fill((255, 255, 255))

    pygame.draw.rect(display, (0, 0, 0), (snx, sny, 20,20))

    pygame.display.flip()

    pygame.time.Clock().tick(60)


pygame.quit()