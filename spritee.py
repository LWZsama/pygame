import pygame
import math

# 初始化Pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Horizontal and Vertical S-Curve Sprite Example")

# 定义精灵类
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.angle = 0

    def update(self):
        # 沿水平和垂直的"S"型路径移动
        self.x = SCREEN_WIDTH / 2 + 200 * math.sin(self.angle)
        self.y = SCREEN_HEIGHT / 2 + 100 * math.sin(2 * self.angle)
        self.rect.center = (self.x, self.y)
        self.angle += 0.01

# 创建精灵组
all_sprites = pygame.sprite.Group()
my_sprite = MySprite()
all_sprites.add(my_sprite)

# 游戏循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新精灵
    all_sprites.update()

    # 清空屏幕
    screen.fill(WHITE)

    # 绘制精灵
    all_sprites.draw(screen)

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出Pygame
pygame.quit()
