import os
import sys
import pygame


pygame.init()
size = width, height = 1250, 625
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
keyr = pygame.mixer.Sound('keys.wav')
ot = pygame.mixer.Sound('otschet.wav')
pygame.display.set_caption('Лабиринт средневековья')
lvs = {'level1': ['`^^^^^^-^^',
                  '!****=_**I',
                  '`*`^**-*!&',
                  '!&!-*=_&!I',
                  '=^=______&'],
       'level2': ['`-`------~',
                  '!!!^^^^I*%',
                  '==_____&*I',
                  '!*-*--*--I',
                  '=________&'],
       'level3': ['`^^^^^---~',
                  '!*!**^*^!I',
                  '%*!`--*__&',
                  '!*!=*___*&',
                  '=________&'],
       'level4': ['`------^^^',
                  '!^*^*^***I',
                  '=_*___*^-~',
                  '=_*___***I',
                  '=_______=&'],
       'level5': ['`--------~',
                  '!I***^*__&',
                  '!********I',
                  '!I*^***^^^',
                  '=______^^^'],
       'level6': ['^^---^---^',
                  '!********^',
                  '^^*^*^*^*^',
                  '!********I',
                  '^^_^___^_&'],
       'level7': ['`--------~',
                  '!********I',
                  '!********I',
                  '!********I',
                  '=________&']}
all_sprites = pygame.sprite.Group()
dop_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
grasss = pygame.sprite.Group()
keys = pygame.sprite.Group()
gates = pygame.sprite.Group()
knights = pygame.sprite.Group()
vrags = pygame.sprite.Group()
balls = pygame.sprite.Group()
levelses = pygame.sprite.Group()
cursors = pygame.sprite.Group()
hoder = pygame.sprite.Group()
wins = pygame.sprite.Group()
MYEVENTTYPE = pygame.USEREVENT + 1
MYEVENT1 = pygame.USEREVENT + 2
MYEVENT2 = pygame.USEREVENT + 3
MYEVENT3 = pygame.USEREVENT + 4
L1 = pygame.USEREVENT + 5
L2 = pygame.USEREVENT + 6
L3 = pygame.USEREVENT + 7
L4 = pygame.USEREVENT + 8
L5 = pygame.USEREVENT + 9
L6 = pygame.USEREVENT + 10
L7 = pygame.USEREVENT + 11
UP = pygame.USEREVENT + 12
STOP_PAUSE = pygame.USEREVENT + 13
SECOND = pygame.USEREVENT + 14
key1, key2, gate1, gate2, castle, ball, vrag1, color, cursor = None, None, None, None, None, None, None, None, None
startbutton, levels, key3, gate3, hertpl, pausee, knight, motion = None, None, None, None, None, None, None, 'stop'
key4, gate4, dragon, vrag2, dragon1, dragon2 = None, None, None, None, None, None
pygame.mouse.set_visible(False)
pres = 1
level = 0
font1 = pygame.font.SysFont('comicsans', 100)
text1 = font1.render('Пауза...', True, pygame.Color('gold'))
font2 = pygame.font.SysFont('comicsans', 50)
text2 = font2.render('Вы прошли уровень!!!', True, pygame.Color('gold'))
font3 = pygame.font.SysFont('comicsans', 30)
font4 = pygame.font.SysFont('comicsans', 35)
pre0 = font3.render('Пресиданий осталось: 0', True, pygame.Color('yellow'))
pre1 = font3.render('Пресиданий осталось: 1', True, pygame.Color('yellow'))
pre2 = font3.render('Пресиданий осталось: 2', True, pygame.Color('yellow'))
pre3 = font3.render('Пресиданий осталось: 3', True, pygame.Color('yellow'))
pre4 = font3.render('Пресиданий осталось: 4', True, pygame.Color('yellow'))
pre5 = font3.render('Пресиданий осталось: 5', True, pygame.Color('yellow'))
giz1 = font3.render('Жизней осталось: 1', True, pygame.Color('red'))
giz2 = font3.render('Жизней осталось: 2', True, pygame.Color('red'))
giz3 = font3.render('Жизней осталось: 3', True, pygame.Color('red'))
vst0 = font3.render('Время до вставания: 1 секунд', True, pygame.Color('blue'))
vst1 = font3.render('Время до вставания: 2 секунд', True, pygame.Color('blue'))
vst2 = font3.render('Время до вставания: 3 секунд', True, pygame.Color('blue'))
vst3 = font3.render('Время до вставания: 4 секунд', True, pygame.Color('blue'))
vst4 = font3.render('Время до вставания: 5 секунд', True, pygame.Color('blue'))
vst5 = font3.render('Время до вставания: 6 секунд', True, pygame.Color('blue'))
vst6 = font3.render('Время до вставания: 7 секунд', True, pygame.Color('blue'))
vst7 = font3.render('Время до вставания: 8 секунд', True, pygame.Color('blue'))
vst8 = font3.render('Время до вставания: 9 секунд', True, pygame.Color('blue'))
vst9 = font3.render('Время до вставания: 10 секунд', True, pygame.Color('blue'))
ups = font4.render('7 уровень.', True, pygame.Color('gold'))
ups1 = font4.render('Упс... Произошло землятрясение и этот уровень завалило', True, pygame.Color('gold'))
ups2 = font4.render('камнями. Вам повезло, вы прошли игру!!!', True, pygame.Color('gold'))
osh = font3.render('Ошибка системы:', True, pygame.Color('gold'))
osh1 = font3.render('Теперь вы можете', True, pygame.Color('gold'))
osh2 = font3.render('присесть, подойти', True, pygame.Color('gold'))
osh3 = font3.render('к стене над вами', True, pygame.Color('gold'))
osh4 = font3.render('и встать...', True, pygame.Color('gold'))
curs = pygame.sprite.Group()


