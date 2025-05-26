import pygame

pygame.init()

WIDTH, HEIGHT = 800,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xylophone")

colors = [
    (255, 0, 0),    # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (139, 0, 255),  # Purple
    (255, 0, 255)   # Magenta
]

sound_files = [
    'note1.mp3',
    'note2.mp3',
    'note3.mp3',
    'noteA.mp3',
    'noteB.mp3',
    'noteC.mp3',
    'noteD.mp3',
    'noteE.mp3'
]

sounds = [pygame.mixer.Sound(name) for name in sound_files]

bar_count = len(colors)
bar_width = WIDTH // bar_count
max_bar_height = 360
min_bar_height = 120

bars = []
for i in range(bar_count):
    height = max_bar_height - i * ((max_bar_height - min_bar_height) // (bar_count - 1))
    x = i * bar_width
    y = 20
    rect = pygame.Rect(x + 5, y, bar_width - 10, height)
    bars.append(rect)

running = True
while running:
    screen.fill((30, 30, 30))

    for i, rect in enumerate(bars):
        pygame.draw.rect(screen, colors[i], rect, border_radius = 8)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(bars):
                if rect.collidepoint(event.pos):
                    sounds[i].play()

pygame.quit()