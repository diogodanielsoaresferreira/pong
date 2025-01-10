import pygame
from game.ball import Ball
from game.paddle import Paddle
from player.pong_player import PongPlayer
from game.move_paddle import MovePaddle

class PongGame:
    def __init__(self, screen_width: int, screen_height: int, player1: PongPlayer, player2: PongPlayer):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = Ball(screen_width, screen_height)
        self.paddle1 = Paddle(screen_width, screen_height, True)
        self.paddle2 = Paddle(screen_width, screen_height, False)
        self.player1 = player1
        self.player2 = player2
    
    def update(self):
        player_1_move = self.player1.calculate_move(self.paddle1, self.ball)
        player_2_move = self.player2.calculate_move(self.paddle2, self.ball)

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
        if self.ball.x > self.screen_width:
            return 1
        return 0
