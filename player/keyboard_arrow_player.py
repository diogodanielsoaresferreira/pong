import pygame
from game.paddle import Paddle
from player.pong_player import PongPlayer
from game.move_paddle import MovePaddle
from game.ball import Ball

class KeyboardArrowPlayer(PongPlayer):
    def calculate_move(self, paddle: Paddle, ball: Ball) -> MovePaddle:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return MovePaddle.UP
        if keys[pygame.K_DOWN]:
            return MovePaddle.DOWN
        return MovePaddle.NONE