import pygame
import os

# 初始化Pygame
pygame.init()

# 定义窗口尺寸和帧率
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# 加载背景图片和进度条图片
BACKGROUND_IMAGES = ['bg/bg1.png', 'bg/bg2.png', 'bg/bg3.png']
PROGRESS_BAR_IMAGE = 'bg/mouse.png'

# 定义进度条起始位置和速度
PROGRESS_BAR_START_X = 100
PROGRESS_BAR_START_Y = 400
PROGRESS_BAR_SPEED = 3

def update_background(screen, background_index):
    # 加载当前背景图片并绘制到窗口上
    background_image = pygame.image.load(BACKGROUND_IMAGES[background_index])
    screen.blit(background_image, (0, 0))

def update_progress_bar(screen, progress_bar_x):
    # 加载进度条图片并绘制到窗口上
    progress_bar_image = pygame.image.load(PROGRESS_BAR_IMAGE)
    screen.blit(progress_bar_image, (progress_bar_x, PROGRESS_BAR_START_Y))

def main():
    # 创建窗口对象
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Loading Screen")

    clock = pygame.time.Clock()
    
    background_index = 0
    progress_bar_x = PROGRESS_BAR_START_X
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 更新背景
        update_background(screen, background_index)
        
        # 更新进度条位置
        progress_bar_x += PROGRESS_BAR_SPEED
        
        # 如果进度条超过窗口宽度，则重置位置并切换背景
        if progress_bar_x > WINDOW_WIDTH:
            break
        # 更新进度条
        update_progress_bar(screen, progress_bar_x)
        
        # 刷新屏幕
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == '__main__':
    main()
