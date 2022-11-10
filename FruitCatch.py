"""
All sound and images are from opengameart.org.
Credit to the creators
"""

# make sure that the ttf file is in the same folder as this file for the code to run
# make sure that the img and snd folders are in the same folder as this file for the code to run
# pygame may also need to be installed

import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), "img")
snd_dir = path.join(path.dirname(__file__), "snd")

# Dimensions for window
WIDTH = 900
HEIGHT = 700
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (165, 42, 42)
ORANGE = (255, 165, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Catch!")
clock = pygame.time.Clock()
# start_time = 30
frame_count = 0
frame_rate = 60

# Load all game graphics
background = pygame.image.load(path.join(img_dir, "sky1.png")).convert()
background_rect = background.get_rect()
bX = 0
bX2 = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "bowl.png")).convert()
apple_image = pygame.image.load(path.join(img_dir, "apple.png")).convert()
banana_image = pygame.image.load(path.join(img_dir, "banana.png")).convert()
cherry_image = pygame.image.load(path.join(img_dir, "cherry.png")).convert()
grape_image = pygame.image.load(path.join(img_dir, "grape.png")).convert()
kiwi_image = pygame.image.load(path.join(img_dir, "kiwi.png")).convert()
orange_image = pygame.image.load(path.join(img_dir, "orange.png")).convert()
strawberry_image = pygame.image.load(path.join(img_dir, "strawberry.png")).convert()
watermelon_image = pygame.image.load(path.join(img_dir, "watermelon.png")).convert()
cookie_image = pygame.image.load(path.join(img_dir, "cookie.png")).convert()

# load all game sounds
pygame.mixer_music.load(path.join(snd_dir, "Orbit.wav"))
fruit_catch = pygame.mixer.Sound(path.join(snd_dir, "completetask_0.wav"))

# plays the background music on repeat
pygame.mixer.music.play(loops=-1)


# Creates the player
class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (95, 50))
        self.rect = self.image.get_rect()
        self.radius = 23
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


