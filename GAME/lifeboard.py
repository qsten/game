import pygame.font

class Lifeboard():

    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stats=stats
        self.show_life()

    def show_life(self):
        if self.stats.player_life>=1 and self.stats.time_mode==False:
            self.life_image=pygame.image.load('images/Life'+str(self.stats.player_life)+'.png')
            self.screen.blit(self.life_image,(1030,40))