def builder(level):
    xx = 0
    yy = 0
    for elems in level:
        for elem in elems:
            if elem == '*':
                grass = Grass(xx, yy, 0)
                xx += 125
            elif elem == '!':
                block = Block(xx, yy, 1)
                grass = Grass(xx + 50, yy, 2)
                xx += 125
            elif elem == '-':
                block = Block(xx, yy, 0)
                grass = Grass(xx, yy + 50, 1)
                xx += 125
            elif elem == '`':
                block = Block(xx, yy, 0)
                block1 = Block(xx, yy, 1)
                grass = Grass(xx + 50, yy + 50, 3)
                xx += 125
            elif elem == '~':
                block = Block(xx, yy, 0)
                block1 = Block(xx + 75, yy, 1)
                grass = Grass(xx, yy + 50, 3)
                xx += 125
            elif elem == '=':
                block = Block(xx, yy + 75, 0)
                block1 = Block(xx, yy, 1)
                grass = Grass(xx + 50, yy, 3)
                xx += 125
            elif elem == '&':
                block = Block(xx, yy + 75, 0)
                block1 = Block(xx + 75, yy, 1)
                grass = Grass(xx, yy, 3)
                xx += 125
            elif elem == 'I':
                grass = Grass(xx, yy, 2)
                block = Block(xx + 75, yy, 1)
                xx += 125
            elif elem == '_':
                grass = Grass(xx, yy, 1)
                block = Block(xx, yy + 75, 0)
                xx += 125
            elif elem == '^':
                block = Block(xx, yy, 0)
                block1 = Block(xx, yy + 50, 2)
                xx += 125
            elif elem == '%':
                block = Block(xx, yy, 1)
                block1 = Block(xx + 50, yy, 3)
                xx += 125
        yy += 125
        xx = 0


def load_image(name, color_key=-1):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            if name == 'heart.png' or name == "dragon_sheet8x21.png" or name == 'vopr.png':
                color_key = image.get_at((0, 0))
            else:
                color_key = image.get_at((18, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()
    return image


cursor_image = load_image('k.png')


class Castle(pygame.sprite.Sprite):
    image = load_image('castle.png')

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Castle.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self):
        if pygame.sprite.spritecollideany(self, knights):
            win()


class Pause_button(pygame.sprite.Sprite):
    image = load_image('paus.png', color_key=None)
    image1 = load_image('play.png', color_key=None)


    def __init__(self, x, y, tf):
        super().__init__(all_sprites)
        if tf:
            self.image = Pause_button.image
        else:
            self.image = Pause_button.image1
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self, pos):
        if self.image == Pause_button.image:
            if self.rect.collidepoint(pos):
                x, y = self.rect.x, self.rect.y
                pause(x, y)
        else:
            if self.rect.collidepoint(pos):
                for elem in dop_sprites:
                    elem.kill()
                pygame.time.set_timer(STOP_PAUSE, 1)


class Restart_button(pygame.sprite.Sprite):
    image = load_image('rest.png', color_key=None)

    def __init__(self, x, y, tf):
            super().__init__(all_sprites)
            if tf:
                self.add(dop_sprites)
            else:
                self.add(wins)
            self.image = Restart_button.image
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x, self.rect.y = x, y

    def update(self, pos):
        if self.rect.collidepoint(pos):
            for elem in all_sprites:
                elem.kill()
            pygame.time.set_timer(MYEVENT1, 0)
            if level == 1:
                level1_do()
            elif level == 2:
                level2_do()
            elif level == 3:
                level3_do()
            elif level == 4:
                level4_do()
            elif level == 5:
                level5_do()
            elif level == 6:
                level6_do()
            elif level == 7:
                level7_do()


