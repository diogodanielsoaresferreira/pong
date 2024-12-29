from pong_player import PongPlayer
from move_paddle import MovePaddle
from paddle import Paddle
from ball import Ball

class AIPlayer(PongPlayer):
    def calculate_move(self, paddle: Paddle, ball: Ball) -> MovePaddle:
        if ball.y < paddle.get_middle_point() - paddle.height/4:
            return MovePaddle.UP
        if ball.y > paddle.get_middle_point() + paddle.height/4:
            return MovePaddle.DOWN
        return MovePaddle.NONE
