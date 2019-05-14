import pygame
from pygame.sprite import Sprite

class Player(Sprite):

    def __init__(self,ai_settings,screen):
        """初始化玩家并设置其初始位置"""
        self.screen=screen
        #加载玩家图像并获取其外接矩形
        super(Player,self).__init__()
        self.ai_settings=ai_settings
        self.image=pygame.image.load('images/player.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.moving_right=False
        self.moving_left=False
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        self.score=0
        self.is_bomb=False
        self.bomb_image = pygame.image.load('images/bang.png')

    def blit(self):
        self.screen.blit(self.image,self.rect)

    def update(self,stats):
        if stats.game_stop==False:
            if self.moving_right and self.rect.right<self.screen_rect.right:
                self.center+=self.ai_settings.player_speed_factor*(stats.famine/20+1)
            elif self.moving_left and self.rect.left>0:
                self.center-=self.ai_settings.player_speed_factor*(stats.famine/20+1)
            self.rect.centerx=self.center