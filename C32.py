import pygame, random
pygame.init()

WINSIZE = 600
SNAKESIZE = 20
APPLESIZE = 20

head_x = WINSIZE // 2
head_y = WINSIZE // 2
snake_dx = 0
snake_dy = 0

score = 0

FPS = 30
clock = pygame.time.Clock()

font = pygame.font.SysFont('gabriola', 48)
score_text = font.render("Score: " + str(score), True, "green", "darkred")
score_rect = score_text.get_rect()
score_rect.topleft = (50, 50)

game_over_text = font.render("GAMEOVER", True, "white", "black")
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINSIZE//2, WINSIZE//2)
display = pygame.display.set_mode((WINSIZE, WINSIZE))
pygame.display.set_caption("Snake but rainbow")
pick_up_sound = pygame.mixer.Sound("eating.wav")

colors = [
    (255, 0 ,0),
    (255, 127, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 0, 255)
]

apple_coord = (500, 500, APPLESIZE, APPLESIZE)
apple_rect = pygame.draw.rect(display, "red", apple_coord)

head_coord = (head_x, head_y, SNAKESIZE, SNAKESIZE)
head_rect = pygame.draw.rect(display, "black", head_coord)
body_coords = []

running = True
gameover = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -0.5 * SNAKESIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = 0.5 * SNAKESIZE
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -0.5 * SNAKESIZE
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = 0.5 * SNAKESIZE

    body_coords.insert(0, head_coord)
    body_coords.pop()

    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKESIZE, SNAKESIZE)
    if head_rect.left < 0 or head_rect.right > WINSIZE or head_rect.top < 0 or head_rect.bottom > WINSIZE or head_coord in body_coords:
        display.blit(game_over_text, game_over_rect)
        gameover = True
        pygame.display.update()

    if gameover:
        display.fill("black")
        display.blit(game_over_text, game_over_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
        apple_x = random.randint(0, WINSIZE - SNAKESIZE)
        apple_y = random.randint(0, WINSIZE - SNAKESIZE)
        apple_coord = (apple_x, apple_y, SNAKESIZE, SNAKESIZE)

        body_coords.append(head_coord)

    score_text = font.render("Score: " + str(score), True, "green")
    display.fill((0, 200, 0))

    display.blit(score_text, score_rect)
    for body in body_coords:
        pygame.draw.rect(display, colors[random.randint(0, 5)], body)

    head_rect = pygame.draw.rect(display, "black", head_coord)
    apple_rect = pygame.draw.rect(display, "red", apple_coord)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
