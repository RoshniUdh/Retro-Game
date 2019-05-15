from settings import *

class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self) 
        self.game = game     
        self.swing = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.angle = -20
        self.image = self.swing_frames[self.current_frame]
        self.image = pygame.transform.scale(self.image, (11, 80))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH_LVL1 / 1.58)
        self.rect.y = (SCREEN_HEIGHT_LVL1 / 1.77)
        
    def load_images(self):
        self.swing_frames = [self.game.spritesheet.get_image(125, 308, 7, 43), 
                             self.game.spritesheet.get_image(43, 584, 35, 35), 
                             self.game.spritesheet.get_image(79, 432, 43, 14), 
                             self.game.spritesheet.get_image(79, 532, 40, 29), 
                             self.game.spritesheet.get_image(201, 85, 43, 21), 
                             self.game.spritesheet.get_image(79, 506, 42, 24),  
                             self.game.spritesheet.get_image(79, 448, 42, 27), 
                             self.game.spritesheet.get_image(201, 108, 43, 17)]
        for frame in self.swing_frames:
            frame.set_colorkey(BLACK)

    def update(self):
        self.keystate = pygame.key.get_pressed()
        if self.keystate[pygame.K_SPACE]:
            self.swing = True
        if self.swing == True and self.angle < 270:
            self.animate()
        if self.keystate[pygame.K_RETURN]:
            if self.angle == 270:
                self.angle = -20
                self.image = self.swing_frames[0]
                self.image = pygame.transform.scale(self.image, (11, 80))
                self.image = pygame.transform.rotate(self.image, self.angle)
                self.rect = self.image.get_rect() 
                self.rect.x = (SCREEN_WIDTH_LVL1 / 1.58)
                self.rect.y = (SCREEN_HEIGHT_LVL1 / 1.77)
                self.swing = False

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 30:
            self.last_update = now
            #self.current_frame = (self.current_frame + 1) % len(self.swing_frames)
            self.image = self.swing_frames[self.current_frame]
            self.image = pygame.transform.scale(self.image, (11, 80))
            self.angle += 10
            #self.angle %= 270
            self.image = pygame.transform.rotate(self.image, self.angle)
                
            if self.angle == -10:
                self.rect.centerx += 13
            if self.angle == 0:
                self.rect.centerx += 12
            elif self.angle == 10:
                self.rect.centerx += 0
            elif self.angle == 20:
                self.rect.centery -= 2
            elif self.angle == 30:
                self.rect.centery -= 1
            elif self.angle == 100:
                self.rect.centery -= 13
            elif self.angle == 110:
                self.rect.centery -= 13
            elif self.angle == 120:
                self.rect.centery -= 10
            elif self.angle == 130:
                self.rect.centery -= 11
            elif self.angle == 140:
                self.rect.centery -= 11
            elif self.angle == 150:
                self.rect.centery -= 5
            elif self.angle == 160:
                self.rect.centery -= 5
            elif self.angle == 170:
                self.rect.centery -= 2
            elif self.angle == 190:
                self.rect.centerx -= 13
                self.rect.centery += 0
            elif self.angle == 200:
                self.rect.centerx -= 13
                self.rect.centery += 3
            elif self.angle == 210:
                self.rect.centerx -= 11
                self.rect.centery += 5
            elif self.angle == 220:
                self.rect.centerx -= 10
                self.rect.centery += 6
            elif self.angle == 230:
                self.rect.centerx -= 10
                self.rect.centery += 10
            elif self.angle == 240:
                self.rect.centerx -= 6
                self.rect.centery += 10
            elif self.angle == 250:
                self.rect.centerx -= 3
                self.rect.centery += 12
            elif self.angle == 260:
                self.rect.centerx -= 7
                self.rect.centery += 12
            elif self.angle == 270:
                self.rect.centerx += 2
                self.rect.centery += 13

class Pitcher(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.throws = False
        self.single_throw = 0
        self.current_frame = 0
        self.last_update = 0
        self.load_images()      
        self.image = self.throw_frames[1]
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH_LVL1 / 3.43)
        self.rect.y = (SCREEN_HEIGHT_LVL1 / 2.10)
        
    def load_images(self):
        self.throw_frames = [self.game.spritesheet.get_image(80, 580, 30, 35),
                             self.game.spritesheet.get_image(43, 510, 34, 35),
                             self.game.spritesheet.get_image(843, 547, 34, 35),
                             self.game.spritesheet.get_image(112, 580, 33, 33),
                             self.game.spritesheet.get_image(1, 510, 40, 31),
                             self.game.spritesheet.get_image(1, 543, 40, 31),
                             self.game.spritesheet.get_image(147, 580, 27, 33),
                             self.game.spritesheet.get_image(176, 580, 27, 33),
                             self.game.spritesheet.get_image(205, 580, 20, 33),
                             self.game.spritesheet.get_image(79, 477, 42, 27),
                             self.game.spritesheet.get_image(190, 551, 29, 27)]
        for frame in self.throw_frames:
            frame.set_colorkey(BLACK)
    
    def update(self):
        self.keystate = pygame.key.get_pressed()
        if self.keystate[pygame.K_RETURN]:
            self.throws = True
        elif self.throws == True and self.single_throw < 12:
            self.animate()
        elif self.single_throw == 12:
            self.current_frame = 0
            self.single_throw = 0
            self.throws = False

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 150:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.throw_frames)
            self.image = self.throw_frames[self.current_frame]
            self.single_throw += 1

class Ball(pygame.sprite.Sprite):
    def __init__(self, game, image_dir):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.ball_thrown = False
        self.counter = 0
        self.image = pygame.image.load(path.join(image_dir, FILENAME_BALL)).convert()     
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH_LVL1 / 3.36)
        self.rect.y = (SCREEN_HEIGHT_LVL1 / 2.08)
        self.speedx = 10
    
    def update(self):
        self.animate()
        self.keystate = pygame.key.get_pressed()
        if self.keystate[pygame.K_RETURN]:
            if self.game.check_counter < 2:
                self.ball_thrown = True
            elif self.game.check_counter == 2:
                self.ball_thrown = False
                self.game.check_counter = 0
                #self.game.all_sprites.remove(self.game.health_bar3)
                #self.game.all_sprites.add(self.game.health_bar1)
                self.game.game_ended = True
        
    def animate(self):
        if self.ball_thrown == True:
            if self.counter != 50:
                self.counter += 1
            elif self.counter == 50:
                self.rect.x += self.speedx
            if self.rect.x > SCREEN_WIDTH_LVL1 + 175:
                self.game.all_sprites.remove(self.game.homerun_message)
                self.game.all_sprites.remove(self.game.strike_message)
                self.game.homerun = False
                self.rect.x = (SCREEN_WIDTH_LVL1 / 3.36)
                self.rect.y = (SCREEN_HEIGHT_LVL1 / 2.08)
                self.speedx = random.randint(10,30)                
                self.counter = 0
                self.ball_thrown = False

class Message(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(x, y, width, height)
        self.rect = self.image.get_rect()
        self.rect.x = 535
        self.rect.y = 20

class Check(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class HP(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(221, 368, 27, 66)
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 200

class HP2(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(123, 455, 66, 27)
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 200

class HP3(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(123, 484, 66, 27)
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 200