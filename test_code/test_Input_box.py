import pygame
pygame.init()
pygame.mixer.init()

from scoreboard import Scoreboard
from settings   import Settings
from game_stats import GameStats
from random import *


class test_Input_box():

    def test_get_event(self,current_string):
        while len(current_string) <= 5:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    inkey = event.key
                    if inkey == K_BACKSPACE:
                        current_string = current_string[0:-1]
                    elif inkey == K_RETURN:
                        break
                    elif inkey == K_MINUS:
                        current_string.append("_")
                    elif inkey <= 127:
                        current_string.append(chr(inkey))
        print(current_string)