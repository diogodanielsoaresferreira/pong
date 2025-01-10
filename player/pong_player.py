from game.paddle import Paddle
from game.move_paddle import MovePaddle
from game.ball import Ball

class PongPlayer:
    def calculate_move(self, paddel: Paddle, ball: Ball) -> MovePaddle:
        return MovePaddle.NONE