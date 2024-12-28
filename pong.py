import pygame
from pong_game import PongGame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

game = PongGame(screen)

while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        game = PongGame(screen)

    game.update(keys)
    game.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
