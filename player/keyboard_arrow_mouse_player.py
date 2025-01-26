import pygame
from player.pong_player import PongPlayer
from game.move_paddle import MovePaddle
from domain.paddle_position import PaddlePosition
from domain.ball_position import BallPosition

class KeyboardArrowAndMousePlayer(PongPlayer):
    def __init__(self):
        super().__init__()
        self.use_mouse = False

    def calculate_move(self, paddle_pos: PaddlePosition, ball_pos: BallPosition) -> MovePaddle:
        pygame.event.pump()
        (_, y_rel) = pygame.mouse.get_rel()
        (_, y_pos) = pygame.mouse.get_pos()
        y_middle_paddle = paddle_pos.top + paddle_pos.height / 2

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.use_mouse = False
            return MovePaddle.UP
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.use_mouse = False
            return MovePaddle.DOWN
        
        if y_rel != 0:
            self.use_mouse = True

        if self.use_mouse and y_pos < y_middle_paddle - paddle_pos.height/20:
            self.use_mouse = True
            return MovePaddle.UP
        elif self.use_mouse and y_pos > y_middle_paddle + paddle_pos.height/20:
            self.use_mouse = True
            return MovePaddle.DOWN
        
        return MovePaddle.NONE
