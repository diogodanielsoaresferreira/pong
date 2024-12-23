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

    game.update()
    game.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
