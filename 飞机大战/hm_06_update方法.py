import pygame

pygame.init()

# 1. 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 2. 绘制背景图像
bg = pygame.image.load("./Image/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 3.绘制英雄的飞机
hero = pygame.image.load("./Image/me1.png")
screen.blit(hero, (150, 300))

# 可以在所有绘制工作完成后，统一调用update方法
pygame.display.update()

while True:

    pygame.event.get(1000)


pygame.quit()