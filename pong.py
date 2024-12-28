import pygame
from pong_game import PongGame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

game = PongGame(screen)
font = pygame.font.Font(None, 80)

player_1 = 0
player_2 = 0

while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    game.update(keys)
    player_won = game.is_point_for_player()

    if keys[pygame.K_r]:
        player_1 = 0
        player_2 = 0
        game = PongGame(screen)

    if player_won == 1:
        player_1 += 1
        game = PongGame(screen)
    elif player_won == 2:
        player_2 += 1
        game = PongGame(screen)

    text = font.render(str(player_1) + "-" + str(player_2), 1, (255, 255, 255))
    screen.blit(text, (screen.get_width() / 2 - 45, 10))
    game.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
