import pygame

class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen: pygame.surface):
        pos = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, "white", pos, 20)
