from typing import List, Union
from game.ball import Ball
from game.paddle import Paddle
from domain.ball_position import BallPosition
from domain.paddle_position import PaddlePosition
from game.move_paddle import MovePaddle

class PongGame:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = Ball(screen_width, screen_height)
        self.paddle1 = Paddle(screen_width, screen_height, True)
        self.paddle2 = Paddle(screen_width, screen_height, False)

    def update(self, player_1_move: MovePaddle, player_2_move: MovePaddle) -> List[Union[PaddlePosition, PaddlePosition, BallPosition, int]]:
        if (player_1_move == MovePaddle.UP):
            self.paddle1.move_up()
        if (player_1_move == MovePaddle.DOWN):
            self.paddle1.move_down()
        if (player_2_move == MovePaddle.UP):
            self.paddle2.move_up()
        if (player_2_move == MovePaddle.DOWN):
            self.paddle2.move_down()

        paddle_1_position = self.paddle1.get_position()
        paddle_2_position = self.paddle2.get_position()

        ball_position = self.ball.update(paddle_1_position, paddle_2_position)
        return [paddle_1_position, paddle_2_position, ball_position, self.is_point_for_player(ball_position)]

    def is_point_for_player(self, ball_position: BallPosition):
        if ball_position.x < 0:
            return 2
        if ball_position.x > self.screen_width:
            return 1
        return 0
