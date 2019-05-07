import pygame


class Return_button:
    def __init__(self, screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats=stats
        self.width, self.height = 200, 50
        self.rect = pygame.Rect(1200,300, self.width, self.height)
        self.image = pygame.image.load('images/return.png')

    def blit(self):
        if self.stats.game_stop==True:
            self.screen.blit(self.image, self.rect)