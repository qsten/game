import pygame


class Return_button:
    def __init__(self, screen,stats,left=680,top=300):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats=stats
        self.width, self.height = 67,71
        self.rect = pygame.Rect(left,top, 67,71)
        self.image = pygame.image.load('images/return.png')

    def blit(self):
        if self.stats.game_over==True:
            self.screen.blit(self.image, (740,510))
            self.rect = pygame.Rect(740, 510, 67, 71)
        if self.stats.game_active==True and self.stats.game_mode==False:
            self.screen.blit(self.image, (1200, 600))
            self.rect = pygame.Rect(1200, 600, 67, 71)
