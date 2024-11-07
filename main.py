import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    for sprite in updatable:
        sprite.update()
    for sprite in drawable:
        sprite.draw(screen)
    
    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
    
    

if __name__ == "__main__":
    main()



print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)


