import pygame.font

class Rank_button:
    def __init__(self, screen,stats):
        self.screen = screen
        self.stats=stats
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(548,450,200,100)
        self.bg_color = (0, 190, 285)
        self.text_color = (248, 248, 244)
        self.font = pygame.font.SysFont(None, 48)
        self.image = pygame.image.load('images/rank.png')
        self.rank_image=pygame.image.load('images/rank_image.png')
        self.rank_flag=False
        self.namelist,self.scorelist=self.read_data()
        self.updata()

    def updata(self):
        self.first_score()
        self.second_score()
        self.third_score()
        self.last_score()
        self.first_name()
        self.second_name()
        self.third_name()
        self.last_name()

    def read_data(self):
        file=self.alt_file()
        f = open(file)
        lines = [line.strip().split('\t') for line in f.readlines()]
        self.namelist = [line[0] for line in lines][:4]
        self.scorelist = [int(line[-1]) for line in lines][:4]
        f.close()
        return self.namelist,self.scorelist

    def write_data(self, namelist, score):
        file = self.alt_file()
        f = open(file, 'w')
        print(file,namelist,score)
        for i in range(4):
            f.write(namelist[i] + '\t' + str(score[i]) + '\n')
        f.close()

    def alt_file(self):
        file = 'classical_rand.txt'
        if self.stats.infinited_mode == True:
            file = 'infinited_rand.txt'
        elif self.stats.time_mode == True:
            file = 'time_rand.txt'
        return file

    def blit(self):
        self.screen.blit(self.image, self.rect)
        if self.rank_flag==True:
            self.updata()
            self.screen.blit(self.rank_image, (0, 0))
            self.screen.blit(self.first_score_image,(780,190))
            self.screen.blit(self.second_score_image, (780, 300))
            self.screen.blit(self.third_score_image, (780, 410))
            self.screen.blit(self.last_score_image, (782, 520))
            self.screen.blit(self.first_name_image, (480, 190))
            self.screen.blit(self.second_name_image, (480, 300))
            self.screen.blit(self.third_name_image, (480, 410))
            self.screen.blit(self.last_name_image, (480, 520))


    def write_score(self,playername,score):
        i=3
        while self.scorelist[i]<score and i>=0:
            i-=1
        self.scorelist.insert(i+1,score)
        self.namelist.insert(i+1,playername)
        self.scorelist=self.scorelist[:-1]
        self.namelist=self.namelist[:-1]
        self.write_data(self.namelist,self.scorelist)


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

    def first_name(self):
        name_str=str(self.namelist[0])
        self.first_name_image=self.font.render(name_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.first_name_image.get_rect()
        self.screen_rect.top=70

    def second_name(self):
        name_str=str(self.namelist[1])
        self.second_name_image=self.font.render(name_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.second_name_image.get_rect()
        self.screen_rect.top=70

    def third_name(self):
        name_str=str(self.namelist[2])
        self.third_name_image=self.font.render(name_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.third_name_image.get_rect()
        self.screen_rect.top=70

    def last_name(self):
        name_str=str(self.namelist[3])
        self.last_name_image=self.font.render(name_str,True,self.text_color,self.bg_color)
        self.screen_rect=self.last_name_image.get_rect()
        self.screen_rect.top=70







