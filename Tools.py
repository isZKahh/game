import pygame
import json


class IM_pg:
    def __init__(self, master, image, rect, group=None, group_mode=0, rect_group=None, rect_group_mode=0):
        if rect_group is None:
            rect_group = []
        if group is None:
            group = []
        self.master = master
        self.image = pygame.image.load(image)
        self.rect = rect
        self.mode = group_mode
        self.array = group
        self.mode2 = rect_group_mode
        self.array2 = rect_group
        wi_he = eval(str(self.image.get_rect())[5:(len(str(self.image.get_rect())) - 1)])
        self.width, self.height = wi_he[2], wi_he[3]
        self.pg()
        self.add()
        # < rect(0, 0, 180, 42) >

    def pg(self):
        self.master.blit(self.image, self.rect)
        pygame.display.update()

    def r(self):
        x = self.rect[0]
        y = self.rect[1]
        '''
        850 450
        '''
        x_ = (x, x + self.width)
        y_ = (y, y + self.height)

        return x_, y_

    def i(self):
        return self.image

    def t(self):
        return self.rect

    def add(self):
        if self.mode == 1:
            self.array.append(self.image)
        if self.mode2 == 1:
            self.array2.append(self.rect)



class Mu:
    def __init__(self, uid, mu_file, item_type):
        self.item_type = item_type
        self.id = uid
        self.mu_file = mu_file
        self.run()

    def run(self):
        music1 = pygame.mixer.Channel(self.id)
        bg = pygame.mixer.Sound(self.mu_file)
        music1.play(bg, self.item_type)


class Blit:
    def __init__(self, master, update_list=None):
        if update_list is None:
            update_list = []
        if update_list:
            for update in update_list:
                master.blit(update[0], update[1])


class Image:
    def __init__(self, image_file, home, num, end):
        self.file = image_file
        self.image_list = []
        self.num = num
        self.home = home
        self.end = end
        self.read()

    def read(self):
        for item in range(self.num):
            image = f'{self.file}{self.home}{item + 1}{self.end}'
            self.image_list.append(image)

    def Image_return(self):
        return self.image_list


class LeveGeneration:
    def __init__(self, master, levefile):
        self.screen = master
        self.file = levefile
        self.information = {}
        self.country_imageArray = {}
        self.read()
        self.generation()

    def read(self):
        with open(self.file, mode='r', encoding='utf-8') as content:
            self.data = json.load(content)
        for dic in self.data:
            for key, information in dic.items():
                self.information[key] = information

    def generation(self):
        for name, info in self.information.items():
            file = f'country/{name}.png'
            image = pygame.image.load(file).convert_alpha()
            self.country_imageArray[name] = image
            self.screen.blit(image, info['location'])

    def returner(self):
        return self.information

    def returner2(self):
        return self.country_imageArray



