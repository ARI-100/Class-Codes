import pygame

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
NAVY_BLUE = (0, 0, 128)

# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong 1v1")
clock = pygame.time.Clock()

# Paddle class
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

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# Ball class
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

        # Bounce off top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy *= -1

    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)

    def reset(self):
        self.rect.x = SCREEN_WIDTH // 2 - self.size // 2
        self.rect.y = SCREEN_HEIGHT // 2 - self.size // 2
        self.active = False
        self.dx *= -1  # send to opposite player

# Game objects
player1 = Paddle(x=50)
player2 = Paddle(x=SCREEN_WIDTH - 65)
ball = Ball()

# Score
score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 50)

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(NAVY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    player1.move(keys[pygame.K_w], keys[pygame.K_s])
    player2.move(keys[pygame.K_UP], keys[pygame.K_DOWN])

    # Start ball movement
    if keys[pygame.K_SPACE]:
        ball.active = True

    ball.move()

    # Collision with paddles
    if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
        ball.dx *= -1

    # Scoring
    if ball.rect.left <= 0:
        score2 += 1
        ball.reset()
    elif ball.rect.right >= SCREEN_WIDTH:
        score1 += 1
        ball.reset()

    # Draw game objects
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)

    # Draw score
    score_text = font.render(f"{score1}    -    {score2}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()

pygame.quit()