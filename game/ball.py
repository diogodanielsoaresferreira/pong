import random
import math
from domain.paddle_position import PaddlePosition
from domain.ball_position import BallPosition

class Ball:

    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.max_angle = 60
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.ball_velocity_module = 10
        self.dx = random.randint(self.ball_velocity_module/2, self.ball_velocity_module)
        self.dy = math.sqrt(self.ball_velocity_module ** 2 - self.dx ** 2)
        self.dv = 0.1
    
    def get_position(self) -> BallPosition:
        return BallPosition(self.x, self.y)

    def is_paddle_colliding(self, paddle_pos: PaddlePosition) -> bool:
        if paddle_pos.top < self.y < paddle_pos.top + paddle_pos.height:
            if paddle_pos.x < self.x < paddle_pos.x + paddle_pos.width:
                return True
        return False

    def update(self, paddle_1_pos: PaddlePosition, paddle_2_pos: PaddlePosition) -> BallPosition:
        self.x += self.dx
        self.y += self.dy
        if self.y < 0 or self.y > self.screen_height:
            self.dy = -self.dy
        if self.is_paddle_colliding(paddle_1_pos):
            self._calculate_paddle_hit(paddle_1_pos)
        if self.is_paddle_colliding(paddle_2_pos):
            self._calculate_paddle_hit(paddle_2_pos)
            self.dx = -self.dx
        return self.get_position()

    def _calculate_paddle_hit(self, paddle_pos: PaddlePosition):
        paddle_middle_point = paddle_pos.top + paddle_pos.height / 2
        relative_position = ((self.y - paddle_middle_point) / (paddle_pos.height / 2))
        relative_angle = relative_position * self.max_angle
        self.ball_velocity_module += self.dv
        self.dx = self.ball_velocity_module * math.cos(math.radians(relative_angle))
        self.dy = self.ball_velocity_module * math.sin(math.radians(relative_angle))