class To_menu(pygame.sprite.Sprite):
    image = load_image('to_levels.png', color_key=None)


    def __init__(self, x, y, tf):
        super().__init__(all_sprites)
        if tf:
            self.add(dop_sprites)
        else:
            self.add(wins)
        self.image = To_menu.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self, pos):
        if self.rect.collidepoint(pos):
            for elem in all_sprites:
                elem.kill()
            pygame.time.set_timer(MYEVENT1, 0)
            menu()


class Next_level(pygame.sprite.Sprite):
    image = load_image('next.png', color_key=None)


    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.add(wins)
        self.image = Next_level.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self, pos):
        if self.rect.collidepoint(pos):
            for elem in all_sprites:
                elem.kill()
            if level == 1:
                level2_do()
            elif level == 2:
                level3_do()
            elif level == 3:
                level4_do()
            elif level == 4:
                level5_do()
            elif level == 5:
                level6_do()
            elif level == 6:
                level7_do()


def pause(x, y):
    global text1, cursor, pausee
    cursor.kill()
    running = True
    pausee.image = Pause_button.image1
    rest = Restart_button(x - 100, y, True)
    tolv = To_menu(x - 260, y, True)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    cursor.add(cursors)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == STOP_PAUSE:
                pygame.time.set_timer(STOP_PAUSE, 0)
                pausee.image = Pause_button.image
                cursor.kill()
                cursor = pygame.sprite.Sprite(all_sprites)
                cursor.image = cursor_image
                cursor.rect = cursor_image.get_rect()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                rest.update(pygame.mouse.get_pos())
                pausee.update(pygame.mouse.get_pos())
                tolv.update(pygame.mouse.get_pos())
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        if level != 2:
            pygame.draw.rect(screen, (50, 0, 0), (312.5, 150, 625, 325))
            screen.blit(text1, (420, 236.5))
        elif level == 2:
            pygame.draw.rect(screen, (50, 0, 0), (312.5, 250, 625, 325))
            screen.blit(text1, (420, 336.5))
        cursors.draw(screen)
        pygame.display.flip()
        clock.tick(80)


class Key(pygame.sprite.Sprite):
    image = load_image('yellowkey.png')
    image1 = load_image('greenkey.png')
    image2 = load_image('redkey.png')
    image3 = load_image('bluekey.png')


    def __init__(self, x, y, color):
        super().__init__(all_sprites)
        self.add(keys)
        if color == 'yellow':
            self.image = Key.image
        elif color == 'green':
            self.image = Key.image1
        elif color == 'red':
            self.image = Key.image2
        elif color == 'blue':
            self.image = Key.image3
        self.color = color
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def proverka(self):
        global color, keyr
        if pygame.sprite.spritecollideany(self, knights):
            self.kill()
            keyr.play()
            color = self.color
            pygame.time.set_timer(MYEVENTTYPE, 1)


class Gate(pygame.sprite.Sprite):
    image = load_image('yelget.png', color_key=None)
    image1 = load_image('griget.png', color_key=None)
    image2 = load_image('redget.png', color_key=None)
    image3 = load_image('bluget.png', color_key=None)


    def __init__(self, x , y, color):
        super().__init__(all_sprites)
        self.add(gates)
        if color == 'yellow':
            self.image = Gate.image
        elif color == 'red':
            self.image = Gate.image2
        elif color == 'blue':
            self.image = Gate.image3
        elif color == 'green':
            self.image = Gate.image1
        self.color = color
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y


class Start_button(pygame.sprite.Sprite):
    image = load_image("start.png")


    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Start_button.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self, pos):
        if self.rect.collidepoint(pos):
            self.kill()
            pygame.time.set_timer(MYEVENT3, 1)


class Knight(pygame.sprite.Sprite):
    image = load_image("knight.png")
    image1 = load_image("knight1.png")


    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.add(knights)
        self.image = Knight.image
        self.rect = self.image.get_rect()
        self.xt, self.yt = x, y
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.midleft = x, y
        self.health = 1

    def move(self, napr):
        global motion, level
        if pygame.sprite.spritecollideany(self, vrags):
            self.restart_do()
        if pygame.sprite.spritecollideany(self, gates) or pygame.sprite.spritecollideany(self, blocks):
            napr = 'stop'
            motion = 'stop'
            self.rect.x += 4
            if pygame.sprite.spritecollideany(self, gates) or pygame.sprite.spritecollideany(self, blocks):
                self.rect.x -= 8
                if pygame.sprite.spritecollideany(self, gates) or pygame.sprite.spritecollideany(self, blocks):
                    self.rect.x += 4
                    self.rect.y += 4
                    if pygame.sprite.spritecollideany(self, gates) or pygame.sprite.spritecollideany(self, blocks):
                        self.rect.y -= 8
                        if pygame.sprite.spritecollideany(self, gates) or pygame.sprite.spritecollideany(self, blocks):
                            self.restart_do()
        if napr == 'down':
            self.rect.y += 3
        if napr == 'left':
            self.rect.x -= 3
        if napr == 'right':
            self.rect.x += 3
        if napr == 'up':
            self.rect.y -= 3

    def restart_do(self):
        pygame.time.set_timer(MYEVENT2, 1)


