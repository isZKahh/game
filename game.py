import pygame
import random
import sys
import time
import webbrowser
from Settings import *
from Tools import *
import MainGame
import os


os.environ['SDL_VIDEO_CENTERED'] = '1'


class Main:
    def __init__(self, size, title, icon):
        self.size = size
        self.title = title
        self.icon = icon

    def init(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)
        Mu(uid=0, mu_file='sound/zzfy01.ogg', item_type=-1)
        self.clock = pygame.time.Clock()
        self.FPS = self.clock.get_fps()
        self.mode = 'main'
        self.pg()
        self.Button()
        # self.main()

    def Game(self):
        self.mode = 'game'
        self.game_object = MainGame.Game(self.screen)
        self.game_blit_array = self.game_object.returner()
        """
        [(<Surface(1028x60x24 SW)>, (0, 0)),
         (<Surface(28x19x32 SW)>, (300, 23)),
         (<Surface(37x37x32 SW)>, (170, 12)),
         (<Surface(26x27x32 SW)>, (250, 18))]
        """
    def pg(self):
        self.bg_n = random.randint(1, 4)
        self.a = IM_pg(master=self.screen, image=f'bg/bg{self.bg_n}.png', rect=(0, 0))
        self.b = IM_pg(master=self.screen, image='bg/itch io.png', rect=(850, 450))
        self.c = IM_pg(master=self.screen, image='bg/afdian.png', rect=(0, 445))
        self.d = IM_pg(master=self.screen, image='bg/Lushen Game.png', rect=(0, 490))
        '''
        ((0, 1028), (0, 581))   a背景
        ((850, 1034), (450, 584))   b下载
        ((0, 58), (445, 490))   c爱发电
        ((0, 95), (490, 585))   d鲁神
        coordinate
        '''
        self.studio = FONT2.render('鲁神游戏工作室 Lushen Game', True, (0, 0, 0))
        self.title = FONT3.render('战争风云', True, (0, 0, 0))

    def Button(self):
        self.button_start = IM_pg(master=self.screen, image='ui/start.png', rect=(440, 230))
        self.button_producer = IM_pg(master=self.screen, image='ui/producer.png', rect=(440, 310))
        self.button_exit = IM_pg(master=self.screen, image='ui/exit.png', rect=(440, 400))

    def producer(self):
        self.button_producerbg = IM_pg(master=self.screen, image='ui/producerbg.png', rect=(410, 50))
        time.sleep(2)

    def fps(self):

        self.clock.tick(100)
        self.FPS = self.clock.get_fps()
        self.text = FONT1.render(f'fps:{round(self.FPS)}', True, (20, 176, 255))
        pygame.display.update()

    def main(self):
        while True:
            if self.mode == 'main':
                self.fps()
                Blit(master=self.screen, update_list=[(self.a.i(), self.a.t()),
                                                      (self.b.i(), self.b.t()),
                                                      (self.c.i(), self.c.t()),
                                                      (self.d.i(), self.d.t()),
                                                      (self.text, (10, 8)),
                                                      (self.button_start.i(), self.button_start.t()),
                                                      (self.button_producer.i(), self.button_producer.t()),
                                                      (self.button_exit.i(), self.button_exit.t()),
                                                      (self.studio, (400, 550)),
                                                      (self.title, (380, 70))
                                                      ])

            elif self.mode == 'game':
                Blit(master=self.screen,update_list=self.game_blit_array)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.mode == 'main':
                        if self.b.r()[0][0] < x < self.b.r()[0][1] and self.b.r()[1][0] < y < self.b.r()[1][1]:
                            Mu(uid=1, mu_file='sound/menu_01.wav', item_type=0)
                            print('下载')
                            webbrowser.open('https://itch.io/')
                            # 下载
                        elif self.c.r()[0][0] < x < self.c.r()[0][1] and self.c.r()[1][0] < y < self.c.r()[1][1]:
                            Mu(uid=1, mu_file='sound/menu_01.wav', item_type=0)
                            print('爱发电')
                            webbrowser.open('https://afdian.net/a/lushen_game')
                        elif self.d.r()[0][0] < x < self.d.r()[0][1] and self.d.r()[1][0] < y < self.d.r()[1][1]:
                            Mu(uid=1, mu_file='sound/menu_01.wav', item_type=0)
                            print('鲁神')
                        elif (self.button_start.r()[0][0] < x < self.button_start.r()[0][1]
                              and self.button_start.r()[1][0] < y < self.button_start.r()[1][1]):
                            Mu(uid=1, mu_file='sound/menu_01.wav', item_type=0)
                            print('start')
                            self.Game()
                        elif (self.button_producer.r()[0][0] < x < self.button_producer.r()[0][1]
                              and self.button_producer.r()[1][0] < y < self.button_producer.r()[1][1]):
                            Mu(uid=1, mu_file='sound/menu_01.wav', item_type=0)
                            print('producer')
                            self.producer()
                        elif (self.button_exit.r()[0][0] < x < self.button_exit.r()[0][1]
                              and self.button_exit.r()[1][0] < y < self.button_exit.r()[1][1]):
                            Mu(uid=1, mu_file='sound/menu_01.wav', item_type=0)
                            pygame.quit()
                            sys.exit()
                    elif self.mode == 'game':
                        button_down = self.game_object.mouse_button_down(posX=x,posY=y)
                        self.game_object.move_tmp(pygame.key.get_pressed())
                        print(button_down)
            pygame.display.update()


# if __name__ == '__main__':
#     game = Main(size=SIZE, title=TITLE, icon=ICON)
