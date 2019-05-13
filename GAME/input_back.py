import pygame


class Input_back():
    def __init__(self, input_box):
        self.input_box = input_box
        self.screen_rect = input_box.screen.get_rect()
        self.stats=input_box.stats
        self.input_box_imgae_rect = pygame.Rect(555, 510, 67, 71)
        self.input_box_imgae = pygame.image.load('images/gameover.png')

    def blit(self):
        self.input_box.screen.blit(self.input_box_imgae, (500, 430))

