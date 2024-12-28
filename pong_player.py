from paddle import Paddle
from move_paddle import MovePaddle

class PongPlayer:
    def calculate_move(self, paddel: Paddle) -> MovePaddle:
        return MovePaddle.NONE