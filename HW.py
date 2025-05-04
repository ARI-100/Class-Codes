import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Letter A with Rectangles")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define rectangles to form the letter "A"
# You can adjust these values to change the shape
rects = [
    pygame.Rect(150, 100, 20, 200),  # Left vertical bar
    pygame.Rect(230, 100, 20, 200),  # Right vertical bar
    pygame.Rect(150, 100, 100, 20),  # Top horizontal bar
    pygame.Rect(150, 190, 100, 20),  # Middle horizontal bar
]

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw rectangles
    for rect in rects:
        pygame.draw.rect(screen, BLACK, rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()