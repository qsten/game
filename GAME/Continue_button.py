import pygame


class Continue_button:
    def __init__(self, screen,stats):
        self.screen = screen
        self.stats=stats
        self.screen_rect = screen.get_rect()
        self.width, self.height = 67, 71
        self.rect = pygame.Rect(490,300, self.width, self.height)
        self.continue_image = pygame.image.load('images/continue.png')

    def blit(self):
        if self.stats.game_stop==True and self.stats.game_over==False:
            self.screen.blit(self.continue_image,self.rect)

    def continue_game(self):
            self.stats.game_stop=False
