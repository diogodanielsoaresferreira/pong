import random
import math
from game.paddle import Paddle

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

    def is_paddle_colliding(self, paddle: Paddle):
        return paddle.paddle_pos.collidepoint(self.x, self.y)
    
    def update(self, paddle1: Paddle, paddle2: Paddle):
        self.x += self.dx
        self.y += self.dy
        if self.y < 0 or self.y > self.screen_height:
            self.dy = -self.dy
        if self.is_paddle_colliding(paddle1):
            self._calculate_paddle_hit(paddle1)
        if self.is_paddle_colliding(paddle2):
            self._calculate_paddle_hit(paddle2)
            self.dx = -self.dx

    def _calculate_paddle_hit(self, paddle: Paddle):
        paddle_middle_point = paddle.get_middle_point()
        relative_position = ((self.y - paddle_middle_point) / (paddle.height / 2))
        relative_angle = relative_position * self.max_angle
        self.ball_velocity_module += self.dv
        self.dx = self.ball_velocity_module * math.cos(math.radians(relative_angle))
        self.dy = self.ball_velocity_module * math.sin(math.radians(relative_angle))
