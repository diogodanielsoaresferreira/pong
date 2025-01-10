import pygame

class Circle:
    def __init__(self, x: int, y: int, r: int):
        self.x = x
        self.y = y
        self.r = r
    
    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self, screen: pygame.surface):
        pygame.draw.circle(screen, "white", pygame.Vector2(self.x, self.y), self.r)