class Grass(pygame.sprite.Sprite):
    image = load_image("grass.png", color_key=None)
    image1 = load_image("grass1.png", color_key=None)
    image2 = load_image("grass2.png", color_key=None)
    image3 = load_image("grass3.png", color_key=None)


    def __init__(self, x, y, z):
        super().__init__(all_sprites)
        self.add(grasss)
        if z == 0:
            self.image = Grass.image
        elif z == 1:
            self.image = Grass.image1
        elif z == 2:
            self.image = Grass.image2
        elif z == 3:
            self.image = Grass.image3
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y


class Block(pygame.sprite.Sprite):
    image = load_image("ограда.png", color_key=None)
    image1 = load_image("ограда1.png", color_key=None)
    image2 = load_image("ограда2.png", color_key=None)
    image3 = load_image("ограда3.png", color_key=None)


    def __init__(self, x, y, z):
        super().__init__(all_sprites)
        self.add(blocks)
        if z == 0:
            self.image = Block.image
        elif z == 1:
            self.image = Block.image1
        elif z == 2:
            self.image = Block.image2
        elif z == 3:
            self.image = Block.image3
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y


class VragHod(pygame.sprite.Sprite):
    image1 = load_image("dragon1.png")
    image2 = load_image("dragon2.png")
    image3 = load_image("dragon3.png")
    image4 = load_image("dragon4.png")


    def __init__(self, hod, z, n):
        super().__init__(all_sprites)
        self.hod = hod
        self.z = z
        self.sled = 1
        self.add(vrags)
        self.add(hoder)
        if z == 2 or z == 4:
            self.image = VragHod.image1
        else:
            self.image = VragHod.image4
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = hod[0]
        self.n = n

    def update(self):
        for i in range(self.n):
            x, y = self.hod[self.sled][0], self.hod[self.sled][1]
            if self.rect.x == x and self.rect.y == y:
                self.sled += 1
                if self.sled == self.z and self.z != 3:
                    self.sled = 0
                if self.z == 3 and self.sled == self.z - 1:
                    self.sled = 0
                if self.z == 2:
                    if self.sled == 0:
                        self.image = VragHod.image2
                    else:
                        self.image = VragHod.image1
                elif self.z == 3:
                    if self.sled == 0:
                        self.image = VragHod.image3
                    else:
                        self.image = VragHod.image4
                else:
                    if self.sled == 0:
                        self.image = VragHod.image4
                    elif self.sled == 1:
                        self.image = VragHod.image1
                    elif self.sled == 2:
                        self.image = VragHod.image3
                    else:
                        self.image = VragHod.image2
                self.rect = self.image.get_rect()
                self.mask = pygame.mask.from_surface(self.image)
                self.rect.x, self.rect.y = x, y
                x, y = self.hod[self.sled][0], self.hod[self.sled][1]
            if x > self.rect.x:
                self.rect.x += 1
            elif x < self.rect.x:
                self.rect.x -= 1
            if y > self.rect.y:
                self.rect.y += 1
            elif y < self.rect.y:
                self.rect.y -= 1


class Vragstrel(pygame.sprite.Sprite):
    image = load_image("cannon.png", color_key=-1)
    image1 = load_image("cannon1.png", color_key=-1)


    def __init__(self, x, y, napr):
        super().__init__(all_sprites)
        self.add(vrags)
        self.napr = napr
        if napr == 'left':
            self.image = Vragstrel.image1
        else:
            self.image = Vragstrel.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self):
        global ball
        if self.napr == 'left':
            ball = Ball(self.rect.x, self.rect.y + 15, self.napr)
        else:
            ball = Ball(self.rect.x + self.image.get_width() - 15, self.rect.y + 15, self.napr)


class Ball(pygame.sprite.Sprite):
    image = load_image("ball.png", color_key=-1)


    def __init__(self, x, y, napr):
        super().__init__(all_sprites)
        self.add(balls)
        self.napr = napr
        self.image = Ball.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self):
        if pygame.sprite.spritecollideany(self, blocks):
            self.kill()
        if pygame.sprite.spritecollideany(self, knights):
            for s in knights:
                s.health -= 1
                if s.health == 0:
                    s.restart_do()
            self.kill()
        if self.napr == 'left':
            self.rect.x -= 2.75
        elif self.napr == 'right':
            self.rect.x += 2.75


class Heartplus(pygame.sprite.Sprite):
    image = load_image("heart.png")


    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Heartplus.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y
        self.give = True

    def update(self):
        if pygame.sprite.spritecollideany(self, knights) and self.give:
            for s in knights:
                s.health += 1
            self.kill()
            self.give = False


