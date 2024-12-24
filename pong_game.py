import pygame
from ball import Ball
from paddle import Paddle

class PongGame:
    def __init__(self, screen: pygame.surface):
        self.ball = Ball(screen)
        self.paddle1 = Paddle(screen, True)
        self.paddle2 = Paddle(screen, False)
    
    def update(self, keys: list[bool]):
        if keys[pygame.K_w]:
            self.paddle1.move_up()
        if keys[pygame.K_s]:
            self.paddle1.move_down()
        if keys[pygame.K_UP]:
            self.paddle2.move_up()
        if keys[pygame.K_DOWN]:
            self.paddle2.move_down()

        self.ball.update(self.paddle1, self.paddle2)

    def draw(self, screen: pygame.surface):
        self.ball.draw(screen)
        self.paddle1.draw(screen)
        self.paddle2.draw(screen)
