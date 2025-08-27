import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
NAVY_BLUE = (0, 0, 128)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Vs Computer")
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, x):
        self.width = 15
        self.height = 100
        self.x = x
        self.y = SCREEN_HEIGHT // 2 - self.height // 2
        self.speed = 6
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, up, down):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        if down and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
        
    def auto_move(self, target_y):
        if self.rect.centery < target_y and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
        elif self.rect.centery > target_y and self.rect.top > 0:
            self.rect.y -= self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.size = 15
        self.rect = pygame.Rect(
            SCREEN_WIDTH // 2 - self.size // 2,
            SCREEN_HEIGHT // 2 - self.size // 2,
            self.size,
            self.size
        )
        self.dx = -5
        self.dy = 5
        self.active = False

    def move(self):
        if not self.active:
            return
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy *= -1

    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)

    def reset(self):
        self.rect.x = SCREEN_WIDTH // 2 - self.size // 2
        self.rect.y = SCREEN_HEIGHT // 2 - self.size // 2
        self.active = False

player = Paddle(x = 50)
computer = Paddle(x = SCREEN_WIDTH - 65)
ball = Ball()

running = True
while running:
    clock.tick(FPS)
    screen.fill(NAVY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys[pygame.K_UP], keys[pygame.K_DOWN])
    computer.auto_move(ball.rect.centery)
    ball.move()

    if ball.rect.colliderect(player.rect) or ball.rect.colliderect(computer.rect):
        ball.dx *= -1

    if ball.rect.left <= 0 or ball.rect.right >= SCREEN_WIDTH:
        ball.reset()

    player.draw(screen)
    computer.draw(screen)
    ball.draw(screen)

    if keys[pygame.K_SPACE]:
        ball.active = True
    
    pygame.display.flip()

pygame.quit()