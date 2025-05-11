import pygame

pygame.init()

WindowSize = 600
MOVEMENTSIZE = 20
display = pygame.display.set_mode((WindowSize, WindowSize))
pygame.display.set_caption("Tron Light Cycle")
clock = pygame.time.Clock()
FPS = 10

x = WindowSize // 2
y = WindowSize // 2
dx = MOVEMENTSIZE
dy = 0
trail = [(x, y)]
score = 0
game_over = False

BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
TRAILCOLOR = (0, 150, 255)
WHITE = (255, 255, 255)
font = pygame.font.SysFont('gabriola', 35)
Othersizefont = pygame.font.SysFont('gabriola', 70)

def draw_text(where, text, font, color, x, y):
    img = font.render(text, True, color)
    rect = img.get_rect(center = (x, y))
    where.blit(img, rect)

for i in range(10, 0, -1):
    display.fill(WHITE)
    draw_text(display, str(i), Othersizefont, BLACK, WindowSize // 2, WindowSize // 2)
    pygame.display.update()
    pygame.time.delay(1000)

display.fill(WHITE)
draw_text(display, "GO!", Othersizefont, BLACK, WindowSize // 2, WindowSize // 2)
pygame.display.update()
pygame.time.delay(1000)

running = True
while running:
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dy == 0:
            dx, dy = 0, -MOVEMENTSIZE
        elif keys[pygame.K_DOWN] and dy == 0:
            dx, dy = 0, MOVEMENTSIZE
        elif keys[pygame.K_LEFT] and dx == 0:
            dx, dy = -MOVEMENTSIZE, 0
        elif keys[pygame.K_RIGHT] and dx == 0:
            dx, dy = MOVEMENTSIZE, 0
        
        x += dx
        y += dy
        new_pos = (x, y)
        trail.append(new_pos)

        if new_pos in trail[:-1] or x < 0 or y < 0 or x >= WindowSize or y >= WindowSize:
            game_over = True

        score = len(trail)

        display.fill(WHITE)
        for pos in trail:
            pygame.draw.rect(display, TRAILCOLOR, (*pos, MOVEMENTSIZE, MOVEMENTSIZE))
        pygame.draw.rect(display, CYAN, (x, y, MOVEMENTSIZE, MOVEMENTSIZE))
        draw_text(display, f"Score: {score}", font, BLACK, WindowSize // 2, 30)

        pygame.display.update()
        clock.tick(FPS)

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_text(display, "GAME OVER", Othersizefont, BLACK, WindowSize // 2, WindowSize // 2)
        draw_text(display, f"Final Score: {score}", font, BLACK, WindowSize // 2, WindowSize // 2 + 50)
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

pygame.quit()