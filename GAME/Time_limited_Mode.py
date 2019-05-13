import pygame.font
import time

class Time_mode():

    def __init__(self,screen,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect = pygame.Rect(900,100,331,375)
        self.stats=stats
        self.image = pygame.image.load('images/Time.png')

    def blit(self):
        self.screen.blit(self.image,self.rect)




