class GameStats():

    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.player_life = 4
        self.reset_stats()
        self.game_active=False
        self.game_stop=False
        self.best_score=0
        self.score_flag=1

    def reset_stats(self):
        self.score=0
        self.player_life=1

    def alter_game_active(self):
        self.game_active=not self.game_active

    def alter_score(self):
        if self.score>self.best_score:
            self.best_score=self.score