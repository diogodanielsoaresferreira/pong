import sys
import pygame
import pygame_menu
from pong_game import PongGame
from pong_player import PongPlayer
from keyboard_arrow_player import KeyboardArrowPlayer
from keyboard_ws_and_mouse_player import KeyboardWSAndMousePlayer
from keyboard_arrow_mouse_player import KeyboardArrowAndMousePlayer
from ai_player import AIPlayer

def run_pong(screen, player_1: PongPlayer, player_2: PongPlayer):
    game = PongGame(screen, player_1, player_2)
    font = pygame.font.Font(None, 80)

    player_1_score = 0
    player_2_score = 0

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        game.update()
        player_won = game.is_point_for_player()

        if keys[pygame.K_r]:
            player_1_score = 0
            player_2_score = 0
            game = PongGame(screen, player_1, player_2)

        if player_won == 1:
            player_1_score += 1
            game = PongGame(screen, player_1, player_2)
        elif player_won == 2:
            player_2_score += 1
            game = PongGame(screen, player_1, player_2)

        text = font.render(str(player_1_score) + "-" + str(player_2_score), 1, (255, 255, 255))
        screen.blit(text, (screen.get_width() / 2 - 45, 10))
        game.draw(screen)
        pygame.display.flip()

        clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
menu = pygame_menu.Menu('Pong', 400, 300, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('1-Player', lambda: run_pong(screen, KeyboardArrowAndMousePlayer(), AIPlayer()))
menu.add.button('2-Player', lambda: run_pong(screen, KeyboardWSAndMousePlayer(), KeyboardArrowPlayer()))
menu.mainloop(screen)
