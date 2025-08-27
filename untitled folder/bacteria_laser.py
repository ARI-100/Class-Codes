import pygame
WINDOW_HEIGHT = 900
class BacteriaLaser(pygame.sprite.Sprite):

    def __init__(self, x, y, laser_group):
        super().__init__()
        self.image = pygame.image.load("red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        laser_group.add(self)

    def update(self):
        self.rect.y += self.velocity

        if self.rect.top > WINDOW_HEIGHT:
            self.kill()