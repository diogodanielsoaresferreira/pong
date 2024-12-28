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

    game.update(keys)
    game.draw(screen)

    if keys[pygame.K_r] or game.is_point_for_player() != 0:
        game = PongGame(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
