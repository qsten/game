import pygame


class Stop_button:
    def __init__(self, screen,stats):
        self.screen = screen
        self.stats=stats
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.rect = pygame.Rect(1200, 95, self.width, self.height)
        self.stop_image = pygame.image.load('images/stop.png')
        self.continue_image=pygame.image.load('images/continue.png')


    def blit(self):
        if self.stats.game_stop==False:
            self.screen.blit(self.stop_image, self.rect)
        else:self.screen.blit(self.continue_image, self.rect)

    def stop_game(self):
        self.stats.game_stop=not self.stats.game_stop

