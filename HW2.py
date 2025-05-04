import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
GOLD = (212, 175, 55)
PLAYER_COLOR = (0, 0, 255)
RECT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 0), (255, 165, 0)]

# Load sound
magic_sound_path = "magic.wav"
magic_sound = pygame.mixer.Sound(magic_sound_path)

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("King Midas Touch")

# Midas player setup
player_size = 50
player = pygame.Rect(WIDTH//2 - player_size//2, HEIGHT//2 - player_size//2, player_size, player_size)
player_speed = 5

# Static rectangles (objects to touch)
rects = [
    pygame.Rect(50, 50, 50, 50),
    pygame.Rect(WIDTH - 100, 50, 50, 50),
    pygame.Rect(50, HEIGHT - 100, 50, 50),
    pygame.Rect(WIDTH - 100, HEIGHT - 100, 50, 50),
]
touched = [False, False, False, False]  # To remember which were turned to gold

# Game loop
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)  # 60 FPS
    win.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Collision detection and updating colors
    for i, rect in enumerate(rects):
        if player.colliderect(rect) and not touched[i]:
            touched[i] = True
            magic_sound.play()

    # Draw objects
    pygame.draw.rect(win, PLAYER_COLOR, player)

    for i, rect in enumerate(rects):
        color = GOLD if touched[i] else RECT_COLORS[i]
        pygame.draw.rect(win, color, rect)

    pygame.display.update()

pygame.quit()