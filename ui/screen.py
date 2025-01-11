import pygame
from domain.ball_position import BallPosition
from domain.paddle_position import PaddlePosition
from ui.circle import Circle
from ui.rectangle import Rectangle

class Screen:
    def __init__(self, screen: pygame.surface):
        pygame.init()
        self.screen = screen
        self.font = pygame.font.Font(None, 80)
        self.ball = Circle(self.screen.get_width() / 2, self.screen.get_height() / 2, 20)
        self.paddle1 = Rectangle(10, 4 * self.screen.get_height() / 10, 20, 2 * self.screen.get_height() / 10)
        self.paddle2 = Rectangle(self.screen.get_width() - 30, 4 * self.screen.get_height() / 10, 20, 2 * self.screen.get_height() / 10)

    def draw(self, paddle_1_position: PaddlePosition, paddle_2_position: PaddlePosition, ball_position: BallPosition, player_1_score: int, player_2_score: int):
        self.screen.fill("black")

        self.ball.move(ball_position.x, ball_position.y)
        self.paddle1.move(paddle_1_position.top, paddle_1_position.height)
        self.paddle2.move(paddle_2_position.top, paddle_2_position.height)

        self.ball.draw(self.screen)
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)

        text = self.font.render(str(player_1_score) + "-" + str(player_2_score), 1, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() / 2 - 45, 10))
        
        pygame.display.flip()
