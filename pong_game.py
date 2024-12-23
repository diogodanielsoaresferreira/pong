import pygame
from ball import Ball
from paddle import Paddle

class PongGame:
    def __init__(self, screen: pygame.surface):
        self.ball = Ball(screen)
        self.paddle1 = Paddle(screen, True)
        self.paddle2 = Paddle(screen, False)

    def draw(self, screen: pygame.surface):
        self.ball.draw(screen)
        self.paddle1.draw(screen)
        self.paddle2.draw(screen)
