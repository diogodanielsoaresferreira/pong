import random
import pygame
import math
from paddle import Paddle

class Ball:

    def __init__(this, screen: pygame.surface):
        this.screen = screen
        this.max_angle = 75
        this.x = screen.get_width() / 2
        this.y = screen.get_height() / 2
        this.ball_velocity_module = 10
        this.dx = random.randint(1, this.ball_velocity_module/2)
        this.dy = math.sqrt(this.ball_velocity_module ** 2 - this.dx ** 2)

    def is_paddle_colliding(this, paddle: Paddle):
        return paddle.paddle_pos.collidepoint(this.x, this.y)
    
    def update(this, paddle1: Paddle, paddle2: Paddle):
        this.x += this.dx
        this.y += this.dy
        if this.y < 0 or this.y > this.screen.get_height():
            this.dy = -this.dy
        if this.is_paddle_colliding(paddle1):
            this.calculate_paddle_hit(paddle1)
        if this.is_paddle_colliding(paddle2):
            this.calculate_paddle_hit(paddle2)
            this.dx = -this.dx

    def draw(this, screen: pygame.surface):
        pygame.draw.circle(screen, "white", pygame.Vector2(this.x, this.y), 20)

    def calculate_paddle_hit(this, paddle: Paddle):
        paddle_middle_point = paddle.offset - paddle.height / 2
        relative_position = 2 * (((this.y - paddle_middle_point) / (paddle.height)) - 1)
        relative_angle = relative_position * this.max_angle
        this.dx = this.ball_velocity_module * math.cos(math.radians(relative_angle))
        this.dy = this.ball_velocity_module * math.sin(math.radians(relative_angle))