class Level_icon(pygame.sprite.Sprite):
    image1 = load_image("first.png", color_key=None)
    image2 = load_image("second.png", color_key=None)
    image3 = load_image("third.png", color_key=None)
    image4 = load_image("fourth.png", color_key=None)
    image5 = load_image("fifth.png", color_key=None)
    image6 = load_image("sixth.png", color_key=None)
    image7 = load_image("seventh.png", color_key=None)
    image8 = load_image("eighth.png", color_key=None)


    def __init__(self, x, y, num):
        super().__init__(all_sprites)
        self.add(levelses)
        self.num = num
        if num == 1:
            self.image = Level_icon.image1
        elif num == 2:
            self.image = Level_icon.image2
        elif num == 3:
            self.image = Level_icon.image3
        elif num == 4:
            self.image = Level_icon.image4
        elif num == 5:
            self.image = Level_icon.image5
        elif num == 6:
            self.image = Level_icon.image6
        elif num == 7:
            self.image = Level_icon.image7
        elif num == 8:
            self.image = Level_icon.image8
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self, pos):
        if self.rect.collidepoint(pos):
            if self.num == 1:
                pygame.time.set_timer(L1, 1)
            elif self.num == 2:
                pygame.time.set_timer(L2, 1)
            elif self.num == 3:
                pygame.time.set_timer(L3, 1)
            elif self.num == 4:
                pygame.time.set_timer(L4, 1)
            elif self.num == 5:
                pygame.time.set_timer(L5, 1)
            elif self.num == 6:
                pygame.time.set_timer(L6, 1)
            elif self.num == 7:
                pygame.time.set_timer(L7, 1)
            elif self.num == 8:
                pygame.time.set_timer(L8, 1)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.add(wins)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Vopr(pygame.sprite.Sprite):
    image = load_image('vopr.png')


    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.add(levelses)
        self.image = Vopr.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = x, y

    def update(self, pos):
        if self.rect.collidepoint(pos):
            for elem in all_sprites:
                elem.kill()
            sho_delat()


def sho_delat():
    global cursor, cursor_image
    tm = To_menu(1130, 90, True)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    font = pygame.font.SysFont('comicsans', 20)
    font1 = pygame.font.SysFont('comicsans', 40)
    s = font1.render('Добро пожаловать в игру "Лабиринт средневековья"', True, pygame.Color('yellow'))
    s1 = font.render('Ваша задача - любой ценой дойти до замка, вы играете за рыцаря,', True, pygame.Color('yellow'))
    s2 = font.render('управлять им вы можете либо стрелками на клавиатуре,', True, pygame.Color('yellow'))
    s3 = font.render('либо клавишами "w", "a", "s", "d" с клавиатуры, так же', True, pygame.Color('yellow'))
    s4 = font.render('вы можете "приседать" зажимая пробел, правда приседать вы', True, pygame.Color('yellow'))
    s5 = font.render('не можете бесконечно, вам будет дано на одно приседание 10 секунд.', True, pygame.Color('yellow'))
    s6 = font.render('Ещё в лабиринте есть монстры: пушки и драконы.', True, pygame.Color('yellow'))
    s7 = font.render('Пушки раз в несколько секунд выстреливают ядрами, которые наносят', True, pygame.Color('yellow'))
    s8 = font.render('1 единицу урона за 1 поподание. Изначально у вас 1 единица здоровья.', True,
                     pygame.Color('yellow'))
    s9 = font.render('Драконы же двигаются по определённой траектории,', True, pygame.Color('yellow'))
    s10 = font.render('При косании героем дракона или пушки уровень начинается сначала.', True, pygame.Color('yellow'))
    s11 = font.render('Чтобы увеличить количество единиц здоровья, собирайте сердечки.', True, pygame.Color('yellow'))
    s12 = font.render('Так же у вас всегда есть возможность остановить уровень,', True, pygame.Color('yellow'))
    s13 = font.render('нажав на иконку паузы на экране, 2 чёрные полосы на жёлтом фоне,', True, pygame.Color('yellow'))
    s14 = font1.render('Желаю вам успехов в прохождении игры!!!', True, pygame.Color('gold'))
    s15 = font.render('и в дальнейшем либо выйти из него, либо начать его сначала, либо продолжить прохождение.', True,
                      pygame.Color('yellow'))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                tm.update(event.pos)
        screen.fill(pygame.Color('black'))
        screen.blit(s, (150, 10))
        screen.blit(s1, (80, 80))
        screen.blit(s2, (80, 110))
        screen.blit(s3, (80, 140))
        screen.blit(s4, (80, 170))
        screen.blit(s5, (80, 200))
        screen.blit(s6, (80, 230))
        screen.blit(s7, (80, 260))
        screen.blit(s8, (80, 290))
        screen.blit(s9, (80, 320))
        screen.blit(s10, (80, 350))
        screen.blit(s11, (80, 380))
        screen.blit(s12, (80, 410))
        screen.blit(s13, (80, 440))
        screen.blit(s15, (80, 470))
        screen.blit(s14, (170, 520))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(80)


