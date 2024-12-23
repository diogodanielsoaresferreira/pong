import pygame

class Ball:

    def __init__(this, screen):
        this.screen = screen
        this.ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    def draw(this, screen):
        pygame.draw.circle(screen, "white", this.ball_pos, 20)
