import pygame.font


class Classical_mode():

    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect = pygame.Rect(100,100,331,375)
        self.stats=stats
        self.image = pygame.image.load('images/classical.png')

    def blit(self):
        self.screen.blit(self.image,self.rect)

