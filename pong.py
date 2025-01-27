import sys
import asyncio
import pygame
import pygame_menu
import pyperclip

from game.pong_game import PongGame
from player.pong_player import PongPlayer
from player.keyboard_arrow_player import KeyboardArrowPlayer
from player.keyboard_ws_and_mouse_player import KeyboardWSAndMousePlayer
from player.keyboard_arrow_mouse_player import KeyboardArrowAndMousePlayer
from player.ai_player import AIPlayer
from network.game_events import create_online_game, join_online_game
from ui.screen import Screen

SERVER_URI = "ws://localhost:8001"

def run_pong(screen: pygame.surface, player_1: PongPlayer, player_2: PongPlayer):
    game_screen = Screen(screen)
    game = PongGame(screen.get_width(), screen.get_height())
    clock = pygame.time.Clock()

    player_1_score = 0
    player_2_score = 0

    paddle_1_position = game.paddle1.get_position()
    paddle_2_position = game.paddle2.get_position()
    ball_position = game.ball.get_position()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        player_1_move = player_1.calculate_move(paddle_1_position, ball_position)
        player_2_move = player_2.calculate_move(paddle_2_position, ball_position)
        
        paddle_1_position, paddle_2_position, ball_position, player_won = game.update(player_1_move, player_2_move)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            player_1_score = 0
            player_2_score = 0
            game = PongGame(screen.get_width(), screen.get_height())

        if player_won == 1:
            player_1_score += 1
            game = PongGame(screen.get_width(), screen.get_height())
        elif player_won == 2:
            player_2_score += 1
            game = PongGame(screen.get_width(), screen.get_height())

        game_screen.draw(paddle_1_position, paddle_2_position, ball_position, player_1_score, player_2_score)
        clock.tick(60)



pygame.init()
screen = pygame.display.set_mode((1280, 720))

game_name = ''

sub_menu_game_name = pygame_menu.Menu('Game name', 400, 300, theme=pygame_menu.themes.THEME_DARK)
text_input_join = sub_menu_game_name.add.text_input('', default='', onchange=lambda value: globals().update(game_name=value))

def set_game_name(name):
    global game_name
    game_name = name
    text_input_join.set_value(game_name)

sub_menu_game_name.add.button('Paste', lambda: set_game_name(pyperclip.paste()))
sub_menu_game_name.add.button('Join', lambda: asyncio.run(join_online_game(screen, SERVER_URI, game_name)))

sub_menu_new_game = pygame_menu.Menu('New game', 400, 300, theme=pygame_menu.themes.THEME_DARK)
text_input = sub_menu_new_game.add.text_input('', default='', onchange=lambda value: globals().update(game_name=value))
sub_menu_new_game.add.button('Create room', lambda: asyncio.run(create_online_game(screen, SERVER_URI, game_name)))

sub_menu_online = pygame_menu.Menu('Online Mode', 400, 300, theme=pygame_menu.themes.THEME_DARK)
sub_menu_online.add.button('Create game', sub_menu_new_game)
sub_menu_online.add.button('Join game', sub_menu_game_name)

sub_menu_2_players = pygame_menu.Menu('2-Player Mode', 400, 300, theme=pygame_menu.themes.THEME_DARK)
sub_menu_2_players.add.button('Local', lambda: run_pong(screen, KeyboardWSAndMousePlayer(), KeyboardArrowPlayer()))
sub_menu_2_players.add.button('Online', sub_menu_online)

menu = pygame_menu.Menu('Pong', 400, 300, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('1-Player', lambda: run_pong(screen, KeyboardArrowAndMousePlayer(), AIPlayer()))
menu.add.button('2-Player', sub_menu_2_players)
menu.mainloop(screen)
