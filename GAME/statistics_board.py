import pygame.font

class Statistics_board():

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.rect = pygame.Rect(400, 20, 600, 500)
        self.bg_color = (0, 190, 285)
        self.text_color = (248, 248, 244)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_statistics()
        self.best_statistics()
        self.image = pygame.image.load('images/win.png')

    def best_statistics(self):
        score_str=str(self.stats.best_score)
        self.best_score_image=self.font.render(score_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.score_image.get_rect()
        self.screen_rect.top=70

    def prep_statistics(self):
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.score_image.get_rect()
        self.screen_rect.top=70

    def show_statistics(self):
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.score_image, (770, 200))
        self.screen.blit(self.best_score_image, (770, 252))