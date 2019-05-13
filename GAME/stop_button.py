import pygame


class Stop_button:
    def __init__(self, screen,stats):
        self.screen = screen
        self.stats=stats
        self.screen_rect = screen.get_rect()
        self.width, self.height = 67,71
        self.rect = pygame.Rect(1200, 600, self.width, self.height)
        self.stop_image = pygame.image.load('images/stop.png')
        self.pause_image=pygame.image.load('images/paused.png')

    def blit(self):
        if self.stats.game_stop==False:
            self.screen.blit(self.stop_image, self.rect)
        elif self.stats.game_over==False:
            self.screen.blit(self.pause_image,(460,250))

    def stop_game(self):
        self.stats.game_stop=True

