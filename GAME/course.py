import pygame.ftfont
import time

class Course:

    def __init__(self,screen,stats):
        self.screen=screen
        self.stats=stats
        self.screen_rect=screen.get_rect()
        self.rect=pygame.Rect(550,350,200,100)
        self.show_flag=False
        self.show_time=1


    def show_course(self):
        if self.show_time<=7 and self.show_flag==True:
            self.course_image = pygame.image.load('images/course_' + str(self.show_time) + '.png')
            self.screen.blit(self.course_image, (321, 483))
            time.sleep(0.25)
            self.show_time+=1
        if self.show_time==8:
            self.stats.game_active=True
            self.show_time=1
            self.show_flag=False





