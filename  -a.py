import pygame, random
pygame.init()

# Screen setup
W, H = 400, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# Player setup
player = pygame.Rect(W//2 - 20, H - 40, 40, 40)
speed = 5

# Enemy setup
enemies = []
spawn_timer = 0

running = True
while running:
    screen.fill((30, 30, 30))
    
    # Events
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0: player.x -= speed
    if keys[pygame.K_RIGHT] and player.right < W: player.x += speed

    # Spawn enemies
    spawn_timer += 1
    if spawn_timer > 30:
        enemies.append(pygame.Rect(random.randint(0, W-30), -30, 30, 30))
        spawn_timer = 0

    # Move enemies
    for e in enemies:
        e.y += 5
        pygame.draw.rect(screen, (200, 0, 0), e)
        if e.colliderect(player): running = False

    # Remove off-screen enemies
    enemies = [e for e in enemies if e.y < H]

    # Draw player
    pygame.draw.rect(screen, (0, 200, 0), player)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()