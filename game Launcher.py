# import subprocess
import time
import random
import game
from Settings import *

print('正在启动游戏')
a = random.randint(4000, 9000)


def game_launcher():
    print('start')
    Game = game.Main(size=SIZE, title=TITLE, icon=ICON)


# game_path = ''  # 请替换为你的游戏可执行文件路径
game_launcher()
