import pygame

class Paddle:
    def __init__(this, screen: pygame.surface, player1: bool):
        this.screen = screen
        this.margin = 10
        this.width = 20
        if player1:
            this.left = this.margin
        else:
            this.left = screen.get_width() - this.margin - this.width
        this.paddle_pos = pygame.Rect(this.left, 4 * screen.get_height() / 10, this.width, 2 * screen.get_height() / 10)
    
    def draw(this, screen: pygame.surface):
        pygame.draw.rect(screen, "white", this.paddle_pos, 20)
