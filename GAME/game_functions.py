import sys
import random
from hotdog import Hotdog
from bomb import Bomb
from time import sleep
import pygame.ftfont
from input_box import *

pygame.init()
pygame.mixer.init()
background = pygame.image.load('images/background.png')
start_backgroud=pygame.image.load('images/start_background.png')

def check_keydown_events(event,player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key==pygame.K_q:
        sys.exit()

def check_keyup_events(event,player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False

def check_events(ai_settings,screen,stats,play_button,player,hotdogs,bombs,music_button,stop_button,continue_button,restart_button,return_button,rank_button,classical_mode,time_mode,infinited_mode,course,clock,back_botton):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,player)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,player)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            rank_button.rank_flag = False
            check_play_button(ai_settings,screen,stats,play_button,hotdogs,bombs,mouse_x,mouse_y,music_button,stop_button,continue_button,restart_button,return_button,rank_button,classical_mode,time_mode,infinited_mode,course,clock,back_botton)


def Restart(ai_settings, screen,stats,hotdogs,bombs):
    stats.reset_stats()
    hotdogs.empty()
    bombs.empty()
    create_hotdogs(ai_settings, screen, hotdogs)
    create_bombs(ai_settings, screen, bombs)
    ai_settings.initialize_dynamic_settings()


def check_play_button(ai_settings,screen,stats,play_button,hotdogs,bombs,mouse_x,mouse_y,music_button,stop_button,continue_button,restart_button,return_button,rank_button,classical_mode,time_mode,infinited_mode,course,clock,back_button):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    music_button_clicked=music_button.rect.collidepoint(mouse_x,mouse_y)
    stop_button_clicked=stop_button.rect.collidepoint(mouse_x,mouse_y)
    restart_button_clicked=restart_button.rect.collidepoint(mouse_x,mouse_y)
    continue_button_clicked=continue_button.rect.collidepoint(mouse_x,mouse_y)
    return_button_clicked=return_button.rect.collidepoint(mouse_x,mouse_y)
    rank_button_clicked=rank_button.rect.collidepoint(mouse_x,mouse_y)
    classical_mode_clicked = classical_mode.rect.collidepoint(mouse_x, mouse_y)
    time_mode_clicked=time_mode.rect.collidepoint(mouse_x, mouse_y)
    back_button_clicked=back_button.rect.collidepoint(mouse_x,mouse_y)
    infinited_mode_clicked=infinited_mode.rect.collidepoint(mouse_x, mouse_y)
    if classical_mode_clicked and stats.game_active==True and stats.game_mode==False:
        stats.game_mode=True
        stats.classical_mode=True
        stats.time_mode=False
        stats.infinited_mode=False
        rank_button.read_data()
    if time_mode_clicked and stats.game_active==True and stats.game_mode==False:
        stats.game_mode=True
        stats.time_mode=True
        stats.classical_mode=False
        stats.infinited_mode=False
        rank_button.read_data()
    if infinited_mode_clicked and stats.game_active == True and stats.game_mode==False:
        stats.game_mode = True
        stats.infinited_mode=True
        stats.classical_mode=False
        stats.time_mode=False
        rank_button.read_data()
    if continue_button_clicked:
        continue_button.continue_game()
    if rank_button_clicked:
        rank_button.rank_flag=True
        rank_button.updata()
    if button_clicked and not stats.game_active :
        Restart(ai_settings,screen,stats,hotdogs,bombs)
        course.show_flag=True
    if back_button_clicked and stats.game_active==True:
        Restart(ai_settings, screen, stats, hotdogs, bombs)
        stats.game_active=True
        stats.game_mode=False
        stats.game_stop=False
        stats.game_over=False
    if music_button_clicked:
        music_button.Music_button_play()
    if stop_button_clicked:
        stop_button.stop_game()
    if restart_button_clicked and stats.game_stop==True:
        Restart(ai_settings, screen,stats,hotdogs,bombs)
        stats.game_mode=True
        stats.game_stop=False
        stats.game_over=False
        if stats.time_mode==True:
            clock.reset_time()
    if return_button_clicked and stats.game_over==True or return_button_clicked and stats.game_mode==False :
        Restart(ai_settings, screen, stats, hotdogs, bombs)
        stats.game_active=False
        stats.game_mode=False
        stats.game_over=False

