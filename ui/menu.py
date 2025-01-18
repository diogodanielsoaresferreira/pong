import time
import pygame
import pyperclip
import pygame_menu
import threading

def animate_copy_button(name: str, button: pygame_menu.widgets.Button):
    pyperclip.copy(name)
    button.set_title("Copied!")
    threading.Thread(target=lambda: (time.sleep(1), button.set_title("Copy"))).start()


def createMenuWithGameName(screen: pygame.surface, name: str):
    game_created_menu = pygame_menu.Menu('Game Created', 400, 300, theme=pygame_menu.themes.THEME_DARK)
    game_created_menu.add.label(f"{name}")
    button = game_created_menu.add.button(
        'Copy',
        lambda: animate_copy_button(name, button)
    )
    game_created_menu.mainloop(screen)
