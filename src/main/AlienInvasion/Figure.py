import pygame
class Figure:
    def __init__(self,figure):
        # 初始化角色的位置
        self.screen = figure.screen
        self.screen_rect = figure.screen.get_rect()

        # 加载角色的图像并且获取外接的矩形
        self.image = pygame.image.load('images/Portrait.png')
        self.rect = self.image.get_rect()

        # 将角色放在屏幕的中间位置，根据x和y的位置设置剧中的情况
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery


    def blitme(self):
        self.screen.blit(self.image,self.rect)