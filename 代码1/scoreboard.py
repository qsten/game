import pygame.font

class Scoreboard():

    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.bg_color=(	0 ,190 ,285)
        self.stats=stats
        self.text_color=(248,248,244)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()
        self.image=pygame.image.load('images/Coins.png')

    def prep_score(self):
        score_str=str(self.stats.score).zfill(5)
        self.score_image=self.font.render(score_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.score_image.get_rect()
        self.screen_rect.top=70

    def show_score(self):
        self.screen.blit(self.image,self.screen_rect)
        self.screen.blit(self.score_image, (81, 94))


