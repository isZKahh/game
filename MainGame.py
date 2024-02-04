import pygame
from Tools import *
from Settings import *


class Game:
    def __init__(self, master):
        self.screen = master
        self.image_array = []
        self.rect_group = []
        self.bgx = 0
        self.bgy = 60
        self.main()
        self.generation()

    def main(self):
        self.zifang = FONT4.render('紫方', True, (128, 0, 128))
        self.up_bt = IM_pg(master=self.screen, image='image/up.png', rect=(0, 0), group=self.image_array, group_mode=1,
                           rect_group=self.rect_group, rect_group_mode=1)
        '''
        b1 = pygame.image.load('image/button/button1.png')
        b3 = pygame.image.load('image/button/jb.png')
        '''
        self.build = IM_pg(master=self.screen, image='image/button/jb.png', rect=(300, 23), group=self.image_array,
                           group_mode=1, rect_group=self.rect_group, rect_group_mode=1)
        self.army = IM_pg(master=self.screen, image='image/button/button1.png', rect=(170, 12), group=self.image_array,
                          group_mode=1, rect_group=self.rect_group, rect_group_mode=1)
        self.ar = IM_pg(master=self.screen, image='image/army_divisions.png', rect=(250, 18), group=self.image_array,
                        group_mode=1, rect_group=self.rect_group, rect_group_mode=1)
        self.bg_game = IM_pg(master=self.screen, image='map/bg2.png', rect=(self.bgx, self.bgy), group=self.image_array,
                             group_mode=1,
                             rect_group=self.rect_group, rect_group_mode=1)

    def generation(self):
        """
        {'country1': {'location': [100, 100], 'army_init_number': 10}, 'country2': {'location': [200, 200], 'army_init_number': 20}}
        :return:
        """
        self.level = LeveGeneration(master=self.screen, levefile='levels/test.json')
        self.info = self.level.returner()
        self.imager = self.level.returner2()
        """
        {'country1': {'location': [100, 100], 'army_init_number': 10}, 'country2': {'location': [200, 200], 'army_init_number': 20}, 'country3': {'location': [300, 300], 'army_init_number': 30}}
        {'country1': <Surface(100x100x32 SW)>, 'country2': <Surface(100x100x32 SW)>, 'country3': <Surface(100x100x32 SW)>}
        
        """
        self.country_list = []
        self.location_list = []
        for key, item_dic in self.info.items():
            self.country_list.append(self.imager[key])
            self.location_list.append(tuple(item_dic['location']))

    def mouse_button_down(self, posX, posY):
        if self.up_bt.r()[0][0] < posX < self.up_bt.r()[0][1] \
                and self.up_bt.r()[1][0] < posY < self.up_bt.r()[1][1]:
            return 'home'
        elif self.build.r()[0][0] < posX < self.build.r()[0][1] \
                and self.build.r()[1][0] < posY < self.build.r()[1][1]:
            return 'build'
        elif self.army.r()[0][0] < posX < self.army.r()[0][1] \
                and self.army.r()[1][0] < posY < self.army.r()[1][1]:
            return 'army'
        elif self.bg_game.r()[0][0] < posX < self.bg_game.r()[0][1] \
                and self.bg_game.r()[1][0] < posY < self.bg_game.r()[1][1]:
            return 'background'
        elif self.ar.r()[0][0] < posX < self.ar.r()[0][1] \
                and self.ar.r()[1][0] < posY < self.ar.r()[1][1]:
            return 'ar'

    def returner(self):
        self.return_list = []
        count = 0
        for _ in range(len(self.image_array)):
            self.return_list.append((self.image_array[count], self.rect_group[count]))
            count += 1
        count = 0
        for _ in range(len(self.country_list)):
            self.return_list.append((self.country_list[count], self.location_list[count]))
            count += 1
        self.return_list.append((self.zifang, (85, 14)))
        # print(self.return_list)
        return self.return_list

    # def move_tmp(self, key: pygame.key.get_pressed()):
    #     if key[pygame.K_RIGHT]:
    #         self.bgx += 10
    #     if key[pygame.K_LEFT]:
    #         self.bgx -= 10
    #     if key[pygame.K_UP]:
    #         self.bgy -= 10
    #     if key[pygame.K_DOWN]:
    #         self.bgy += 10
