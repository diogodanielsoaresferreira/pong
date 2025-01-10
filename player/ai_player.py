from player.pong_player import PongPlayer
from game.move_paddle import MovePaddle
from game.paddle import Paddle
from game.ball import Ball

class AIPlayer(PongPlayer):
    def calculate_move(self, paddle: Paddle, ball: Ball) -> MovePaddle:
        if ball.y < paddle.get_middle_point() - paddle.height/4:
            return MovePaddle.UP
        if ball.y > paddle.get_middle_point() + paddle.height/4:
            return MovePaddle.DOWN
        return MovePaddle.NONE
