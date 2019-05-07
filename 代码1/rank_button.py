import pygame.font
import IoData


class Rank_button:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(548,450,200,100)
        self.bg_color = (0, 190, 285)
        self.text_color = (248, 248, 244)
        self.font = pygame.font.SysFont(None, 48)
        self.image = pygame.image.load('images/rank.png')
        self.rank_image=pygame.image.load('images/rank_image.png')
        self.rank_flag=False
        self.namelist,self.scorelist=IoData.read_data()
        self.first_score()
        self.second_score()
        self.third_score()
        self.last_score()

    def blit(self):
        self.screen.blit(self.image, self.rect)
        if self.rank_flag==True:
            self.screen.blit(self.rank_image, (0, 0))
            self.screen.blit(self.first_score_image,(780,190))
            self.screen.blit(self.second_score_image, (780, 300))
            self.screen.blit(self.third_score_image, (780, 410))
            self.screen.blit(self.last_score_image, (780, 520))


    def write_score(self,score):
        self.scorelist.append(score)
        self.scorelist= sorted(self.scorelist,reverse=True)[:-1]
        IoData.write_data(self.namelist,self.scorelist)

    def first_score(self):
        score_str=str(self.scorelist[0])
        self.first_score_image=self.font.render(score_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.first_score_image.get_rect()
        self.screen_rect.top=70

    def second_score(self):
        score_str=str(self.scorelist[1])
        self.second_score_image=self.font.render(score_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.second_score_image.get_rect()
        self.screen_rect.top=70

    def third_score(self):
        score_str=str(self.scorelist[2])
        self.third_score_image=self.font.render(score_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.third_score_image.get_rect()
        self.screen_rect.top=70

    def last_score(self):
        score_str=str(self.scorelist[3])
        self.last_score_image=self.font.render(score_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.last_score_image.get_rect()
        self.screen_rect.top=70






