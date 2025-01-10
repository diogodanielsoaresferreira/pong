import sys
import asyncio
import pygame
import pygame_menu

from game.pong_game import PongGame
from player.pong_player import PongPlayer
from player.keyboard_arrow_player import KeyboardArrowPlayer
from player.keyboard_ws_and_mouse_player import KeyboardWSAndMousePlayer
from player.keyboard_arrow_mouse_player import KeyboardArrowAndMousePlayer
from player.ai_player import AIPlayer
from network.game_events import create_online_game, join_online_game

SERVER_URI = "ws://localhost:8001"

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

game_name = ''
sub_menu_game_name = pygame_menu.Menu('Game name', 400, 300, theme=pygame_menu.themes.THEME_DARK)
sub_menu_game_name.add.text_input('', default='', onchange=lambda value: globals().update(game_name=value))
sub_menu_game_name.add.button('Join', lambda: asyncio.run(join_online_game(SERVER_URI, game_name)))

sub_menu_online = pygame_menu.Menu('Online Mode', 400, 300, theme=pygame_menu.themes.THEME_DARK)
sub_menu_online.add.button('Create game', lambda: asyncio.run(create_online_game(SERVER_URI)))
sub_menu_online.add.button('Join game', sub_menu_game_name)

sub_menu_2_players = pygame_menu.Menu('2-Player Mode', 400, 300, theme=pygame_menu.themes.THEME_DARK)
sub_menu_2_players.add.button('Local', lambda: run_pong(screen, KeyboardWSAndMousePlayer(), KeyboardArrowPlayer()))
sub_menu_2_players.add.button('Online', sub_menu_online)

menu = pygame_menu.Menu('Pong', 400, 300, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('1-Player', lambda: run_pong(screen, KeyboardArrowAndMousePlayer(), AIPlayer()))
menu.add.button('2-Player', sub_menu_2_players)
menu.mainloop(screen)
