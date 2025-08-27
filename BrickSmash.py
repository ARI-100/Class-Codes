import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaker")
clock = pygame.time.Clock()

# --- Game Classes --- #

class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 15
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - 40
        self.speed = 8
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)

class Ball:
    def __init__(self):
        self.radius = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.dx = random.choice([-4, 4])
        self.dy = -4
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.dx *= -1
        if self.rect.top <= 0:
            self.dy *= -1

    def draw(self, surface):
        pygame.draw.ellipse(surface, RED, self.rect)

    def bounce(self):
        self.dy *= -1

class Brick:
    def __init__(self, x, y):
        self.width = 60
        self.height = 20
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.destroyed = False

    def draw(self, surface):
        if not self.destroyed:
            pygame.draw.rect(surface, WHITE, self.rect)
            pygame.draw.rect(surface, BLACK, self.rect, 2)

paddle = Paddle()
ball = Ball()

bricks = []
for row in range(5):
    for col in range(10):
        brick_x = col * 70 + 35
        brick_y = row * 30 + 50
        bricks.append(Brick(brick_x, brick_y))

running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move & Draw
    keys = pygame.key.get_pressed()
    paddle.move(keys)
    ball.move()

    # Collision with paddle
    if ball.rect.colliderect(paddle.rect):
        ball.bounce()

    # Collision with bricks
    for brick in bricks:
        if not brick.destroyed and ball.rect.colliderect(brick.rect):
            brick.destroyed = True
            ball.bounce()
            break

    # Game Over (Ball Falls off Screen)
    if ball.rect.top > SCREEN_HEIGHT:
        print("Game Over")
        running = False

    #Draw Everything
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    pygame.display.flip()

pygame.quit()