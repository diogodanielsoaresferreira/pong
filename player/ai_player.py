from player.pong_player import PongPlayer
from game.move_paddle import MovePaddle
from domain.paddle_position import PaddlePosition
from domain.ball_position import BallPosition

class AIPlayer(PongPlayer):
    def calculate_move(self, paddle_pos: PaddlePosition, ball_pos: BallPosition) -> MovePaddle:
        y_middle_paddle = paddle_pos.top + paddle_pos.height / 2
        if ball_pos.y < y_middle_paddle - paddle_pos.height/4:
            return MovePaddle.UP
        if ball_pos.y > y_middle_paddle + paddle_pos.height/4:
            return MovePaddle.DOWN
        return MovePaddle.NONE
