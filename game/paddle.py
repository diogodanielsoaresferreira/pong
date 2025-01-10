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
        this.top = 4 * screen.get_height() / 10
        this.height = 2 * this.screen.get_height() / 10
        this.paddle_pos = pygame.Rect(this.left, this.top, this.width, this.height)

    def move_up(this):
        if this.top > 0:
            this.top -= 10

    def move_down(this):
        if this.top < this.screen.get_height() - this.height:
            this.top += 10

    def get_middle_point(this):
        return this.top + this.height / 2

    def update_pos(this, pos):
        pos -= this.height / 2
        if pos < 0:
            this.top = 0
        elif pos >= this.screen.get_height() - this.height:
            this.top = this.screen.get_height() - this.height
        else:
            this.top = pos

    def draw(this, screen: pygame.surface):
        this.paddle_pos = pygame.Rect(this.left, this.top, this.width, this.height)
        pygame.draw.rect(screen, "white", this.paddle_pos, 20)
