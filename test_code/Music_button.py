import pygame
pygame.init()
pygame.mixer.init()

from scoreboard import Scoreboard
from settings   import Settings
from game_stats import GameStats
from random import *

class Music_button():
    def __init__(self):
        self.Music_play=True
        self.music_continuous=True
        self.BGM_music=pygame.mixer.music.load("music/BGM.mp3")

    def test_music_play(self):
        if self.Music_play==True and self.music_continuous==True:
            pygame.mixer.music.play()
        self.music_continuous=False

    def test_Music_button_play(self):
        if self.Music_play==False:
            self.Music_play=True
            self.music_continuous=True
        else:
            self.Music_play=False
            pygame.mixer_music.pause()

    def test_music(self):
        self.test_music_play()
        self.test_Music_button_play()