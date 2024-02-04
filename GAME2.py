import pygame
import random
import os
import sys
import time
import webbrowser
import json

bglist = ['bg/bg1.png','bg/bg2.png','bg/bg3.png','bg/bg4.png']
maplist = ['map/map1/map01.png']

def check_file_exists(file_path):
    return os.path.isfile(file_path)
file_path = 'game.txt'
if check_file_exists(file_path):
    print('已接收到校验码，可以正常游戏')
    #os.remove(file_path)
else:
    print('请使用启动器启动游戏')
    time.sleep(5)
    sys.exit()

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1028,581))
pygame.display.set_caption("战争风云")
icon = pygame.image.load('icon.ico')
pygame.display.set_icon(icon)
bg = pygame.image.load(random.choice(bglist))
itchio = pygame.image.load('bg/itch io.png')
afdian = pygame.image.load('bg/afdian.png')
lushengame = pygame.image.load('bg/Lushen Game.png')
Cstart = pygame.image.load('ui/start.png')
Cstart_rect = Cstart.get_rect()
Cexit = pygame.image.load('ui/exit.png')
Cproducer = pygame.image.load('ui/producer.png')
font1 = pygame.font.Font('font/font.ttc',75)
font2 = pygame.font.Font('font/font.ttc',20)
font3 = pygame.font.Font('font/font.ttc',35)
title = font1.render('战争风云',True,(0,0,0))
studio = font2.render('鲁神游戏工作室 Lushen Game',True,(0,0,0))
text1 = font3.render('欢迎来到新手教程,请按照教程操作',True,(0,0,0))
text2 = font3.render('紫方',True,(128,0,128))
map = pygame.image.load(random.choice(maplist))
army_divisions = pygame.image.load('image/army_divisions.png')
tank_divisions = pygame.image.load('image/tank_divisions.png')
army_vehicle_division = pygame.image.load('image/army_vehicle_Division.png')
up = pygame.image.load('image/up.png')
b1 = pygame.image.load('image/button/button1.png')
b3 = pygame.image.load('image/button/jb.png')
db1 = pygame.image.load('image/button/divisions_button.png')
db2 = pygame.image.load('image/button/divisions_button2.png')
db3 = pygame.image.load('image/button/divisions_button3.png')
close_button = pygame.image.load('image/button/close.png')
divisions_bg = pygame.image.load('image/divisionsbg.png')
producer = pygame.image.load('ui/producerbg.png')
scbg = pygame.image.load('image/scbg.png')
shc = pygame.image.load('image/button/shc.png')
bg2 = pygame.image.load('image/bg2.png')
gc1 = pygame.image.load('image/button/gc1.png')
gc2 = pygame.image.load('image/button/gc2.png')
gc3 = pygame.image.load('image/button/gc3.png')
gc4 = pygame.image.load('image/button/gc4.png')
gc5 = pygame.image.load('image/button/gc5.png')
gcjt = pygame.image.load('image/jt.png')
pygame.mixer.music.load('sound/zzfy01.ogg')
pygame.mixer.music.play()
clock = pygame.time.Clock()
data = {'tank_number':2,
        'army_number':2,
        'army_vehicle_number':1,
        'gc_number':0,
        'sc_army_number':0,
        'sc_tank_number':0,
        'sc_army_vehicle_number':0,
        'divisions_tank_number':0,
        'divisions_army_number':0,
        'divisions_army_vehicle_number':0,
        'sc':0,
        }
with open('save/save1.json','w',encoding='utf-8') as f:
    json.dump(data,f)
    f.close()

