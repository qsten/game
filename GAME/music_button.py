import pygame.ftfont
import pygame
pygame.init()
pygame.mixer.init()

class Music_button:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 600, 67, 71)
        self.image=pygame.image.load('images/Sound.png')
        self.BGM_music=pygame.mixer.music.load("music/BGM.mp3")
        self.Music_play=True
        self.music_continuous=True

    def music_play(self):
        if self.Music_play==True and self.music_continuous==True:
            pygame.mixer.music.play()
        self.music_continuous=False

    def Music_button_play(self):
        if self.Music_play==False:
            self.Music_play=True
            self.music_continuous=True
        else:
            self.Music_play=False
            pygame.mixer_music.pause()

    def blit(self):
        self.screen.blit(self.image,self.rect)

