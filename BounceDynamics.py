import pygame
import pymunk
import pymunk.pygame_util

def create_ball(space, position, elasticity):
  #write the code to create ball object
  body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 20))
  body.position = position
  shape = pymunk.Circle(body, 20)
  shape.elasticity = elasticity
  space.add(body, shape)
  return shape

def create_floor(space):
    """Creates a static floor for the balls to bounce on."""
    floor = pymunk.Segment(space.static_body, (50, 500), (750, 500), 5)
    floor.elasticity = 1.0  # Maximum bounce
    space.add(floor)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Elasticity Demo")
    clock = pygame.time.Clock()

    #create pymunk space
    space = pymunk.Space()
    


    #gravity to pull downward
    space.gravity = (0, 981)

    draw_options = pymunk.pygame_util.DrawOptions(screen)
    

    #Update physics simulation
    
    
    # Create a floor
    create_floor(space)

    # Create balls with different elasticity
    ball1 = create_ball(space, (200, 100), 0.2)
    ball2 = create_ball(space, (400, 100), 0.6)
    ball3 = create_ball(space, (600, 100), 1)

    running = True
    while running:
        screen.fill((0, 0, 0))  # Black background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update physics simulation
        space.step(1/60)
        
        # Draw objects
        space.debug_draw(draw_options)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()