import pygame
from paddle import Paddle
from pong_player import PongPlayer
from move_paddle import MovePaddle

class KeyboardArrowPlayer(PongPlayer):
    def calculate_move(self, paddle: Paddle) -> MovePaddle:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return MovePaddle.UP
        if keys[pygame.K_DOWN]:
            return MovePaddle.DOWN
        return MovePaddle.NONE