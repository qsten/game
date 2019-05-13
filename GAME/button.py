import pygame.ftfont

class Button:

    def __init__(self,screen):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect=pygame.Rect(550,350,200,100)
        self.image=pygame.image.load('images/start.png')

    def draw_button(self):
        self.screen.blit(self.image,self.rect)




