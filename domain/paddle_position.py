class PaddlePosition():
    def __init__(self, x: int, top: int, width: int, height: int):
        self.x = x
        self.top = top
        self.width = width
        self.height = height
    
    def from_json(string: dict) -> 'PaddlePosition':
        return PaddlePosition(string["x"], string["top"], string["width"], string["height"])
