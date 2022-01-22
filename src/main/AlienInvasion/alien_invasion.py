import sys
import pygame
from Settings import Settings
from Ship import Ship
'''
description:创建外星文明入侵的类以及相应的方法   将近100page的讲解，去从项目中理解代码
初始背景，以及设置相应的游戏窗口参数
'''
class AlienInvasion:
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # RGB red green blue RGB所代表的含义
        self.bg_color = (self.settings.bg_color)
    def run_game(self):
        """游戏能够实现自己的循环"""
        while True:
            # 对玩家的键盘和鼠标的时间进行更新的操作
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.ship.blitme()
           # 让刚才绘制的屏幕可见：
            pygame.display.flip()
if __name__ == '__main__':
           #创建游戏的实例并且运行实例
   alien_invasion = AlienInvasion()
   alien_invasion.run_game()


