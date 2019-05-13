import pygame.font


class Infinited_mode():

    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect = pygame.Rect(500,100,331,375)
        self.stats=stats
        self.image = pygame.image.load('images/Infinited.png')

    def blit(self):
        self.screen.blit(self.image,self.rect)