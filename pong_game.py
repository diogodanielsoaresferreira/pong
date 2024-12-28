import pygame
from ball import Ball
from paddle import Paddle
from pong_player import PongPlayer
from move_paddle import MovePaddle

class PongGame:
    def __init__(self, screen: pygame.surface, player1: PongPlayer, player2: PongPlayer):
        self.screen = screen
        self.ball = Ball(screen)
        self.paddle1 = Paddle(screen, True)
        self.paddle2 = Paddle(screen, False)
        self.player1 = player1
        self.player2 = player2
    
    def update(self):

        player_1_move = self.player1.calculate_move(self.paddle1)
        player_2_move = self.player2.calculate_move(self.paddle1)

        if (player_1_move == MovePaddle.UP):
            self.paddle1.move_up()
        if (player_1_move == MovePaddle.DOWN):
            self.paddle1.move_down()
        if (player_2_move == MovePaddle.UP):
            self.paddle2.move_up()
        if (player_2_move == MovePaddle.DOWN):
            self.paddle2.move_down()

        self.ball.update(self.paddle1, self.paddle2)

    def is_point_for_player(self):
        if self.ball.x < 0:
            return 2
        if self.ball.x > self.screen.get_width():
            return 1
        return 0

    def draw(self, screen: pygame.surface):
        self.ball.draw(screen)
        self.paddle1.draw(screen)
        self.paddle2.draw(screen)
