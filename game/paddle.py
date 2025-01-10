class Paddle:
    def __init__(self, screen_width: int, screen_height: int, player1: bool):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.margin = 10
        self.width = 20
        if player1:
            self.left = self.margin
        else:
            self.left = screen_width - self.margin - self.width
        self.top = 4 * screen_height / 10
        self.height = 2 * screen_height / 10

    def move_up(self):
        if self.top > 0:
            self.top -= 10

    def move_down(self):
        if self.top < self.screen_height - self.height:
            self.top += 10

    def get_middle_point(self):
        return self.top + self.height / 2

    def update_pos(self, pos):
        pos -= self.height / 2
        if pos < 0:
            self.top = 0
        elif pos >= self.screen_height - self.height:
            self.top = self.screen_height - self.height
        else:
            self.top = pos