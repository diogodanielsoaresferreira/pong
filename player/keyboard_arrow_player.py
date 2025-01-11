import pygame
from player.pong_player import PongPlayer
from game.move_paddle import MovePaddle
from domain.paddle_position import PaddlePosition
from domain.ball_position import BallPosition

class KeyboardArrowPlayer(PongPlayer):
    def calculate_move(self, paddle_pos: PaddlePosition, ball_pos: BallPosition) -> MovePaddle:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return MovePaddle.UP
        if keys[pygame.K_DOWN]:
            return MovePaddle.DOWN
        return MovePaddle.NONE