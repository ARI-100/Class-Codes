import pygame
import pymunk
import pymunk.pygame_util

def create_ball(space):
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 20))
    body.position = (400, 50)
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0.8  # Bounciness
    space.add(body, shape)
    return body,shape


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 981)
draw_options = pymunk.pygame_util.DrawOptions(screen)

ball = create_ball(space)  # Add bouncing ball

running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    space.step(1/60)
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

