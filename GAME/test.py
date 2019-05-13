import pygame
pygame.init()
pygame.mixer.init()

import time
import _thread



# import unittest
#
#
# # 测试文件读写
# from IoData import *
# class IOdataTestCase(unittest.TestCase):   #必须继承unittest.TestCase类
#     def Iodata(self):
#         namelist=['null','null','null','null']
#         scorelist=[0,0,0,0,0]
#         write_data(namelist,scorelist)
#         testname,testscore=read_data()
#         self.assertEqual(testname,['null','null','null','null'])
#
# unittest.main
#
# from scoreboard import Scoreboard
# from settings   import Settings
# from game_stats import GameStats
# from random import *
#
#
#
# class Statistics_board_test (unittest.TestCase):
#     score = random.random()
#     rect = pygame.Rect(0,0,0,0)
#     bg_color = (0,0,0,0)
#     text_color = (0,0,0,0)
#     font = pygame.font.SysFont(None, 48)
#
#     def test_best_statistics(self):
#         score_str = str(self.score).zfill(5)
#         self.score_image = self.font.render(score_str, True,self.text_color, self.bg_color)
#         self.screen_rect = self.score_image.get_rect()
#         self.screen_rect.top = 0
#         return self.screen_rect
#
#     def test_prep_statistics(self):
#         score_str=str(self.score)
#         self.score_image=self.font.render(score_str,True,self.text_color,self.bg_color)
#         self.screen_rect=self.score_image.get_rect()
#         self.screen_rect.top=0
#         return self.screen_rect
#
#     def test(self):
#         best_statistics=self.test_best_statistics()
#         prep_statistics=self.test_prep_statistics()
#         self.assertEqual(best_statistics,prep_statistics)
#
#
# class test_player(unittest.TestCase):
#     moving_right=True
#     moving_left=False
#     rect_left=0
#     rect_right=0
#     stats_famine=0
#     game_stop=False
#     player_speed_factor=1
#     center=random.random()
#     def update(self):
#         if self.game_stop == False:
#             if self.moving_right and self.rect_right < self.screen_rect_right:
#                 self.center += self.player_speed_factor * (self.stats_famine / 20 + 1)
#             elif self.moving_left and self.rect_left > 0:
#                 self.center -= self.player_speed_factor * (self.stats_famine / 20 + 1)
#             self.rect_centerx = self.center
#         return self.rect_centerx
#
#     def test_updata(self):
#         test_rect_centerx=self.updata()
#         self.assertEqual(test_rect_centerx,1)
#
