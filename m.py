import pygame

pygame.init()
# screen = pygame.display.set_mode((300,300))
image = pygame.image.load('ui/exit.png')
print(type(image.get_rect()))