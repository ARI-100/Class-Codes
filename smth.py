import pygame
pygame.init()
W = 600
SNSIZE = 20
APSIZE = 20
display = pygame.display.set_mode((W, W))
pygame.display.set_caption("Snake Game")
head_x = W/2
head_y = W/2
snake_dx = 0
snake_dy = 0
hc = (head_x, head_y, SNSIZE, SNSIZE)
head_rect = pygame.draw.rect(display, (0, 255, 0), hc)
ac = (500, 500, APSIZE, APSIZE)
apple_rect = pygame.draw.rect(display, (255, 0, 0), ac)
pygame.event.get()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1*SNSIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNSIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1*SNSIZE
            if event.key == pygame.K_DOWN:
                snake_dx = SNSIZE
                snake_dy = 0
    
    head_x += snake_dx
    head_y += head_y
    hc = (head_x, head_y, SNSIZE, SNSIZE)

    #if head_rect.colliderect(apple_rect):
        #pick_up_sound.play()

    display.fill((34, 114, 198))

    head_rect = pygame.draw.rect(display, (0, 200, 0), hc)
    apple_rect = pygame.draw.rect(display, (200, 0, 0), ac) 

    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()