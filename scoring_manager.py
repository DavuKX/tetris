class GameScoreManager:
    def __init__(self):
        self.score = 0
    
    def calculate_score(self, lines_cleared: int, move_down_points) -> int:
        score = 0
        if lines_cleared == 1:
            score += 100
        elif lines_cleared == 2:
            score += 300
        elif lines_cleared == 3:
            score += 500
        elif lines_cleared >= 4:
            score += 800
        
        return score + move_down_points
    
    def update_score(self, lines_cleared: int, move_down_points: int):
        self.score += self.calculate_score(lines_cleared, move_down_points)
    
    def reset_score(self):
        self.score = 0