class Settings():
    """储存《热狗大战》的所有设置的类"""

    def __init__(self):

        self.screen_width=1280
        self.screen_height=680
        self.bg_color=(230,230,230)

        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        self.increase_speed()

    def initialize_dynamic_settings(self):
        self.play_phase=0
        self.hotdog_points = 5
        self.player_speed_factor=8
        self.hotdog_speed_factor=15
        self.button_speed_factor=15

    def increase_speed(self):
        self.play_phase=0
        self.player_speed_factor *= self.speedup_scale
        self.hotdog_speed_factor *= self.speedup_scale
        self.button_speed_factor *= self.speedup_scale
        self.hotdog_points=int(self.hotdog_points*self.score_scale)

