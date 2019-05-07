import pygame
from pygame.sprite import Sprite
import random

class Bomb(Sprite):
    def __init__(self, ai_settings, screen):
        super(Bomb, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/bomb.png')
        self.bomb_image=pygame.image.load('images/bang.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1200 * random.random()
        self.rect.y = -5000*random.random()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.is_bomb=False

    def blit(self):
        if self.is_bomb==False:
            self.screen.blit(self.image,self.rect)
        else:self.screen.blit(self.bomb_image,self.rect)

    def update(self,stats):
        if stats.game_stop==False:
            self.y+=self.ai_settings.button_speed_factor
            self.rect.y=self.y

