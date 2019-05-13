import pygame


class Back_button:
    def __init__(self, screen,stats,left=585,top=300):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats=stats
        self.rect = pygame.Rect(left,top, 67,71)
        self.image = pygame.image.load('images/Back.png')

    def blit(self):
        if self.stats.game_stop==True and self.stats.game_over==False:
            self.rect = pygame.Rect(680, 300, 67, 71)
            self.screen.blit(self.image, (680, 300))
        if self.stats.game_over==True:
            self.rect = pygame.Rect(640, 510, 67, 71)
            self.screen.blit(self.image, (640, 510))



