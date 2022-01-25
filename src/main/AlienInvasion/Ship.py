import pygame
class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船的位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/Ship1.png')
        self.rect = self.image.get_rect()
        # 将每艘飞船放置在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        """在特定的位置绘制飞船"""
        self.screen.blit(self.image,self.rect)