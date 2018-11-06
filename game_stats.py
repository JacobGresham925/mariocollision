class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self):
        """Initialize statistics."""
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.lives_left = 3
        self.score = 0
        self.level = 1
