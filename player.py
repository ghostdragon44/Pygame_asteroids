import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED

class Player (CircleShape):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.Surface([1,1])
        self.rect = self.image.get_rect()
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255,255,255), points, 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
       forward = pygame.Vector2(0,1).rotate(self.rotation)
       displacement = forward * PLAYER_SPEED * dt
       self.position += displacement







