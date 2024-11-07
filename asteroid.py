import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.Surface([1,1])
        self.rect = self.image.get_rect()
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

