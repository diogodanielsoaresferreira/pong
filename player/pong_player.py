from game.move_paddle import MovePaddle
from domain.paddle_position import PaddlePosition
from domain.ball_position import BallPosition

class PongPlayer:
    def calculate_move(self, paddle_pos: PaddlePosition, ball_pos: BallPosition) -> MovePaddle:
        return MovePaddle.NONE