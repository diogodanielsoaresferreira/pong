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
        this.offset = 4 * screen.get_height() / 10
        this.height = 2 * this.screen.get_height() / 10
        this.paddle_pos = pygame.Rect(this.left, this.offset, this.width, this.height)

    def move_up(this):
        if this.offset > 0:
            this.offset -= 10


    def move_down(this):
        if this.offset < this.screen.get_height() - this.height:
            this.offset += 10

    def update_pos(this, pos):
        pos -= this.height / 2
        if pos < 0:
            this.offset = 0
        elif pos >= this.screen.get_height() - this.height:
            this.offset = this.screen.get_height() - this.height
        else:
            this.offset = pos

    def draw(this, screen: pygame.surface):
        this.paddle_pos = pygame.Rect(this.left, this.offset, this.width, this.height)
        pygame.draw.rect(screen, "white", this.paddle_pos, 20)
