import pygame
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

    def draw(self, player_1_score: int, player_2_score: int):
        self.screen.fill("black")

        self.ball.draw(self.screen)
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)

        text = self.font.render(str(player_1_score) + "-" + str(player_2_score), 1, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() / 2 - 45, 10))
        
        pygame.display.flip()
