import pygame.font

class Feed_board():

    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stats=stats
        self.font=pygame.font.SysFont(None,48)
        self.show_feed()

    def show_feed(self):
        if self.stats.infinited_mode==True and self.stats.game_over==False:
            self.feed_image=pygame.image.load('images/famine'+str(self.stats.famine)+'.png')
            self.screen.blit(self.feed_image,(1020,110))