import pygame

hero_rect = pygame.Rect(100, 500, 125, 200)

print("英雄的原点坐标是 %d,%d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸是 %d,%d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)