def start_game():
    global startbutton, cursor, cursor_image
    startbutton = Start_button(375, 175)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN and startbutton:
                startbutton.update(event.pos)
            if event.type == MYEVENT3:
                pygame.time.set_timer(MYEVENT3, 0)
                for sprite in all_sprites:
                    sprite.kill()
                menu()
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(80)


def menu():
    global level, cursor
    level = 0
    l1, l2 = Level_icon(275, 162.5, 1), Level_icon(475, 162.5, 2)
    l3, l4 = Level_icon(675, 162.5, 3), Level_icon(875, 162.5, 4)
    l5, l6 = Level_icon(375, 362.5, 5), Level_icon(575, 362.5, 6)
    l7 = Level_icon(775, 362.5, 7)
    vopr = Vopr(1150, 0)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                for elem in levelses:
                    elem.update(event.pos)
            if event.type == L1:
                pygame.time.set_timer(L1, 0)
                for elem in all_sprites:
                    elem.kill()
                level1_do()
            if event.type == L2:
                pygame.time.set_timer(L2, 0)
                for elem in all_sprites:
                    elem.kill()
                level2_do()
            if event.type == L3:
                pygame.time.set_timer(L3, 0)
                for elem in all_sprites:
                    elem.kill()
                level3_do()
            if event.type == L4:
                pygame.time.set_timer(L4, 0)
                for elem in all_sprites:
                    elem.kill()
                level4_do()
            if event.type == L5:
                pygame.time.set_timer(L5, 0)
                for elem in all_sprites:
                    elem.kill()
                level5_do()
            if event.type == L6:
                pygame.time.set_timer(L6, 0)
                for elem in all_sprites:
                    elem.kill()
                level6_do()
            if event.type == L7:
                pygame.time.set_timer(L7, 0)
                for elem in all_sprites:
                    elem.kill()
                level7_do()
        screen.fill(pygame.Color('black'))
        pygame.draw.rect(screen, (128, 128, 0), (250, 140, 750, 340))
        pygame.draw.line(screen, (255, 255, 255), (1100, 400), (1200, 120), 5)
        pygame.draw.line(screen, (255, 255, 255), (1200, 120), (1130, 175), 5)
        pygame.draw.line(screen, (255, 255, 255), (1200, 120), (1220, 195), 5)
        pygame.draw.ellipse(screen, (255, 0, 0), (50, 50, 100, 350), 3)
        pygame.draw.arc(screen, pygame.Color('yellow'), (220, 70, 810, 200), 0, 3.14, 3)
        pygame.draw.circle(screen, pygame.Color('green'), (100, 500), 70, 3)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(80)


def level1_do():
    global level, pausee, knight, motion
    global lvs, key1, key2, gate1, gate2, castle, ball, vrag1, color, cursor, cursor_image, pres, key3, gate3, hertpl
    builder(lvs['level1'])
    level = 1
    pres = 2
    knight = Knight(50, 102)
    key1 = Key(60, 520, 'yellow')
    gate1 = Gate(300, 125, 'yellow')
    key2 = Key(310, 300, 'blue')
    gate2 = Gate(625, 250, 'blue')
    castle = Castle(1125, 500)
    key3 = Key(690, 140, 'green')
    gate3 = Gate(1000, 125, 'green')
    ball = None
    pausee = Pause_button(800, 20, True)
    hertpl = Heartplus(410, 170)
    vrag1 = Vragstrel(1000, 500, 'left')
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    motion = 'stop'
    color = None
    pygame.time.set_timer(MYEVENT1, 3450)
    playing()


def level2_do():
    global level, knight, motion, pausee, dragon
    global lvs, key1, gate1, gate2, castle, ball, vrag1, color, cursor, cursor_image, pres, hertpl
    builder(lvs['level2'])
    level = 2
    pres = 3
    knight = Knight(50, 274)
    vrag1 = Vragstrel(50, 503, 'right')
    castle = Castle(50, 400)
    gate1 = Gate(125, 375, 'red')
    gate2 = Gate(1125, 250, 'red')
    key1 = Key(1140, 60, 'red')
    pausee = Pause_button(770, 150, True)
    hertpl = Heartplus(1030, 280)
    dragon = VragHod([(880, 260), (300, 260), (300, 60), (880, 60)], 4, 4)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    motion = 'stop'
    pygame.time.set_timer(MYEVENT1, 4150)
    playing()


