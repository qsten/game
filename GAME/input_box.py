import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *




class Input_box():

    def __init__(self, screen,stats):
        self.screen = screen
        self.stats=stats
        self.screen_rect = screen.get_rect()
        self.width, self.height = 67,71
        self.rect = pygame.Rect(200, 50, self.width, self.height)
        self.Input_image = pygame.image.load('images/Input_box.png')
        self.Input_image2 = pygame.image.load('images/Input_box2.png')
        self.input_back_imgae_rect = pygame.Rect(555, 510, 67, 71)
        self.input_back_imgae = pygame.image.load('images/gameover.png')
        self.end_flag=True

    def get_event(self,current_string):
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                print(mouse_x,mouse_y)
                if mouse_x>=497 and mouse_x<=821 and  mouse_y >= 433 and mouse_y<=500 or mouse_x>=1024 and mouse_x<=1104 and  mouse_y >= 68 and mouse_y<=145 :
                    self.end_flag=False

    def display_box(self,message):
      fontobject = pygame.font.Font(None,50)
      if len(message) != 0:
        self.screen.blit(fontobject.render(message, 1, (0,0,0)),(520,315))
      pygame.display.flip()

    def ask(self):
      self.end_flag=True
      pygame.font.init()
      current_string = []
      self.screen.blit(self.Input_image, self.rect)
      self.display_box("".join(current_string))
      while self.end_flag and len(current_string)<=5:
        if len(current_string)>0:
          self.screen.blit(self.Input_image2, self.rect)
        else:self.screen.blit(self.Input_image, self.rect)
        self.screen.blit(self.input_back_imgae, (500, 430))
        self.get_event(current_string)
        self.display_box("".join(current_string))
      return "".join(current_string)