def update_screen(screen,stats,sb,life,player,hotdogs,bombs,play_button,music_button,stop_button,continue_button,restart_button,return_button,rank_button,feed_board,classical_mode,time_mode,infinited_mode,statistics,course,clock,back_button):
    if  stats.game_active==False :
        play_button.draw_button()
        rank_button.blit()
        course.show_course()
        pygame.display.flip()
        screen.blit(start_backgroud, (0, 0))
    elif stats.game_active==True and stats.game_mode==False:
        clock.reset_time()
        classical_mode.blit()
        music_button.blit()
        return_button.blit()
        time_mode.blit()
        infinited_mode.blit()
        pygame.display.flip()
        screen.blit(background, (0, 0))
    else:
        clock.show_time()
        hotdogs.draw(screen)
        for bomb in bombs:
            bomb.blit()
        player.blit()
        if stats.game_over==True:
            statistics.show_statistics()
        sb.show_score()
        life.show_life()
        music_button.blit()
        stop_button.blit()
        back_button.blit()
        continue_button.blit()
        feed_board.show_feed()
        restart_button.blit()
        return_button.blit()
        pygame.display.flip()
        screen.blit(background, (0, 0))

def create_hotdogs(ai_settings,screen,hotdogs):
    if len(hotdogs)==0:
        ai_settings.play_phase+=1
        if ai_settings.play_phase==5:ai_settings.increase_speed()
        hotdog=Hotdog(ai_settings,screen)
        hotdog_width=hotdog.rect.width
        for hotdog_number in range(5):
            hotdog=Hotdog(ai_settings,screen)
            hotdog.x=hotdog_width+10*hotdog_width*random.random()
            hotdog.rect.x=hotdog.x
            hotdogs.add(hotdog)

def create_bombs(ai_settings,screen,bombs):
    if len(bombs)==0:
        bomb=Bomb(ai_settings,screen)
        bomb_width=bomb.rect.width
        for bomb_number in range(2):
            bomb=Bomb(ai_settings,screen)
            bomb.x=bomb_width+10*bomb_width*random.random()
            bomb.rect.x=bomb.x
            bombs.add(bomb)

def check_collide(player,groups):
    flag_collide=False
    for group in groups:
        if ((player.center-group.x-50)**2)+((580-group.y)**2)<5000:
            groups.remove(group)
            flag_collide=True
    return  flag_collide

def check_bottom(groups):
    len_groups=len(groups)
    for group in groups:
        if group.y>=1000:
            groups.remove(group)
    if len(groups)<len_groups:
        return True

def update_hotdog(ai_settings,stats,sb,player,hotdogs):
    hotdogs.update(stats)
    if check_collide(player,hotdogs) :
        if stats.infinited_mode == True and stats.famine<10:
            stats.famine+=1
            if stats.famine==10 and stats.player_life<3:
                stats.famine=0
                stats.player_life+=1
        stats.score+=ai_settings.hotdog_points
    check_bottom(hotdogs)


def update_bomb(stats,player,hotdogs,bombs,statistics,rank_button,input_box,restart_button):
    bombs.update(stats)
    for bomb in bombs:
        if ((player.center-bomb.x-50)**2)+((580-bomb.y)**2)<5000:
            sleep(0.5)
            if stats.time_mode==True and stats.score>=10:
                stats.score-=10
            else:
                stats.player_life-=1
            bombs.remove(bomb)
    if stats.player_life == 0:
        stats.game_stop=True
        stats.alter_score()
        statistics.best_statistics()
        statistics.prep_statistics()
        if stats.score_flag==True:
            hotdogs.empty()
            bombs.empty()
            if stats.score>rank_button.scorelist[-1]:
                print(rank_button.scorelist[-1])
                playername=input_box.ask()
                rank_button.write_score(playername,stats.score)
            stats.score_flag=False
            stats.game_over = True
    check_bottom(bombs)