def level3_do():
    global level, knight, motion, pausee, dragon
    global lvs, key1, key2, gate1, gate2, castle, ball, vrag1, color, cursor, cursor_image, pres, key3, gate3, hertpl
    builder(lvs['level3'])
    level = 3
    pres = 5
    pausee = Pause_button(650, 20, True)
    hertpl, knight, castle = Heartplus(160, 410), Knight(50, 102), Castle(540, 150)
    gate1, gate2, gate3 = Gate(375, 125, 'yellow'), Gate(437.5, 125, 'red'), Gate(500, 125, 'green')
    key1, key2, key3 = Key(430, 350, 'green'), Key(1020, 510, 'red'), Key(1060, 160, 'yellow')
    vrag1, dragon = Vragstrel(1100, 503, 'left'), VragHod([(1130, 260), (770, 260), (770, 65), (1130, 65)], 4, 3)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    pygame.time.set_timer(MYEVENT1, 4150)
    motion = 'stop'
    playing()


def level4_do():
    global level, knight, motion, castle, hertpl, vrag1, dragon, vrag2, pausee
    global lvs, cursor, cursor_image, pres, key1, key2, key3, gate1, gate2, gate3
    builder(lvs['level4'])
    level = 4
    pres = 4
    knight, castle, hertpl = Knight(1100, 520), Castle(1100, 160), Heartplus(60, 170)
    vrag1, vrag2, = Vragstrel(50, 503, 'right'), Vragstrel(50, 378, 'right')
    dragon, key1 = VragHod([(800, 260), (60, 260), (60, 60), (800, 60)], 4, 4), Key(290, 160, 'red')
    key2, key3, pausee = Key(530, 160, 'green'), Key(290, 510, 'blue'), Pause_button(1150, 40, True)
    gate1, gate2, gate3 = Gate(875, 125, 'red'), Gate(940, 125, 'green'), Gate(1000, 125, 'blue')
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    pygame.time.set_timer(MYEVENT1, 3500)
    motion = 'stop'
    playing()


def level5_do():
    global level, pres, cursor, castle, gate1, gate2, gate3, gate4, cursor_image, pausee
    global knight, motion, hertpl, vrag1, dragon, key1, key2, dragon1, dragon2, key3, key4
    builder(lvs['level5'])
    level = 5
    pres = 4
    key1, key2, key3 = Key(90, 160, 'red'), Key(90, 420, 'yellow'), Key(420, 150, 'green')
    key4, gate1, gate2 = Key(666, 420, 'blue'), Gate(875, 250, 'yellow'), Gate(1100, 250, 'blue')
    gate3, gate4, pausee = Gate(950, 250, 'green'), Gate(1025, 250, 'red'), Pause_button(1150, 520, True)
    knight, castle, hertpl = Knight(1130, 102), Castle(1130, 280), Heartplus(410, 290)
    vrag1, dragon = Vragstrel(70, 280, 'right'), VragHod([(800, 510), (60, 510), (60, 60), (800, 60)], 4, 4)
    dragon1, dragon2 = VragHod([(270, 70), (270, 480)], 3, 2), VragHod([(520, 70), (520, 480)], 3, 3)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    pygame.time.set_timer(MYEVENT1, 5000)
    motion = 'stop'
    playing()


def level6_do():
    global level, pres, motion, knight, castle, dragon, vrag1, dragon1
    global cursor_image, cursor, pausee
    builder(lvs['level6'])
    level = 6
    pres = 5
    vrag1, dragon = Vragstrel(70, 150, 'right'), VragHod([(780, 420), (530, 420), (530, 170), (780, 170)], 4, 3)
    castle, knight, dragon1 = Castle(1000, 500), Knight(270, 520), VragHod([(1100, 420), (70, 420)], 2, 4)
    pausee = Pause_button(280, 30, True)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    pygame.time.set_timer(MYEVENT1, 1000)
    motion = 'stop'
    playing()


def level7_do():
    global level, lvs
    builder(lvs['level7'])
    level = 7
    win()