def game_event():
    global flag
    global data
    flag = False
    mousexy = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 250 <= mousexy[0] <= 250 + 26 and 18 <= mousexy[1] <= 18 + 27:   #如果点击了训练士兵按钮
                pygame.mixer.music.load('sound/menu_01.wav')
                pygame.mixer.music.play()
                time.sleep(0.1)
                pygame.mixer.music.load('sound/zzfy01.ogg')
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
                while True:
                    mousexy = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if 235 <= mousexy[0] <= 235 + 84 and 540 <= mousexy[1] <= 540 + 27:  # 如果点击了训练按钮
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                flag = True
                                break
                            elif 100 <= mousexy[0] <= 100 + 84 and 340 <= mousexy[1] <= 340 + 27:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['army_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                            elif 100 <= mousexy[0] <= 100 + 84 and 440 <= mousexy[1] <= 440 + 27:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['army_vehicle_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                            elif 100 <= mousexy[0] <= 100 + 84 and 540 <= mousexy[1] <= 540 + 27:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['tank_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                    if flag:
                        flag = False
                        break
                    screen.blit(divisions_bg, (0, 250))
                    screen.blit(db1, (100, 340))
                    screen.blit(db2, (100, 440))
                    screen.blit(db3, (100, 540))
                    screen.blit(close_button, (235, 540))
                    pygame.display.update()
            elif 300 <= mousexy[0] <= 300 + 28 and 23 <= mousexy[1] <= 23 + 19:  #如果点击了生产按钮
                pygame.mixer.music.load('sound/menu_01.wav')
                pygame.mixer.music.play()
                time.sleep(0.1)
                pygame.mixer.music.load('sound/zzfy01.ogg')
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
                while True:
                    mousexy = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if 235 <= mousexy[0] <= 235 + 84 and 540 <= mousexy[1] <= 540 + 27:  #如果点击了退出按钮
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                flag = True
                                break
                            elif 140 <= mousexy[0] <= 140 + 84 and 250 <= mousexy[1] <= 250 + 27:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['sc_army_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                            elif 140 <= mousexy[0] <= 140 + 84 and 360<= mousexy[1] <= 360 + 27:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['sc_army_vehicle_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                            elif 140 <= mousexy[0] <= 140 + 84 and 473<= mousexy[1] <= 473 + 27:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['sc_tank_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                    if flag:
                        flag = False
                        break
                    screen.blit(scbg,(0,150))
                    screen.blit(close_button,(235,540))
                    screen.blit(shc,(140,250))
                    screen.blit(shc, (140, 360))
                    screen.blit(shc, (140, 473))
                    pygame.display.update()
            elif 170 <= mousexy[0] <= 170 + 37 and 12 <= mousexy[1] <= 12 + 37: #如果点击了国策按钮
                pygame.mixer.music.load('sound/menu_01.wav')
                pygame.mixer.music.play()
                time.sleep(0.1)
                pygame.mixer.music.load('sound/zzfy01.ogg')
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
                while True:
                    mousexy = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if 600 <= mousexy[0] <= 600 + 84 and 530 <= mousexy[1] <= 530 + 27:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                flag = True
                                break
                            elif 80 <= mousexy[0] <= 80 + 40 and 500 <= mousexy[1] <= 500 + 38:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['gc_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                            elif 180 <= mousexy[0] <= 180 + 55 and 500 <= mousexy[1] <= 500 + 37:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['gc_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                            elif 280 <= mousexy[0] <= 280 + 49 and 500 <= mousexy[1] <= 500 + 36:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['gc_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                            elif 380 <= mousexy[0] <= 380 + 58 and 500 <= mousexy[1] <= 500 + 41:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['gc_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                            elif 480 <= mousexy[0] <= 480 + 56 and 490 <= mousexy[1] <= 490 + 45:
                                pygame.mixer.music.load('sound/menu_01.wav')
                                pygame.mixer.music.play()
                                time.sleep(0.1)
                                pygame.mixer.music.load('sound/zzfy01.ogg')
                                pygame.mixer.music.play()
                                clock = pygame.time.Clock()
                                with open('save/save1.json', 'w', encoding='utf-8') as f:
                                    data['gc_number'] += 1
                                    json.dump(data, f)
                                    f.close()
                    if flag:
                        flag = False
                        break
                    screen.blit(bg2,(0,450))
                    screen.blit(gc1,(80,500))
                    screen.blit(gc2, (180, 500))
                    screen.blit(gc3, (280, 500))
                    screen.blit(gc4,(380,500))
                    screen.blit(gc5,(480,490))
                    screen.blit(gcjt,(100,465))
                    screen.blit(gcjt, (200, 465))
                    screen.blit(gcjt, (300, 465))
                    screen.blit(gcjt, (405, 465))
                    screen.blit(close_button,(600,530))
                    pygame.display.update()
def ai():
    mousexy = pygame.mouse.get_pos()

while True:
    mousexy = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if 440<=mousexy[0]<=440+180 and 400<= mousexy[1]<=400+42: #退出游戏
                pygame.mixer.music.load('sound/menu_01.wav')
                pygame.mixer.music.play()
                pygame.quit()
                sys.exit()
            elif 440<=mousexy[0]<=440+180 and 230<= mousexy[1]<=230+45:  #开始游戏
                pygame.mixer.music.load('sound/menu_01.wav')
                pygame.mixer.music.play()
                time.sleep(0.1)
                pygame.mixer.music.load('sound/zzfy01.ogg')
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
                while True:    #游戏主循环
                    game_event()
                    screen.fill((0,0,0))
                    #time.sleep(5)
                    screen.blit(map,(0,0))
                    screen.blit(up,(0,0))
                    screen.blit(army_divisions,(250,18))
                    screen.blit(b1,(170,12))
                    screen.blit(b3,(300,23))
                    screen.blit(text1,(250,250))
                    screen.blit(text2,(85,14))

                    #步兵
                    screen.blit(army_divisions,(365,354))
                    screen.blit(army_divisions, (543,282))
                    screen.blit(army_divisions, (748, 343))
                    screen.blit(army_divisions, (378, 210))
                    screen.blit(army_divisions, (54, 109))
                    screen.blit(army_divisions, (543, 87))
                    screen.blit(army_divisions, (900, 250))
                    screen.blit(army_divisions, (750,200))
                    screen.blit(army_divisions, (100, 250))
                    screen.blit(army_divisions, (500, 400))
                    screen.blit(army_divisions, (850, 410))

                    #坦克
                    screen.blit(tank_divisions,(300,354))
                    screen.blit(tank_divisions, (700,400))
                    screen.blit(tank_divisions, (750,150))
                    screen.blit(tank_divisions, (500,200))
                    screen.blit(tank_divisions, (100,150))
                    screen.blit(tank_divisions, (830,250))
                    screen.blit(tank_divisions, (750,500))
                    screen.blit(tank_divisions, (450, 200))

                    #军车
                    screen.blit(army_vehicle_division, (900, 200))
                    screen.blit(army_vehicle_division, (900, 500))
                    screen.blit(army_vehicle_division, (600, 200))
                    screen.blit(army_vehicle_division, (450, 250))

                    dt = clock.tick(60)
                    fps = clock.get_fps()
                    font = pygame.font.Font('font/font.ttc', 24)
                    fps_text = font.render("FPS: {:.2f}".format(fps), True, (0, 0, 0))
                    screen.blit(fps_text, (10, 80))

                    pygame.display.update()
            elif 440<=mousexy[0]<=440+182 and 310<= mousexy[1]<=310+46:   #开发者名单
                pygame.mixer.music.load('sound/menu_01.wav')
                pygame.mixer.music.play()
                time.sleep(0.1)
                pygame.mixer.music.load('sound/zzfy01.ogg')
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
                screen.blit(producer,(410,50))
                pygame.display.update()
                time.sleep(3)


            elif 0<=mousexy[0]<=0+58 and 445<= mousexy[1]<=445+45:  #爱发电
                pygame.mixer.music.load('sound/menu_02.wav')
                pygame.mixer.music.play()
                url = "https://afdian.net/a/lushen_game"
                webbrowser.open(url)
                time.sleep(0.1)
                pygame.mixer.music.load('sound/zzfy01.ogg')
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
            elif 850<=mousexy[0]<=850+184 and 450<=mousexy[1]<=450+45:  #itch io
                pygame.mixer.music.load('sound/menu_02.wav')
                pygame.mixer.music.play()
                url = "https://itch.io/"
                webbrowser.open(url)
                time.sleep(0.1)
                pygame.mixer.music.load('sound/zzfy01.ogg')
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
    screen.blit(bg, (0, 0))
    screen.blit(itchio,(850,450))
    screen.blit(afdian,(0,445))
    screen.blit(lushengame,(0,490))
    screen.blit(Cstart,(440,230))
    screen.blit(Cexit,(440,400))
    screen.blit(Cproducer,(440,310))
    screen.blit(title, (380,70))
    screen.blit(studio,(400,550))
    dt = clock.tick(60)
    fps = clock.get_fps()
    font = pygame.font.Font('font/font.ttc',24)
    fps_text = font.render("FPS: {:.2f}".format(fps), True, (0, 0, 0))
    screen.blit(fps_text, (10, 10))
    pygame.display.update()
