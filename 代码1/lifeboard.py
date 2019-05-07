import pygame.font

class Lifeboard():

    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stats=stats
        self.font=pygame.font.SysFont(None,48)
        self.show_life()

    def show_life(self):
        self.life_image=pygame.image.load('images/Life'+str(self.stats.player_life)+'.png')
        self.screen.blit(self.life_image,self.screen_rect)