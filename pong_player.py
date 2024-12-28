from paddle import Paddle
from move_paddle import MovePaddle
from ball import Ball

class PongPlayer:
    def calculate_move(self, paddel: Paddle, ball: Ball) -> MovePaddle:
        return MovePaddle.NONE