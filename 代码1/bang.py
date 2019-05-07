import pygame

class Bang():
    def __init__(self, ai_settings, player):
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/bang.png')
        self.rect = self.image.get_rect()
        self.rect.center=player.rect.centerx
        self.rect.bottom=player.rect.bottom
        self.center=float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image,self.rect)