def playing():
    global level, pausee, knight, motion, key4, gate4, vrag2, pres, dragon, pre0, pre1, pre2, pre3, pre4, pre5, giz1
    global key1, key2, gate1, gate2, castle, ball, vrag1, color, cursor, cursor_image, pres, key3, gate3, hertpl, giz2
    global giz3, vst0, vst1, vst2, vst3, vst4, vst5, vst6, vst7, vst8, vst9, dragon1, dragon2, osh, osh1, osh2, osh3
    global osh4, ot
    tres = False
    nepres = True
    secs = 10
    cursor.add(curs)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    motion = 'down'
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    motion = 'up'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    motion = 'left'
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    motion = 'right'
                if event.key == pygame.K_SPACE and pres > 0:
                    x, y = knight.rect.x, knight.rect.y
                    knight.image = Knight.image1
                    knight.mask = pygame.mask.from_surface(Knight.image1)
                    knight.rect = knight.image.get_rect()
                    knight.rect.bottomleft = x, y + 102
                    tres = True
                    nepres = False
                    pygame.time.set_timer(SECOND, 1000)
                    pygame.time.set_timer(UP, 10000)
                    ot.play()
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT,
                                 pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                    motion = 'stop'
                if event.key == pygame.K_SPACE and pres > 0 and tres:
                    pygame.time.set_timer(UP, 0)
                    nepres = True
                    secs = 10
                    x, y = knight.rect.x, knight.rect.y
                    knight.image = Knight.image
                    knight.mask = pygame.mask.from_surface(Knight.image)
                    knight.rect = knight.image.get_rect()
                    knight.rect.topleft = x, y - 62
                    pres -= 1
                    tres = True
                    ot.stop()
            if event.type == SECOND:
                secs -= 1
            if event.type == MYEVENTTYPE:
                pygame.time.set_timer(MYEVENTTYPE, 0)
                for sprite in gates:
                    if sprite.color == color:
                        sprite.kill()
                color = None
            if event.type == MYEVENT1:
                for sprite in vrags:
                    sprite.update()
            if event.type == MYEVENT2:
                x, y = knight.rect.x, knight.rect.y
                knight.image = Knight.image
                knight.mask = pygame.mask.from_surface(Knight.image)
                knight.rect = knight.image.get_rect()
                knight.rect.topleft = x, y - 62
                pygame.time.set_timer(MYEVENT2, 0)
                for sprite in all_sprites:
                    sprite.kill()
                if level == 1:
                    level1_do()
                elif level == 2:
                    level2_do()
                elif level == 3:
                    level3_do()
                elif level == 4:
                    level4_do()
                elif level == 5:
                    level5_do()
                elif level == 6:
                    level6_do()
                elif level == 7:
                    level7_do()
            if event.type == UP:
                x, y = knight.rect.x, knight.rect.y
                knight.image = Knight.image
                nepres = True
                secs = 10
                knight.mask = pygame.mask.from_surface(Knight.image)
                knight.rect = knight.image.get_rect()
                knight.rect.topleft = x, y - 62
                pres -= 1
                tres = False
                pygame.time.set_timer(UP, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pausee.update(event.pos)
        for sprite in keys:
            sprite.proverka()
        for sprite in balls:
            sprite.update()
        castle.update()
        for elem in hoder:
            elem.update()
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        if level < 6:
            hertpl.update()
        knight.move(motion)
        if not nepres:
            if secs == 10:
                screen.blit(vst9, (140, 577))
            elif secs == 9:
                screen.blit(vst8, (140, 577))
            elif secs == 8:
                screen.blit(vst7, (140, 577))
            elif secs == 7:
                screen.blit(vst6, (140, 577))
            elif secs == 6:
                screen.blit(vst5, (140, 577))
            elif secs == 5:
                screen.blit(vst4, (140, 577))
            elif secs == 4:
                screen.blit(vst3, (140, 577))
            elif secs == 3:
                screen.blit(vst2, (140, 577))
            elif secs == 2:
                screen.blit(vst1, (140, 577))
            elif secs == 1:
                screen.blit(vst0, (140, 577))
        if nepres:
            secs = 10
            if pres == 5:
                screen.blit(pre5, (140, 577))
            if pres == 4:
                screen.blit(pre4, (140, 577))
            if pres == 3:
                screen.blit(pre3, (140, 577))
            if pres == 2:
                screen.blit(pre2, (140, 577))
            if pres == 1:
                screen.blit(pre1, (140, 577))
            if pres == 0:
                screen.blit(pre0, (140, 577))
        if knight.health == 1:
            screen.blit(giz1, (600, 577))
        if knight.health == 2:
            screen.blit(giz2, (600, 577))
        if knight.health == 3:
            screen.blit(giz3, (600, 577))
        curs.draw(screen)
        pygame.display.flip()
        clock.tick(80)


def win():
    global level, text2, cursor, ups, ups1, ups2
    cursor.kill()
    a = 0
    rest = Restart_button(800, 400, False)
    tolv = To_menu(640, 400, False)
    drag = AnimatedSprite(load_image("dragon_sheet8x21.png"), 8, 2, 330, 300)
    if level < 7:
        nextlvl = Next_level(900, 400)
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor_image.get_rect()
    cursor.add(wins)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                rest.update(event.pos)
                tolv.update(event.pos)
                if level < 7:
                    nextlvl.update(event.pos)
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)
        if a == 10:
            drag.update()
            a = 0
        a += 1
        if level == 7:
            pygame.draw.rect(screen, (128, 0, 0), [50, 50, 1150, 525])
            screen.blit(ups, (100, 100))
            screen.blit(ups1, (100, 150))
            screen.blit(ups2, (100, 200))
        else:
            pygame.draw.polygon(screen, (170, 0, 0), ((200, 100), (1050, 100), (1050, 525), (200, 525)))
            screen.blit(text2, (250, 150))
        wins.draw(screen)
        pygame.display.flip()
        clock.tick(80)


start_game()