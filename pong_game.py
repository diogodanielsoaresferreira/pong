import pygame
from ball import Ball
from paddle import Paddle

class PongGame:
    def __init__(self, screen: pygame.surface):
        self.screen = screen
        self.ball = Ball(screen)
        self.paddle1 = Paddle(screen, True)
        self.paddle2 = Paddle(screen, False)
    
    def update(self, keys: list[bool]):
        
        (_, y_rel) = pygame.mouse.get_rel()
        (_, y_pos) = pygame.mouse.get_pos()
        
        if keys[pygame.K_w]:
            self.paddle1.move_up()
        if keys[pygame.K_s]:
            self.paddle1.move_down()
        if keys[pygame.K_UP]:
            self.paddle2.move_up()
        if keys[pygame.K_DOWN]:
            self.paddle2.move_down()
        
        if y_rel != 0:
            self.paddle1.update_pos(y_pos)

        self.ball.update(self.paddle1, self.paddle2)

    def is_point_for_player(self):
        if self.ball.x < 0:
            return 2
        if self.ball.x > self.screen.get_width():
            return 1
        return 0

    def draw(self, screen: pygame.surface):
        self.ball.draw(screen)
        self.paddle1.draw(screen)
        self.paddle2.draw(screen)
