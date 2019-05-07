import sys
import pygame
import random
from hotdog import Hotdog
from bomb import Bomb
from time import sleep
from statistics_board import Statistics_board
import pygame.ftfont



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

def check_events(ai_settings,screen,stats,play_button,player,hotdogs,bombs,music_button,stop_button,restart_button,return_button,rank_button):
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
            check_play_button(ai_settings,screen,stats,play_button,hotdogs,bombs,mouse_x,mouse_y,music_button,stop_button,restart_button,return_button,rank_button)


def Restart(ai_settings, screen,stats,hotdogs,bombs):
    stats.reset_stats()
    stats.game_stop=False
    stats.score_flag = True
    hotdogs.empty()
    bombs.empty()
    create_hotdogs(ai_settings, screen, hotdogs)
    create_bombs(ai_settings, screen, bombs)
    ai_settings.initialize_dynamic_settings()

def check_play_button(ai_settings,screen,stats,play_button,hotdogs,bombs,mouse_x,mouse_y,music_button,stop_button,restart_button,return_button,rank_button):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    music_button_clicked=music_button.rect.collidepoint(mouse_x,mouse_y)
    stop_button_clicked=stop_button.rect.collidepoint(mouse_x,mouse_y)
    restart_button_clicked=restart_button.rect.collidepoint(mouse_x,mouse_y)
    return_button_clicked=return_button.rect.collidepoint(mouse_x,mouse_y)
    rank_button_clicked=rank_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        Restart(ai_settings,screen,stats,hotdogs,bombs)
        stats.alter_game_active()
    if music_button_clicked:
        music_button.Music_button_play()
    if stop_button_clicked:
        stop_button.stop_game()
    if restart_button_clicked:
        Restart(ai_settings, screen,stats,hotdogs,bombs)
    if return_button_clicked:
        Restart(ai_settings, screen, stats, hotdogs, bombs)
        stats.game_active=False
    if rank_button_clicked:
        rank_button.rank_flag=True
        rank_button.first_score()
        rank_button.second_score()
        rank_button.third_score()
        rank_button.last_score()

def update_screen(screen,stats,sb,life,player,hotdogs,bombs,play_button,music_button,stop_button,restart_button,return_button,rank_button):
    if not stats.game_active :
        play_button.draw_button()
        rank_button.blit()
        pygame.display.flip()
        screen.blit(start_backgroud, (0, 0))
    else:
        restart_button.blit()
        return_button.blit()
        hotdogs.draw(screen)
        for bomb in bombs:
            bomb.blit()
        player.blit()
        sb.show_score()
        life.show_life()
        music_button.blit()
        stop_button.blit()
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
    if check_collide(player,hotdogs):
        player.famine+=1
        stats.score+=ai_settings.hotdog_points
        sb.prep_score()
    check_flag=check_bottom(hotdogs)
    if player.famine >0 and check_flag:
        player.famine-=1

def update_bomb(screen,stats,player,bombs,statistics,rank_button):
    bombs.update(stats)
    for bomb in bombs:
        if ((player.center-bomb.x-50)**2)+((580-bomb.y)**2)<5000:
            bomb.screen.blit(bomb.bomb_image,bomb.rect)
            sleep(0.5)
            stats.player_life-=1
            bombs.remove(bomb)
    if stats.player_life == 0:
        statistics_board=Statistics_board(screen,stats)
        stats.game_stop=True
        stats.alter_score()
        if stats.score_flag==True:
            rank_button.write_score(stats.score)
            stats.score_flag=False
        statistics.best_statistics()
        statistics.prep_statistics()
        statistics_board.show_statistics()
    check_bottom(bombs)

