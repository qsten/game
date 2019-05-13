import pygame
from player import Player
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import  Scoreboard
from lifeboard import Lifeboard
from music_button import Music_button
from stop_button import Stop_button
from statistics_board import Statistics_board
from Restart_button import Restart_button
from return_button import Return_button
from rank_button import Rank_button
from Feed_board import Feed_board
from classical_mode import Classical_mode
from Time_limited_Mode import Time_mode
from Infinited_mode import Infinited_mode
from clock import Clock
from input_box import Input_box
from  Continue_button import  Continue_button
from statistics_board import  Statistics_board
from course import  Course
from back_button import Back_button

def run_game():
    #初始化游戏并创建一个屏幕对象
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('hotdog_invasion')
    play_button=Button(screen)
    player=Player(ai_settings,screen)
    hotdogs=Group()
    bombs=Group()
    stats=GameStats(ai_settings)
    sb=Scoreboard(screen,stats)
    life=Lifeboard(screen,stats)
    music_button = Music_button(screen)
    stop_button=Stop_button(screen,stats)
    restart_button=Restart_button(screen,stats)
    return_button=Return_button(screen,stats)
    rank_button=Rank_button(screen,stats)
    feed_board=Feed_board(screen,stats)
    classical_mode=Classical_mode(screen,stats)
    time_mode=Time_mode(screen,stats)
    infinited_mode=Infinited_mode(screen,stats)
    clock=Clock(screen,stats)
    continue_button=Continue_button(screen,stats)
    input_box=Input_box(screen,stats)
    statistics_board=Statistics_board(screen,stats)
    course=Course(screen,stats)
    back_button=Back_button(screen,stats)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,player,hotdogs,bombs,music_button,stop_button,continue_button,restart_button,return_button,rank_button,classical_mode,time_mode,infinited_mode,course,clock,back_button)
        if stats.game_active:
            gf.create_hotdogs(ai_settings, screen, hotdogs)
            gf.create_bombs(ai_settings, screen, bombs)
            player.update(stats)
            gf.update_hotdog(ai_settings,stats,sb,player,hotdogs)
            gf.update_bomb(stats, player,hotdogs, bombs,statistics_board,rank_button,input_box,restart_button)
            music_button.music_play()
        gf.update_screen(screen,stats,sb,life,player,hotdogs,bombs,play_button,music_button,stop_button,continue_button,restart_button,return_button,rank_button,feed_board,classical_mode,time_mode,infinited_mode,statistics_board,course,clock,back_button)

if __name__=='__main__':
    run_game()

