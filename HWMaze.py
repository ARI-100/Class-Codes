import pygame, random

def run_maze_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Random Maze Escape")
    clock = pygame.time.Clock()
    FPS = 30

    WHITE = (255, 255, 255)
    RED = (200, 50, 50)
    GOLD = (255, 215, 0)
    BG = (10, 10, 10)

    PLAYER_SIZE = 40
    player = pygame.Rect(50, 50, PLAYER_SIZE, PLAYER_SIZE)
    finish = pygame.Rect(WIDTH - 90, HEIGHT - 90, PLAYER_SIZE, PLAYER_SIZE)

    def generate_walls(count):
        walls = []
        while len(walls) < count:
            w, h = random.randint(60, 120), random.randint(30, 100)
            x, y = random.randint(0, WIDTH - w), random.randint(0, HEIGHT - h)
            rect = pygame.Rect(x, y, w, h)
            if rect.colliderect(player) or rect.colliderect(finish): continue
            if any(rect.colliderect(wall) for wall in walls): continue
            walls.append(rect)
        return walls

    walls = generate_walls(10)
    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 36)
    game_over = False
    running = True

    while running:
        screen.fill(BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        keys = pygame.key.get_pressed()
        if not game_over:
            dx = dy = 0
            if keys[pygame.K_LEFT]: dx = -5
            if keys[pygame.K_RIGHT]: dx = 5
            if keys[pygame.K_UP]: dy = -5
            if keys[pygame.K_DOWN]: dy = 5

            player.x += dx
            if player.left < 0: player.left = 0
            if player.right > WIDTH: player.right = WIDTH
            for wall in walls:
                if player.colliderect(wall):
                    if dx > 0: player.right = wall.left
                    if dx < 0: player.left = wall.right

            player.y += dy
            if player.top < 0: player.top = 0
            if player.bottom > HEIGHT: player.bottom = HEIGHT
            for wall in walls:
                if player.colliderect(wall):
                    if dy > 0: player.bottom = wall.top
                    if dy < 0: player.top = wall.bottom

            if player.colliderect(finish): game_over = True

        for wall in walls: pygame.draw.rect(screen, RED, wall)
        pygame.draw.rect(screen, GOLD, finish)
        pygame.draw.rect(screen, WHITE, player)

        if game_over:
            screen.blit(font.render("You Escaped!", True, GOLD), (280, 250))
            screen.blit(small_font.render("Press R to restart", True, WHITE), (290, 310))
            if keys[pygame.K_r]:
                player.topleft = (50, 50)
                walls = generate_walls(10)
                game_over = False

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    run_maze_game()
