import random
import pygame
import math
from paddle import Paddle

class Ball:

    def __init__(this, screen: pygame.surface):
        this.screen = screen
        this.x = screen.get_width() / 2
        this.y = screen.get_height() / 2
        this.ball_velocity_module = 10
        this.dx = random.randint(-this.ball_velocity_module, this.ball_velocity_module)
        this.dy = math.sqrt(this.ball_velocity_module ** 2 - this.dx ** 2)

    def is_paddle_colliding(this, paddle: Paddle):
        return paddle.paddle_pos.collidepoint(this.x, this.y)
    
    def update(this, paddle1: Paddle, paddle2: Paddle):
        this.x += this.dx
        this.y += this.dy
        if this.y < 0 or this.y > this.screen.get_height():
            this.dy = -this.dy
        if this.is_paddle_colliding(paddle1) or this.is_paddle_colliding(paddle2):
            this.dx = -this.dx
    

    def draw(this, screen: pygame.surface):
        pygame.draw.circle(screen, "white", pygame.Vector2(this.x, this.y), 20)
