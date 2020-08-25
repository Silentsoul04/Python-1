import pygame

pygame.init()

# 1. 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 2. 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./Image/background.png")
# 2> blit 绘制在屏幕
screen.blit(bg, (0, 0))
# 3> 更新屏幕显示
# pygame.display.update()

# 3.绘制英雄的飞机
hero = pygame.image.load("./Image/me1.png")
screen.blit(hero, (150, 300))
pygame.display.update()

while True:

    pygame.event.get(1000)


pygame.quit()