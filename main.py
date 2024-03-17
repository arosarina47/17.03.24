from pygame import*
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load("nyancat.jpg"), (win_width, win_height))

game = True #щоб гра відкривлась/закривалась
clock = time.Clock() #частота кадрів
FPS = 60
class GameSprite(sprite.Sprite): #загальні характеристики персонажів
    def __init__(self,player_image, player_x, player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65)) #зображення персонажів
        self.speed = player_speed
        self.rect = self.image.get_rect() #невидима обводка чи стикнулись персонажі
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): #на екран персонажа
        window.blit(self.image, ( self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width -70:
            self.rect.x += self.speed
            if keys[K_UP] and self.rect.y > 3:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < win_width -70:
                self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3, wall_x ,wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((color1,color2,color3))
        self.rect = self.image.get_rect()
        self.rect_x = wall_x
        self.rect_y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
w1 = Wall(234, 252, 182, 100,20,450,10)
w1 = Wall(234, 252, 182, 100,20,10,380)




player = Player("catcool.jpg",5, win_height - 80,4)
monster = Enemy('angrycat.png', win_width - 80,280,3)
goal = GameSprite('cookie.png', 440,420,0)
# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()
font.init()
font1 = font.Font(None,70)
win = font1.render('YOU WIN!', True, (255,215, 0))
lose = font1.render('YOU LOSE!', True, (255,0, 0))
while game:
    for e in event.get(): #щоб віконце не зависало
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    player.update()
    monster.update()
    goal.reset()
    player.reset() #відобразити героя
    monster.reset()
    w1.draw_wall()
    if sprite.collide_rect(player, goal):
        window.blit(win,(200,200))
    if sprite.collide_rect(player, monster): or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)
        window.blit(lose,(200,200))

    display.update()
    clock.tick(FPS) #частота кадрів