# creates the apple
class Apple(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(apple_image, (55, 40))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .7 / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 2
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 2


# creates the banana
class Banana(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(banana_image, (70, 80))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 3
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 3


# creates the cherry
class Watermelon(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(watermelon_image, (65, 75))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 4
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 4


# creates the grape
class Grape(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(grape_image, (65, 70))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 5
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 5


# creates the kiwi
class Kiwi(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(kiwi_image, (65, 50))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 6
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 6


# creates the orange
class Orange(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(orange_image, (50, 55))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 7
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 7


# creates the strawberry
class Strawberry(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(strawberry_image, (45, 40))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 8
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 8


# creates the cherry
class Cherry(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(cherry_image, (45, 40))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 9
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 9


# creates the cookie
class Cookie(pygame.sprite.Sprite):
    # sprite for the fruit
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(cookie_image, (50, 50))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image_orig, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speedy = 10
        self.rot = 0
        self.rot_speed = 3
        self.last_update = pygame.time.get_ticks()

    # makes the sprite rotate
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -10)
            self.speedy = 10


# Creates a function for drawing the text
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('FFFFORWA.ttf', size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def main_menu():
    screen.blit(background, background_rect)
    draw_text(screen, "Fruit Catch!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Collect all the fruit within the time limit.", 24,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "The faster the falling fruit the better the score!", 24, WIDTH / 2, HEIGHT * .6)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * .75)
    draw_text(screen, "Made by: Buttur Games", 10, WIDTH / 10, HEIGHT * .97)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def end_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Finish!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Your Score: " + str(score), 24, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press T to try again", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    waiting = False


def draw_timer(surf, text, size, x, y):
    font = pygame.font.Font('FFFFORWA.ttf', size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def paused():
    pass


def new_apple():
    a = Apple()
    all_sprites.add(a)
    apples.add(a)


def new_banana():
    b = Banana()
    all_sprites.add(b)
    bananas.add(b)


def new_cherry():
    ch = Cherry()
    all_sprites.add(ch)
    cherries.add(ch)


def new_grape():
    g = Grape()
    all_sprites.add(g)
    grapes.add(g)


def new_kiwi():
    k = Kiwi()
    all_sprites.add(k)
    kiwis.add(k)


def new_orange():
    o = Orange()
    all_sprites.add(o)
    oranges.add(o)


def new_strawberry():
    s = Strawberry()
    all_sprites.add(s)
    strawberries.add(s)


def new_watermelon():
    w = Watermelon()
    all_sprites.add(w)
    watermelons.add(w)


def new_cookie():
    c = Cookie()
    all_sprites.add(c)
    cookies.add(c)


class PlayerScore(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite__init__(self)


# Don't think I need this
'''
# Creates instance of each object
all_sprites = pygame.sprite.Group()
apples = pygame.sprite.Group()
bananas = pygame.sprite.Group()
cherries = pygame.sprite.Group()
grapes = pygame.sprite.Group()
kiwis = pygame.sprite.Group()
oranges = pygame.sprite.Group()
strawberries = pygame.sprite.Group()
watermelons = pygame.sprite.Group()
cookies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
'''

# Game loop
game_over = True
running = True
counter, text = 30, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
while running:
    if game_over:
        main_menu()
        game_over = False
        all_sprites = pygame.sprite.Group()
        apples = pygame.sprite.Group()
        bananas = pygame.sprite.Group()
        cherries = pygame.sprite.Group()
        grapes = pygame.sprite.Group()
        kiwis = pygame.sprite.Group()
        oranges = pygame.sprite.Group()
        strawberries = pygame.sprite.Group()
        watermelons = pygame.sprite.Group()
        cookies = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        new_apple()
        new_banana()
        new_cherry()
        new_grape()
        new_kiwi()
        new_orange()
        new_strawberry()
        new_watermelon()
        new_cookie()
        counter = 30
        score = 0

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # countdown timer
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3)
        if counter == 0:
            end_screen()
            all_sprites = pygame.sprite.Group()
            apples = pygame.sprite.Group()
            bananas = pygame.sprite.Group()
            cherries = pygame.sprite.Group()
            grapes = pygame.sprite.Group()
            kiwis = pygame.sprite.Group()
            oranges = pygame.sprite.Group()
            strawberries = pygame.sprite.Group()
            watermelons = pygame.sprite.Group()
            cookies = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            new_apple()
            new_banana()
            new_cherry()
            new_grape()
            new_kiwi()
            new_orange()
            new_strawberry()
            new_watermelon()
            new_cookie()
            counter = 30
            score = 0
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # check to see if a apple hit a player
    hits = pygame.sprite.spritecollide(player, apples, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 5
        fruit_catch.play()
        new_apple()

    # check to see if a banana hit a player
    hits = pygame.sprite.spritecollide(player, bananas, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 10
        fruit_catch.play()
        new_banana()

    # check to see if a cherry hit a player
    hits = pygame.sprite.spritecollide(player, cherries, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 15
        fruit_catch.play()
        new_cherry()

    # check to see if a grape hit a player
    hits = pygame.sprite.spritecollide(player, grapes, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 20
        fruit_catch.play()
        new_grape()

    # check to see if a kiwi hit a player
    hits = pygame.sprite.spritecollide(player, kiwis, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 25
        fruit_catch.play()
        new_kiwi()

    # check to see if a kiwi hit a player
    hits = pygame.sprite.spritecollide(player, oranges, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 30
        fruit_catch.play()
        new_orange()

    # check to see if a kiwi hit a player
    hits = pygame.sprite.spritecollide(player, strawberries, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 35
        fruit_catch.play()
        new_strawberry()

    # check to see if a watermelon hit a player
    hits = pygame.sprite.spritecollide(player, watermelons, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 40
        fruit_catch.play()
        new_watermelon()

    # check to see if a cookie hit a player
    hits = pygame.sprite.spritecollide(player, cookies, True, pygame.sprite.collide_circle)
    for hit in hits:
        score += 45
        # draw_text(screen, "+45", 18, WIDTH * .65, 10)
        fruit_catch.play()
        new_cookie()

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, 'Score: ' + str(score), 18, WIDTH / 2, 10)
    draw_timer(screen, 'Time: ' + str(int(counter)), 18, WIDTH / 16, 10)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
