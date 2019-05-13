import time
import pygame

class Clock():

    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.bg_color=(	0 ,190 ,285)
        self.stats=stats
        self.font=pygame.font.SysFont(None,75)
        self.pretime=0
        self.remaining_time=60
        self.text_color = (244, 244, 244)
        self.famine_flag=3
        self.image=pygame.image.load('images/s.png')

    def reset_time(self):
        self.pretime=time.time()
        self.remaining_time=60

    def show_time(self):
        newtime=time.time()
        if int(newtime-self.pretime)>=1 and self.stats.game_stop==False:
            self.remaining_time-=1
            self.pretime=time.time()
            if self.stats.infinited_mode==True:
                self.famine_flag -= 1
                if self.famine_flag<=0 and self.stats.famine>0:
                    self.stats.famine-=1
                    self.famine_flag=3
        time_str = str(+self.remaining_time)
        self.time_image = self.font.render(time_str, True, self.text_color, self.bg_color)
        self.screen_rect = self.time_image.get_rect()
        self.screen_rect.top = 70
        if  self.stats.time_mode==True:
            self.text_color = (240 - self.remaining_time * 4, self.remaining_time * 3, 50)
            self.screen.blit(self.time_image,(600,30))
            self.screen.blit(self.image,(662,28))
            if self.remaining_time==0:
                self.stats.player_life=0





