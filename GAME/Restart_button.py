import pygame


class Restart_button:
    def __init__(self, screen,stats,left=585,top=300):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats=stats
        self.rect = pygame.Rect(left,top, 67,71)
        self.image = pygame.image.load('images/Reload.png')

    def blit(self):
        if self.stats.game_stop==True and self.stats.game_over==False:
            self.rect = pygame.Rect(585, 300, 67, 71)
            self.screen.blit(self.image, self.rect)
        if self.stats.game_over==True:
            self.rect = pygame.Rect(540, 510, 67, 71)
            self.screen.blit(self.image, (540, 510))



