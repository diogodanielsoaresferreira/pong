import pygame
from paddle import Paddle
from pong_player import PongPlayer
from move_paddle import MovePaddle
from ball import Ball

class KeyboardWSAndMousePlayer(PongPlayer):
    def __init__(self):
        super().__init__()
        self.use_mouse = False

    def calculate_move(self, paddle: Paddle, ball: Ball) -> MovePaddle:
        (_, y_rel) = pygame.mouse.get_rel()
        (_, y_pos) = pygame.mouse.get_pos()
        y_middle_paddle = paddle.get_middle_point()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.use_mouse = False
            return MovePaddle.UP
        if keys[pygame.K_s]:
            self.use_mouse = False
            return MovePaddle.DOWN
        
        if y_rel != 0:
            self.use_mouse = True

        if self.use_mouse and y_pos < y_middle_paddle - paddle.height/20:
            self.use_mouse = True
            return MovePaddle.UP
        elif self.use_mouse and y_pos > y_middle_paddle + paddle.height/20:
            self.use_mouse = True
            return MovePaddle.DOWN
        
        return MovePaddle.NONE
