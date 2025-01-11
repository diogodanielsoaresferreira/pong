class BallPosition:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def from_json(string: dict) -> 'BallPosition':
        return BallPosition(string["x"], string["y"])
