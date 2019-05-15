import pygame
import sys
from pygame.locals import *
import time
import random
from os import path
from homerun_sprites import * 
from settings import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60 #speed of game
WIDTH = 480
HEIGHT = 600
FPS = 60 #speed of game
 
#screen.blit(background, background_rect)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() #track the time
def draw_text(surf, text, size, x, y):
        font_name = pygame.font.match_font('calibri')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x , y)
        surf.blit(text_surface, text_rect)

def render_multi_line(screen, text,font, WIDTH, HEIGHT):
            line = text.splitlines()
            for i, l in enumerate (line):
                draw_text(screen, l,25, WIDTH/2 , (HEIGHT/3) * i)

def level1():
    import pygame
    import random
    from os import path

    TITLE = "Homerun"
    FONT = "fonts\\prstart.ttf"
    FPS = 60

    DIR = path.dirname(__file__)
    IMAGE_DIR = path.join(DIR, 'images')
    SOUND_DIR = path.join(DIR, 'sound')

    FILENAME_START_SCREEN = "start_screen.png"
    FILENAME_INSTRUCTIONS_SCREEN = "instructiescherm_homerun.png"
    FILENAME_GAME_OVER_SCREEN = "gameover_homerun.png"
    FILENAME_HIGHSCORE = "highscore.txt"

    FILENAME_MUSIC = "spaceship.wav"
    FILENAME_BACKGROUND = "black_background.png"
    FILENAME_SPRITESHEET = "spritesheet.png"
    FILENAME_BALL = "Naamloos2.ico"

    SCREEN_WIDTH_LVL0 = 480
    SCREEN_HEIGHT_LVL0 = 600
    SCREEN_WIDTH_LVL1 = 1280
    SCREEN_HEIGHT_LVL1 = 720
    SCREEN_WIDTH_LVL2 = 640
    SCREEN_HEIGHT_LVL2 = 480
    SCREEN_WIDTH_LVL3 = 480
    SCREEN_HEIGHT_LVL3 = 600
    SCREEN_WIDTH_LVL4 = 1024
    SCREEN_HEIGHT_LVL4 = 695
    SCREEN_WIDTH_LVL5 = 640
    SCREEN_HEIGHT_LVL5 = 480
    SCREEN_WIDTH_LVL6 = 600
    SCREEN_HEIGHT_LVL6 = 500
    SCREEN_SIZE   = 640,480

    #             R    G    B
    WHITE     = (255, 255, 255)
    BLACK     = (  0,   0,   0)
    RED       = (255,   0,   0)
    GREEN     = (  0, 255,   0)
    BLUE      = (  0,   0, 255)
    PURPLE    = (255,   0, 255)
    DARKGREEN = (  0, 155,   0)
    DARKGRAY  = ( 40,  40,  40)

    # Object dimensions
    BRICK_WIDTH   = 60
    BRICK_HEIGHT  = 15
    PADDLE_WIDTH  = 60
    PADDLE_HEIGHT = 12
    BALL_DIAMETER = 16
    BALL_RADIUS   = BALL_DIAMETER / 2

    MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
    MAX_BALL_X   = SCREEN_SIZE[0] - BALL_DIAMETER
    MAX_BALL_Y   = SCREEN_SIZE[1] - BALL_DIAMETER

    # Paddle Y coordinate
    PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10

    # State constants
    STATE_BALL_IN_PADDLE = 0
    STATE_PLAYING = 1
    STATE_WON = 2
    STATE_GAME_OVER = 3

    class StartGame:
        def __init__(self):
            pygame.init()
            pygame.mixer.init()
            pygame.display.set_caption(TITLE)
            self.screen = pygame.display.set_mode((1280, 720))
            self.load_data()
            self.update()
            self.game = Game()

        def load_data(self):
            dir = path.dirname(__file__)
            image_dir = path.join(dir, 'images')

            self.start_screen = pygame.image.load(path.join(image_dir, FILENAME_START_SCREEN)).convert()
            self.start_screen_rect = self.start_screen.get_rect()

            self.instructions_screen = pygame.image.load(path.join(image_dir, FILENAME_INSTRUCTIONS_SCREEN)).convert()
            self.instructions_screen_rect = self.instructions_screen.get_rect()

        def update(self):
            self.active_screen = 1
            self.game_active = True
            while self.game_active == True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RETURN:
                            print('switching screens..')
                            if self.active_screen < 3:
                                self.active_screen += 1

                if self.active_screen == 1:
                    self.screen.blit(self.start_screen, self.start_screen_rect)
                if self.active_screen == 2:
                    self.screen.blit(self.instructions_screen, self.instructions_screen_rect)
                if self.active_screen == 3:
                    self.game_active = False

                pygame.display.update()

    class Game:
        def __init__(self):
            self.clock = pygame.time.Clock()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH_LVL1,SCREEN_HEIGHT_LVL1))
            self.load_data()

    # Load all game graphics
        def load_data(self):
            self.dir = path.dirname(__file__)
            self.image_dir = path.join(self.dir, 'images')
            self.sound_dir = path.join(self.dir, 'sound')

            with open(path.join(self.dir, FILENAME_HIGHSCORE), 'r') as f:
                try:
                    self.highscore = int(f.read(), r)
                except:
                    self.highscore = 0

    # Load spritesheet image
            self.spritesheet = Spritesheet(path.join(self.image_dir, FILENAME_SPRITESHEET))

    # Load and play music
            pygame.mixer.music.load(path.join(self.sound_dir, FILENAME_MUSIC))
            pygame.mixer.music.play(-1, 0.0)

     # Load background
            self.background = pygame.image.load(path.join(self.image_dir, FILENAME_BACKGROUND)).convert()
            self.background_rect = self.background.get_rect()

    # Game over screen
            self.game_over_screen = pygame.image.load(path.join(self.image_dir, FILENAME_GAME_OVER_SCREEN)).convert()
            self.game_over_rect = self.game_over_screen.get_rect()
 
    # Start a new game
        def new(self):   
            self.player = pygame.sprite.Group()
            self.pitcher = pygame.sprite.Group()
            self.ball = pygame.sprite.Group()
            self.check = pygame.sprite.Group()
            self.message = pygame.sprite.Group()
            self.health_bar1 = pygame.sprite.Group()
            self.health_bar2 = pygame.sprite.Group()
            self.health_bar3 = pygame.sprite.Group()
            self.all_sprites = pygame.sprite.Group()
        
            self.player.add(Player(self))
            self.pitcher = Pitcher(self)
            self.ball = Ball(self, self.image_dir)
            self.check.add(Check(900, 310, 60, 90))
            self.health_bar1 = HP(self)
            self.health_bar2 = HP2(self)
            self.health_bar3 = HP3(self)
        
            self.all_sprites.add(self.pitcher, self.player, self.ball, self.message, self.check, self.health_bar1)

            self.homerun_message = Message(self, 1, 1, 243, 40)
            self.strike_message = Message(self, 1, 85, 198, 40)

            self.running = False
            self.homerun = False
            self.game_ended = False
            self.game_over = False
            self.end_game_incremental = 0
            self.check_counter = 0
            self.score = 0
            self.run()

        def run(self):
            self.playing = True
            while self.playing:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()

    # Game loop - events
        def events(self):  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.playing == True:
                        self.playing = False
                        self.running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        if self.ball.ball_thrown == True:
                            self.check_counter += 1
                            if self.game_over == True and self.end_game_incremental > 45:
                                print('finished!')
                                self.new()                            
    # Game loop -  update
        def update(self):
            self.all_sprites.update()

            self.hits_check = pygame.sprite.spritecollide(self.ball, self.check, False)
            if self.hits_check:
                if self.homerun == False and self.check_counter == 1:
                    self.all_sprites.add(self.strike_message)
                    self.all_sprites.remove(self.health_bar1)
                    self.all_sprites.add(self.health_bar2)
                elif self.homerun == False and self.check_counter == 2:
                    self.all_sprites.add(self.strike_message)
                    self.all_sprites.remove(self.health_bar2)
                    self.all_sprites.add(self.health_bar3)
            hits_bat = pygame.sprite.spritecollide(self.ball, self.player, False)
            if hits_bat:
                self.homerun = True
                if self.homerun == True:
                    self.ball.rect.x += 500
                    self.all_sprites.add(self.homerun_message)
                    self.all_sprites.add(self.health_bar1)
                    self.all_sprites.remove(self.health_bar2)
                    self.all_sprites.remove(self.health_bar3)
                    self.check_counter = 0
                    self.score += 1

    # Game loop - draw
        def draw(self):
            self.screen.blit(self.background, self.background_rect)
            self.all_sprites.draw(self.screen)

            self.draw_text("Score: " + str(self.score), 22, WHITE, 95, 10)
        
            if self.game_ended == True:
                self.show_go_screen()
                self.end_game_incremental += 1

            pygame.display.update()

        def draw_text(self, text, size, color, x, y):
            font = pygame.font.Font(FONT, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            self.screen.blit(text_surface, text_rect)

        
        #def show_start_screen(self):
        #    # game splash/start screen
        #    self.screen.fill(BLACK)
        #    self.draw_text(TITLE, 48, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        #    self.draw_text("Arrows to move, Space to jump", 22, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        #    self.draw_text("Press a key to play", 22, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        #    self.draw_text("High Score: " + str(self.highscore), 22, RED, SCREEN_WIDTH / 2, 15)
        #    pygame.display.update()

        def show_go_screen(self):
            self.game_over = True
            self.screen.fill(BLACK)
            self.draw_text("GAME OVER", 48, WHITE, SCREEN_WIDTH_LVL1 / 2, SCREEN_HEIGHT_LVL1 / 4)
            self.draw_text("Score: " + str(self.score), 22, WHITE, SCREEN_WIDTH_LVL1 / 2, SCREEN_HEIGHT_LVL1 / 2)
            show_level2_screen()
            self.draw_text("Press R to try again", 22, WHITE, SCREEN_WIDTH_LVL1 / 2, SCREEN_HEIGHT_LVL1 * 3 / 4)
            self.draw_text("Press ENTER to continue to the next level", 22, WHITE, SCREEN_WIDTH_LVL1 / 2, 630)
            if self.score > self.highscore:
                self.highscore = self.score
                self.draw_text("NEW HIGH SCORE!", 22, WHITE, SCREEN_WIDTH_LVL1 / 2, SCREEN_HEIGHT_LVL1 / 2 + 40)
                with open(path.join(DIR, FILENAME_HIGHSCORE), 'w') as f:
                    f.write(str(self.score))
            else:
                self.draw_text("High Score: " + str(self.highscore), 22, WHITE, SCREEN_WIDTH_LVL1 / 2, SCREEN_HEIGHT_LVL1 / 2 + 40)

    startGame = StartGame()
    game = Game()

    while startGame.game_active == False:
        #game.running = True
        game.new()

    pygame.quit()
#class Goingretro:
def level2():    
    import sys
    import pygame


    SCREEN_SIZE   = 640,480



    # Object dimensions
    BRICK_WIDTH   = 60
    BRICK_HEIGHT  = 15
    PADDLE_WIDTH  = 60
    PADDLE_HEIGHT = 12
    BALL_DIAMETER = 16
    BALL_RADIUS   = BALL_DIAMETER / 2

    MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
    MAX_BALL_X   = SCREEN_SIZE[0] - BALL_DIAMETER
    MAX_BALL_Y   = SCREEN_SIZE[1] - BALL_DIAMETER

    # Paddle Y coordinate
    PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10

# Color constants
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    BLUE  = (255,255,255)
    BRICK_COLOR = (255,255,255)

# State constants
    STATE_BALL_IN_PADDLE = 0
    STATE_PLAYING = 1
    STATE_WON = 2
    STATE_GAME_OVER = 3


    class Bricka:

        def __init__(self):
        
            pygame.init()

            pygame.mixer.init()
            pygame.mixer.music.load("spaceship.wav")


       
        
            self.screen = pygame.display.set_mode(SCREEN_SIZE)
            pygame.display.set_caption("Brick Breaker Version 1.0")
        
            self.clock = pygame.time.Clock()

            if pygame.font:
                self.font = pygame.font.Font(None,30)
            else:
                self.font = None

            self.init_game()
        
        

        
    
        def init_game(self):
        
            self.lives = 3
            self.score = 0
            self.state = STATE_BALL_IN_PADDLE

            self.paddle   = pygame.Rect(300,PADDLE_Y,PADDLE_WIDTH,PADDLE_HEIGHT)
            self.ball     = pygame.Rect(300,PADDLE_Y - BALL_DIAMETER,BALL_DIAMETER,BALL_DIAMETER)

            self.ball_vel = [5,-5]

            self.create_bricks()
            pygame.mixer.music.play()

        def create_bricks(self):
            y_ofs = 35
            self.bricks = []
            for i in range(7):
                x_ofs = 35
                for j in range(8):
                    self.bricks.append(pygame.Rect(x_ofs,y_ofs,BRICK_WIDTH,BRICK_HEIGHT))
                    x_ofs += BRICK_WIDTH + 10
                y_ofs += BRICK_HEIGHT + 5

        def draw_bricks(self):
            for brick in self.bricks:
                pygame.draw.rect(self.screen, BRICK_COLOR, brick)
        
        def check_input(self):
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_LEFT]:
                self.paddle.left -= 12
                if self.paddle.left < 0:
                    self.paddle.left = 0

            if keys[pygame.K_RIGHT]:
                self.paddle.left += 12
                if self.paddle.left > MAX_PADDLE_X:
                    self.paddle.left = MAX_PADDLE_X

            if keys[pygame.K_SPACE] and self.state == STATE_BALL_IN_PADDLE:
                self.ball_vel = [5,-5]
                self.state = STATE_PLAYING
            elif keys[pygame.K_RETURN] and (self.state == STATE_GAME_OVER or self.state == STATE_WON):
                self.init_game()

        def move_ball(self):
            self.ball.left += self.ball_vel[0]
            self.ball.top  += self.ball_vel[1]

            if self.ball.left <= 0:
                self.ball.left = 0
                self.ball_vel[0] = -self.ball_vel[0]
            elif self.ball.left >= MAX_BALL_X:
                self.ball.left = MAX_BALL_X
                self.ball_vel[0] = -self.ball_vel[0]
        
            if self.ball.top < 0:
                self.ball.top = 0
                self.ball_vel[1] = -self.ball_vel[1]
            elif self.ball.top >= MAX_BALL_Y:            
                self.ball.top = MAX_BALL_Y
                self.ball_vel[1] = -self.ball_vel[1]

        def handle_collisions(self):
            for brick in self.bricks:
                if self.ball.colliderect(brick):
                    self.score += 3
                    self.ball_vel[1] = -self.ball_vel[1]
                    self.bricks.remove(brick)
                    break
            
            if len(self.bricks) == 0:
                self.state = STATE_WON
                time.sleep(3)
                level3()
            
            if self.ball.colliderect(self.paddle):
                self.ball.top = PADDLE_Y - BALL_DIAMETER
                self.ball_vel[1] = -self.ball_vel[1]
            elif self.ball.top > self.paddle.top:
                self.lives -= 1
                if self.lives > 0:
                    self.state = STATE_BALL_IN_PADDLE
                else:
                    self.show_message("Crashed!")
                    pygame.display.flip()
                    self.state = STATE_GAME_OVER
                    if self.state == STATE_GAME_OVER:
                            time.sleep(3)
                            level3()

        def show_stats(self):
            if self.font:
                font_surface = self.font.render("SCORE: " + str(self.score) + " LIVES: " + str(self.lives), False, WHITE)
                self.screen.blit(font_surface, (205,5))

        def getscore1(self):
            return self.score

        def show_message(self,message):
            if self.font:
                size = self.font.size(message)
                font_surface = self.font.render(message,False, WHITE)
                x = (SCREEN_SIZE[0] - size[0]) / 2
                y = (SCREEN_SIZE[1] - size[1]) / 2
                self.screen.blit(font_surface, (x,y))
        
            
        def run(self):
            while 1:            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit

                self.clock.tick(50)
                self.screen.fill(BLACK)
                self.check_input()

                if self.state == STATE_PLAYING:
                    self.move_ball()
                    self.handle_collisions()
                elif self.state == STATE_BALL_IN_PADDLE:
                    self.ball.left = self.paddle.left + self.paddle.width / 2
                    self.ball.top  = self.paddle.top - self.ball.height
                    self.show_message("PRESS SPACE TO LAUNCH THE BALL")
                #elif self.state == STATE_GAME_OVER:
                    #   self.show_message("Crashed!")
                elif self.state == STATE_WON:
                    self.show_message("YOU WON! PRESS ENTER TO PLAY AGAIN")
                
                self.draw_bricks()

                # Draw paddle
                pygame.draw.rect(self.screen, BLUE, self.paddle)

                # Draw ball
                pygame.draw.circle(self.screen, WHITE, (int(self.ball.left + BALL_RADIUS),int(self.ball.top + BALL_RADIUS)),int(BALL_RADIUS))

                self.show_stats()

                pygame.display.flip()
    if __name__ == "__main__":
            Bricka().run()

def level3():
    import pygame, sys
    import random
    import os

    WIDTH = 480
    HEIGHT = 600
    FPS = 60 #speed of game

    #define usefull colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255) 

    #set up assets:art and sound
    game_folder = os.path.dirname(__file__) #our project
    img_folder = os.path.join(game_folder, "img")

#initialize pygame and screen
    pygame.init()
    pygame.mixer.init() #soundeffects of game
    pygame.mixer.music.load("spaceship.wav")
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Meteorites fall down")
    clock = pygame.time.Clock() #track the time
    start = 6000 #for 1 minute
    running = True

    def show_go_screen(): 
            #screen.blit(background, background_rect)
            draw_text(screen, "Meteorites fall down", 44, WIDTH /2 , HEIGHT /4)
            draw_text(screen, "Try not to touch the meteorites, with arrow keys", 
                    16, WIDTH /2 , HEIGHT /2)
            draw_text(screen, "Press an arrow key to start", 
                        16, WIDTH /2 , HEIGHT /2 * ( 3/4))
            pygame.display.flip()
            waiting = True
            while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: #first the exit-event
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        waiting = False
# effect, geluid en snelheid
    def show_next_screen(): 
            #screen.blit(background, background_rect)
            draw_text(screen, "Your score was: " + str(score1), 36, WIDTH /2 , HEIGHT /4)
            draw_text(screen, "CRASHED!", 
                    52, WIDTH /2 , HEIGHT /2)
            pygame.display.flip()
            waiting = True
            while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            screen.fill(BLACK)
            show_level4_screen()
            

    def show_win_screen(): 
            #screen.blit(background, background_rect)
            draw_text(screen, "Your score was: " + str(score1), 36, WIDTH /2 , HEIGHT /4)
            draw_text(screen, "YOU WON!", 
                    52, WIDTH /2 , HEIGHT /2)
            pygame.display.flip()
            waiting = True
            while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        waiting = False
            screen.fill(BLACK)
            show_level4_screen()

#define sprite objects
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (50,50)) #give new format
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()

            self.radius = 18
            #####pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.center = (WIDTH / 2, HEIGHT /2)
            self.speedx = 0
            self.speedy = 0

        def update(self):
            self.speedx = 0
            self.speedy = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -5
            if keystate[pygame.K_RIGHT]:
                self.speedx = 5
            if keystate[pygame.K_DOWN]:
                self.speedy = 5
            if keystate[pygame.K_UP]:
                self.speedy = -5
            self.rect.x = self.rect.x + self.speedx 
            self.rect.y = self.rect.y + self.speedy

            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
            if self.rect.top < 0:
                self.rect.top = 0
 
    class Meteorite(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_orig = meteor_img
            self.image_orig.set_colorkey(BLACK)
            self.image_orig = pygame.transform.scale(meteor_img, (50,50)) #give new format
            self.image = self.image_orig.copy()
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width / 2)
            ######pygame.draw.circle(self.image, BLUE, self.rect.center, self.radius)
            self.rect.x = random.randrange(WIDTH - self.rect.width) #it has to come on the screen
            self.rect.y = random.randrange(-100, -40) #minus is above the screen placing
            self.speedy = random.randrange(1, 4) # slow and fast enemies
            self.speedx = random.randrange(-2, 2)
            self.rot = 0
            self.rot_speed = random.randrange(-8, 8) #rotationspeed
            self.last_update = pygame.time.get_ticks()

        def rotate(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > 50:
                self.last_update = now
                self.rot = (self.rot + self.rot_speed) % 360
                self.image = pygame.transform.rotate(self.image_orig, self.rot)
                new_image = pygame.transform.rotate(self.image_orig, self.rot)
                old_center = self.rect.center
                self.image = new_image
                self.rect = self.image.get_rect()
                self.rect.center = old_center
 

        def update(self):
            self.rotate()
            self.rect.x = self.rect.x + self.speedx
            self.rect.y = self.rect.y + self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -2 or self.rect.right > WIDTH + 5:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width) #randomize place for same meteorites
                self.rect.y = random.randrange(-100, -40) #y-as punt voor enemy
                self.speedy = random.randrange(2, 6) #randomize speed

    


    #load all game graphics
    background = pygame.image.load(os.path.join(img_folder, "achtergrong1.jpg")).convert()
    background_rect = background.get_rect()
    player_img = pygame.image.load(os.path.join(img_folder, "Naamloos2.ico")).convert()
    meteor_img = pygame.image.load(os.path.join(img_folder, "Naamloos1.ico")).convert()
    #sound_game = pygame.mixer.Sound(path.join(snd_dir, "spaceship.wav"))


    #Game loop
    game_over = False
    game_start = True
    running = True
    while running:
        if game_start:
            show_level3_screen()
            screen.fill(BLACK)
            show_go_screen() #show start  screen
            game_start = False #text will go
            #Sprite: objects that move around. make all update
            all_sprites = pygame.sprite.Group() 
            meteorites = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            #all_sprites.add(meteorites)
            for i in range(8):
                m = Meteorite()
                all_sprites.add(m)
                meteorites.add(m)
            

        if game_over:
                show_next_screen()
                game_over = True


        clock.tick (FPS) #keep loop running at the right speed
        # Process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #first the exit-event
                running = False

        # Update: what need a sprite to do
        all_sprites.update()
   
        # Check if meteor hit the player
        hits = pygame.sprite.spritecollide(player, meteorites, False, pygame.sprite.collide_circle) #boolean tells if it has the get deleted
        if hits:
            #running = False
            game_over = True



        # Draw/render: draw the sprite into the screen
        screen.fill(BLACK)
        #screen.blit(background, background_rect)#old fashioned copy the pixels.
        all_sprites.draw(screen)
        start -= 1
        start1 = start // 100
        score = 5999 - start 
        score1 = score // 100
        draw_text(screen, str(start1), 18, WIDTH / 2, 10)
        draw_text(screen, "score:" + str(score1), 18, 400, 10)
        # Double buffering: after I draw, always do this last.
        pygame.display.flip()
        if start <= 0:
            show_next_screen()
        elif score1 == 60:
            show_win_screen()

        def getscore2():
            return score1

#def getscores:
    #   getscore1()+getscore2()

def level4():
    import pygame
    import sys
    import random
    
    # Initalizes screen, clock and font
    pygame.font.init()
    screen = pygame.display.set_mode((1024, 695))
    clock = pygame.time.Clock()
    
    # Initialize pygame font
    smallFont = pygame.font.Font(None, 25)
    sentenceFont = pygame.font.Font(None, 50)
    bigFont = pygame.font.Font(None, 100)
    mediumFont = pygame.font.Font(None, 75)
    
    class ballSprite(pygame.sprite.Sprite):
        def __init__(self, image, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(image).convert()
            self.position = position
            self.k_left = self.k_right = 0
            # make sure the initial sprite has a rect so the collision detection works
            self.rect = self.image.get_rect()
        def update(self, speed_limitation, collisions, wallSpeed):  
            x, y = self.position
            
            if len(collisions) != 0:
                # if there's something in the collisions list, it's getting hit by a wall
                # The collision detection is a bit slow, so the ball will fall through the platform without this
                bottom = self.rect.bottom - 15
                # if the ball is trying to go out the left side of the screen, push it back. also, since there's a collision,
                # the ball has to be pushed up as well
                if x <= 10:
                    x = 20
                    y -= 3
                if x >= 1014:
                    x = 1004
                    y -= 3
                # if the y value of the bottom of the ball is greater than the y value of the top of the platform
                # this means the ball is INSIDE the platform
                if bottom > collisions[0].rect.top:
                    # the total is equal to the x value of the rightmost part of the ball minus the x value of the leftmost part
                    # of the platform. the absolute value is then taken of the answer
                    total = self.rect.right - collisions[0].rect.left
                    total = abs(total)
                    # when the ball is coming from the right, the absolute value of the difference of the total is large, so
                    if total > 20:
                        # ball coming from the right
                        x += 25
                    else:
                        # ball coming from left
                        x -= 25
                # if the ball is NOT caught inside the platform
                else:
                    # ball gets pushed up with the platform
                    y -= wallSpeed
                    
            elif y >= 740: 
        	    # if the ball gets to the bottom of the screen
                    pass	
            elif x <= 10:
        	    # so the ball can't go off the side of the screen (no y movement because no collision)
                x = 20
            elif x >= 1014:
                x = 994
                
            # gravity    
            else: y += 5
                
            # If the ball reaches the top of the screen, thou loseth
            if y <= 0: gameOver = 1
                
            # if no collisions are happening, and the ball isn't trying to escape off the side of the screen
            else:
                # x is changed depending on whether or not user presses left key or right key
                x += self.k_right
                x -= self.k_left
                self.position = (x, y)
                self.rect.center = self.position
                gameOver = 0
            return gameOver
            
    class wallSprite(pygame.sprite.Sprite):
        def __init__(self, image, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(image).convert()
            self.position = position
            self.rect = self.image.get_rect()
        def update(self, speed_limitation, wallSpeed):
            x, y = self.position
            y -= wallSpeed
            # if wall reaches the top of the screen, kill it
            if y < -40: 
                self = self.kill
            else:
                self.position = (x, y)
                self.rect.center = (self.position)
            
            
    # Adds walls to the screen at random. There are usually 2 gaps in the line of walls, and occasionally 1, 3 or 4      
    def wallAdd():
        gap = random.randint(1,8)
        if gap == 1: wallList = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        elif gap == 2: wallList = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        elif gap == 3: wallList = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        elif gap == 4: wallList = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        else: wallList = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
        random.shuffle(wallList)
        rect = pygame.Rect(0, 0, 85, 1538)
        for x in wallList:
            if x == 1: 
                wall = wallSprite('wall.png', rect.center)
                wall_group.add(wall)
                rect.width += 170
            else: 
                rect.width += 170
    
    # Create the ball, with ball.png as the image for the sprite, and at the top-center of the screen      
    
    def menuScreen(startGame):
        # The Title screen
        if startOver != 1:
            initialize = 1
            
            
            
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN
            if event.key == K_RETURN: 
                startGame = 1 
                initialize = 0
                screen.fill(BLACK)
            if event.key == K_ESCAPE: sys.exit()

        
        title = pygame.font.Font.render(bigFont, "Gravity In Space", 1, (255,255,255), (0,0,0))  
        screen.blit(title, (225,150))
        begin = pygame.font.Font.render(sentenceFont, "Press Enter to begin", 1, (255,255,255), (0,0,0)) 
        screen.blit(begin, (335, 400))
        version = pygame.font.Font.render(smallFont, "Version 1.0", 1, (255,255,255), (0,0,0))  
        screen.blit(version, (450, 650))
        programmer = pygame.font.Font.render(smallFont, "Programmed by Abdullah Sener", 1, (255,255,255), (0,0,0))  
        screen.blit(programmer, (375, 675))
        pygame.display.flip()
            
        return startGame, initialize
    
    def gameOverScreen(score, keypress):
        screen.fill((0,0,0))
        highScoreFile = open("highscore.txt", 'r')
        highScore = highScoreFile.readline()
        highScore = int(highScore)
        startOver = 0
        initialize = 0 
            
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
            if highScore < score:
                highScoreFile.close()
                highScoreFile = open("highscore.txt", 'w')
                scoreString = str(score)
                highScoreFile.write(scoreString)
            down = event.type == KEYDOWN
            if event.key == K_ESCAPE: 
                # This is here because when the user presses ESC to exit the main game, it sends him to this screen
                # The user is sent here faster than they can stop holding the escape key, so unless there's some sort of mechanism
                # in place, then the game is exited as soon as it gets to this screen. The keypress system stops that.
                if keypress > 1: pass
                else: sys.exit()
            if event.key == K_RETURN:
                # To continue the game... 
                startOver = 1
                initialize = 1
    
        # If the player's score beats the recorded high score, display this text
        if highScore < score:
            newScore = pygame.font.Font.render(mediumFont, "New High Score!", 1, (255,255,255), (0,0,0)) 
            screen.blit(newScore, (260,120))
            previousScore = pygame.font.Font.render(sentenceFont, "Previous High Score: %s" %(highScore), 1, (255,255,255), (0,0,0)) 
            screen.blit(previousScore, (260, 185))
        else:
            highScoreDisplay = pygame.font.Font.render(sentenceFont, "High Score: %s" %(highScore), 1, (255,255,255), (0,0,0)) 
            screen.blit(highScoreDisplay, (360, 185))
        yourScore = pygame.font.Font.render(bigFont, "Your score: %i" %(score), 1, (255,255,255), (0,0,0))  
        #returnToExit1 = pygame.font.Font.render(sentenceFont, "Press Enter To Play Again", 1, (255,255,255), (0,0,0))
        #returnToExit2 = pygame.font.Font.render(sentenceFont, "Or Escape If You Do Not Dare HaHa ;D", 1, (255,255,255), (0,0,0))
        screen.blit(yourScore, (275,270))
        pygame.display.flip()
        time.sleep(3)
        screen.fill(BLACK)
        #screen.blit(returnToExit1, (290, 400))
        #screen.blit(returnToExit2, (200, 440))
        show_level5_screen() 
        keypress -= 1
        return keypress, startOver, initialize
        
        
    
    def mainGame(wallNow, score, speedUp, wallTiming, gameOver, escGameOver):
        # Sets Frames per second to x
        fps = 60
        speed_limitation = clock.tick(fps)
        
        for event in pygame.event.get():
            # If the event is not a keypress, don't do anything
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN
            # If right arrow is pressed, make the ball go x spaces right, same thing with left
            if event.key == K_RIGHT: ball.k_right = down * 10
            elif event.key == K_LEFT: ball.k_left = down * 10
            # If ESC pressed, exit game
            elif event.key == K_ESCAPE: escGameOver = 1
                
        # makes it so that the walls appear every x frame
        wallNow += 1 
        if wallNow == wallTiming:
            score +=  10 
            wallAdd()
            rect = pygame.Rect(0, 0, 85, 1538)
        if wallNow == wallTiming * 2:
            score +=  10  
            wallAdd()
            speedUp += 1
            wallNow = 0
               
        # Every x sets of walls, walls are created more quickly  
        if speedUp == 15:
            # So that the walls can't get too crazy
            if wallTiming >= 18: wallTiming -= 2
            else: pass
            speedUp = 0
                
        screen.fill((0,0,0))
            
        # check for collisions, use this variable for more accurate collision checking as well
        collisions = pygame.sprite.spritecollide(ball, wall_group, 0)
        # Gets value for stop from ball.update to prevent the user from moving if caught by platform
        gameOver= ball.update(speed_limitation, collisions, wallSpeed)
        ball_group.draw(screen)
        wall_group.update(speed_limitation, wallSpeed)
        wall_group.draw(screen)
        pygame.display.flip()
        return wallNow, score, speedUp, wallTiming, gameOver, escGameOver
    
    # Make sure the base variables initialize, but doesn't think it has to start over (that comes later)
    initialize = 1
    startOver = 0
    
    while 1:
        if initialize == 1:
            startGame = 0
            
            if startOver == 1:
                ball_group = ball_group.empty()
                wall_group = wall_group.empty()
                screen.fill((0,0,0))
                startGame = 1
                
            origBallPos = pygame.Rect(0, 0, 512, 40)
            ball = ballSprite('ball.png', origBallPos.center)
            ball_group = pygame.sprite.RenderPlain(ball)
            
            # Initialize wall group
            wall_group = pygame.sprite.RenderPlain()
            
            # Set up some default variables for the main game loop
            wallNow = 0
            score = 0
            speedUp = 0
            wallSpeed = 5
            gameOver = 0
            escGameOver = 0
            wallTiming = 36
            keypress = 50
                
            startOver = 0
            initialize = 0
                
        if startGame == 0:
            startGame, initialize = menuScreen(startGame)
        
        elif gameOver == 1 or escGameOver == 1: 
            keypress, startOver, initialize = gameOverScreen(score, keypress)
        
        #elif gameOver == 0 and startGame == 1: 
        else:
            wallNow, score, speedUp, wallTiming, gameOver, escGameOver = mainGame(wallNow, score, speedUp, wallTiming, gameOver, escGameOver)

def level5():
    file = 'music/spaceship.wav'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.

    FPS = 15
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    CELLSIZE = 20
    assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
    CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

    #             R    G    B
    WHITE     = (255, 255, 255)
    BLACK     = (  0,   0,   0)
    RED       = (255,   0,   0)
    GREEN     = (  0, 255,   0)
    DARKGREEN = (  0, 155,   0)
    DARKGRAY  = ( 40,  40,  40)
    BGCOLOR = BLACK

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    HEAD = 0 # syntactic sugar: index of the worm's head

    def main():
        global FPSCLOCK, DISPLAYSURF, BASICFONT

        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Space Eater')

        showStartScreen()
        while True:
            runGame()
            showGameOverScreen()


    def runGame():
        # Set a random start point.
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        wormCoords = [{'x': startx,     'y': starty},
                      {'x': startx - 1, 'y': starty},
                      {'x': startx - 2, 'y': starty}]
        direction = RIGHT

        # Start the apple in a random place.
        apple = getRandomLocation()

        while True: # main game loop
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                        direction = LEFT
                    elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                        direction = RIGHT
                    elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                        direction = UP
                    elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                        direction = DOWN
                    elif event.key == K_ESCAPE:
                        terminate()

            # check if the worm has hit itself or the edge
            if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
                return # game over
            for wormBody in wormCoords[1:]:
                if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                    return # game over

            # check if worm has eaten an apply
            if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
                # don't remove worm's tail segment
                apple = getRandomLocation() # set a new apple somewhere
            else:
                del wormCoords[-1] # remove worm's tail segment

            # move the worm by adding a segment in the direction it is moving
            if direction == UP:
                newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
            elif direction == DOWN:
                newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
            elif direction == LEFT:
                newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
            elif direction == RIGHT:
                newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
            wormCoords.insert(0, newHead)
            DISPLAYSURF.fill(BGCOLOR)
            drawGrid()
            drawWorm(wormCoords)
            drawApple(apple)
            drawScore(len(wormCoords) - 3)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def drawPressKeyMsg():
        pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


    def checkForKeyPress():
        if len(pygame.event.get(QUIT)) > 0:
            terminate()

        keyUpEvents = pygame.event.get(KEYUP)
        if len(keyUpEvents) == 0:
            return None
        if keyUpEvents[0].key == K_ESCAPE:
            terminate()
        return keyUpEvents[0].key


    def showStartScreen():
        titleFont = pygame.font.Font('freesansbold.ttf', 100)
        titleSurf1 = titleFont.render('Space Eater', True, WHITE, DARKGREEN)
        titleSurf2 = titleFont.render('Space Eater', True, GREEN)

        degrees1 = 0
        degrees2 = 0
        while True:
            DISPLAYSURF.fill(BGCOLOR)
            rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
            rotatedRect1 = rotatedSurf1.get_rect()
            rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
            DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

            rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
            rotatedRect2 = rotatedSurf2.get_rect()
            rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
            DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

            drawPressKeyMsg()

            if checkForKeyPress():
                pygame.event.get() # clear event queue
                return
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            degrees1 += 3 # rotate by 3 degrees each frame
            degrees2 += 7 # rotate by 7 degrees each frame


    def terminate():
        pygame.quit()
        sys.exit()


    def getRandomLocation():
        return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


    def showGameOverScreen():
        screen.fill(BLACK)
        show_level6_screen()
        gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
        gameSurf = gameOverFont.render('Try', True, RED)
        overSurf = gameOverFont.render('Again ?', True, RED)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, 10)
        overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

        DISPLAYSURF.blit(gameSurf, gameRect)
        DISPLAYSURF.blit(overSurf, overRect)
        drawPressKeyMsg()
        pygame.display.update()
        pygame.time.wait(500)
        checkForKeyPress() # clear out any key presses in the event queue

        while True:
            if checkForKeyPress():
                pygame.event.get() # clear event queue
                return

    def drawScore(score):
        scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 120, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)


    def drawWorm(wormCoords):
        for coord in wormCoords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(DISPLAYSURF, WHITE, wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect)


    def drawApple(coord):
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, WHITE, appleRect)


    def drawGrid():
        for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
        for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


    if __name__ == '__main__':
        main()

def level6():
    import pygame, sys
    import time, os
    from json import load
    from pygame import image
    import pygame.locals
    # Number of frames per second
    # Change this value to speed up or slow down your game
    FPS = 200
    #Global Variables to be used through our program
    WINDOWWIDTH = 600
    WINDOWHEIGHT = 500
    LINETHICKNESS = 10
    PADDLESIZE = 50
    PADDLEOFFSET = 15
    # Set up the colours
    BLACK     = (0  ,0  ,0  )
    WHITE     = (255,255,255)
#Draws the arena the game will be played in. 
    def drawArena():
        DISPLAYSURF.fill((0,0,0))
        #Draw outline of arena
        pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
   


    #Draws the paddle
    def drawPaddle(paddle):
        #Stops paddle moving too low
        if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
                paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
        #Stops paddle moving too high
        elif paddle.top < LINETHICKNESS:
                paddle.top = LINETHICKNESS
        #Draws paddle
        pygame.draw.rect(DISPLAYSURF, WHITE, paddle)


    #draws the ball
    def drawBall(ball):
        pygame.draw.rect(DISPLAYSURF, WHITE, ball)

        #moves the ball returns new position
    def moveBall(ball, ballDirX, ballDirY):
        ball.x += ballDirX
        ball.y += ballDirY
        return ball

    #Checks for a collision with a wall, and 'bounces' ball off it.
    #Returns new direction
    def checkEdgeCollision(ball, ballDirX, ballDirY):
        if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
            ballDirY = ballDirY * -1
        if ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS):
            ballDirX = ballDirX * -1
        return ballDirX, ballDirY

    #Checks is the ball has hit a paddle, and 'bounces' ball off it.     
    def checkHitBall(ball, paddle1, paddle2, ballDirX):
        if ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
            return -1
        elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
            return -1
        else: return 1

    def crash():
        print('You Crashed')

        #Checks to see if a point has been scored returns new score

    def checkPointScored(paddle1, ball, score, ballDirX):
            #1 point for hitting the ball
            if ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
                score += 1
                return score
            else:
                return score
                print("Ta da")
            #return score


    #Artificial Intelligence of computer player 
    def artificialIntelligence(ball, ballDirX, paddle2):
        #If ball is moving away from paddle, center bat
        if ballDirX == -1:
            if paddle2.centery < (WINDOWHEIGHT/2):
                paddle2.y += 1
            elif paddle2.centery > (WINDOWHEIGHT/2):
                paddle2.y -= 1
        # if ball moving towards bat, track its movement. 
        elif ballDirX == 1:
            if paddle2.centery < ball.centery:
                paddle2.y += 1
            else:
                paddle2.y -=1
        return paddle2

    #Displays the current score on the screen
    def displayScore(score):
        resultSurf = BASICFONT.render('Score = %s' %(score), True, WHITE)
        resultRect = resultSurf.get_rect()
        resultRect.topleft = (WINDOWWIDTH - 150, 25)
        DISPLAYSURF.blit(resultSurf, resultRect)

    def text_objects(text, font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

# crash
    def message_display(text):
        largeText = pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((WINDOWWIDTH/2),(WINDOWHEIGHT/2))
        DISPLAYSURF.blit(TextSurf, TextRect)

    def crash():
        message_display('You Crashed')
    


    

#Main function
    def main():
        pygame.init()
        global DISPLAYSURF
        ##Font information
        global BASICFONT, BASICFONTSIZE
        BASICFONTSIZE = 20
        pygame.mixer.init()
        pygame.mixer.music.load("spaceship.wav")
        pygame.mixer.music.load("sound115.wav")

        sound1 = pygame.mixer.Sound("sound115.wav")
        sound2 = pygame.mixer.Sound("spaceship.wav")
    

        BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
        pygame.display.set_caption('Pong')

        #Initiate variable and set starting positions
        #any future changes made within rectangles
        ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
        ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
        playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) /2
        playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) /2
        score = 0

        #Keeps track of ball direction
        ballDirX = -1 ## -1 = left 1 = right
        ballDirY = -1 ## -1 = up 1 = down

        #Creates Rectangles for ball and paddles.
        paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition, LINETHICKNESS,PADDLESIZE)
        paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS,PADDLESIZE)
        ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)
   

        #Draws the starting position of the Arena
        drawArena()
        pygame.mixer.music.play()
        sound2.play(-1)

        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)

  
        currentTime = time.clock()
        game_over = False
   
   
        while not game_over: #main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    paddle1.y = paddle1.y - 1
                if event.key == pygame.K_DOWN:
                    paddle1.y = paddle1.y + 1

            # if score == 5:
            #    game_over = True
            #print("TA DAAAAA")

            
            drawArena()
            drawPaddle(paddle1)
            drawPaddle(paddle2)
            drawBall(ball)

    
            ball = moveBall(ball, ballDirX, ballDirY)
            ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
            score = checkPointScored(paddle1, ball, score, ballDirX)
            ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
            paddle2 = artificialIntelligence (ball, ballDirX, paddle2)
            #draw the background
            displayScore(score)
         
        

        
            if ball.left == LINETHICKNESS and score != 0 and score >= 5:
                #  game_over = True
                    print("YOU LOST")
                    game_over = True
                    crash()
                    pygame.display.update()
                    time.sleep(3)
                    screen.fill(BLACK)
                    show_gameover_screen()

            if ball.left == LINETHICKNESS and score <= 5:
                    sound1.play()
        

            pygame.display.update()
            if(score < 1):
                FPSCLOCK.tick(FPS)
            else:
                FPSCLOCK.tick(FPS + (score*45)) 


    if __name__=='__main__':
            main()

def show_start_screen(): 
        draw_text(screen, "GOIN' RETRO", 44, WIDTH /2 , HEIGHT /4)
        draw_text(screen, "WELCOME", 66, WIDTH /2 , HEIGHT /8)
        #render_multi_line(screen, "\n\n\nWELCOME\n",60, WIDTH , HEIGHT/7) 
        render_multi_line(screen, "\n\n\n\n\n\n\n\n\nHomerun\nBrickbreaker\nMeteorites\nGravityInSpace\nSpaceEater\nPongpong",30, WIDTH , HEIGHT/7)
        draw_text(screen, "Press a key to start the game", 16, WIDTH /2 , HEIGHT /1.25)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #first the exit-event
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    waiting = False
def show_level1_screen(): 
        #draw_text(screen, "Your score was: ", 36, WIDTH/2 , HEIGHT/2)
        render_multi_line(screen, "\n\n\nHOMERUN\nEverytime the player makes a homerun,\n the player gains a point.\nIf the player misses the ball, \n he or she lose one life.\n If the player makes a homerun after a strike,\n lifes will replenish.",25, WIDTH , HEIGHT/7)
        myfont = pygame.font.SysFont("monospace", 15)
        pygame.display.flip()
        waiting = True
        while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        waiting = False
                        level1()
def show_level2_screen(): 
        #draw_text(screen, "Your score was: ", 36, WIDTH/2 , HEIGHT/2)
        render_multi_line(screen, "\n\n\nIf the ball breaks bricks,\nthe player gets scores.\nIf the ball falls down three times,\n the player loses the game.\nThe speller gets scores by\ncalculating the bricks. If the player\n breaks all bricks, the player wins the\ngame and he / she can go\n to a higher level.",25, WIDTH , HEIGHT/7)
        myfont = pygame.font.SysFont("monospace", 15)

        
        pygame.display.flip()
        waiting = True
        while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        waiting = False
                        level2()
def show_level3_screen(): 
        render_multi_line(screen, "\n\n\nMeteorites fall down\nIn this game meteorites will\nfall from the sky, the enemies\nYou are the ball in the\n game, the player\nAs player you have to dodge\n the meteorites to survive.\nIf you touch the\n meteorites you will lose.\nYou will get 60 seconds\n to survive.",25, WIDTH , HEIGHT/7)
        myfont = pygame.font.SysFont("monospace", 15)

        pygame.display.flip()
        waiting = True
        while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        waiting = False
def show_level4_screen(): 
        
        render_multi_line(screen, "\n\n\nThe roof will\nfall descends you\nYou must avoid touching the roof by\nfalling descending than the roof\nBut there\nare just a few openings\nIn order to move towards the openings\npress the right arrow on your\nkeyboard to move to the right\nPress the left arrow on your\nkeyboard to move to the left\nOnce the roof \ntouches you it is game over!",25, WIDTH , HEIGHT/7)
        myfont = pygame.font.SysFont("monospace", 15)

        pygame.display.flip()
        waiting = True
        while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        waiting = False
                        level4()
def show_level5_screen(): 
        #draw_text(screen, "Your score was: ", 36, WIDTH/2 , HEIGHT/2)
        render_multi_line(screen, "\n\n\nSpaceEater\nIn this game you need to keep\neating. While running around\nYou are the snake\nand the blocks make\ngrow!\n Avoid the walls to survive!",25, WIDTH , HEIGHT/7)
        myfont = pygame.font.SysFont("monospace", 15)

# render text
        #label = myfont.render("Some text!", 1, (255,255,0))
        #screen.blit(label, (100, 100))
        #draw_text(screen, "Pongpong: The game happens between you and the computer. 
                        #  "Your ball should hit the paddle on your left side. Becareful!" You have to really hit the middle of the paddle or you get no scores!", 15, WIDTH /2 , HEIGHT /4)
        
        pygame.display.flip()
        waiting = True
        while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        waiting = False
                        level5()
def show_level6_screen(): 
        #draw_text(screen, "Your score was: ", 36, WIDTH/2 , HEIGHT/2)
        render_multi_line(screen, "\n\n\nPONGpong:\nThe game is between\nyou and the computer.\nYour ball should hit\nthe paddle on your left side.\nBecareful!\nYou have to really hit\nthe middle of the paddle\nor you get no scores!\nGet 60 Scores\n and YOU WIN!",25, WIDTH , HEIGHT/7)
        myfont = pygame.font.SysFont("monospace", 15)

# render text
        #label = myfont.render("Some text!", 1, (255,255,0))
        #screen.blit(label, (100, 100))
        #draw_text(screen, "Pongpong: The game happens between you and the computer. 
                        #  "Your ball should hit the paddle on your left side. Becareful!" You have to really hit the middle of the paddle or you get no scores!", 15, WIDTH /2 , HEIGHT /4)
        
        pygame.display.flip()
        waiting = True
        while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        waiting = False
                        level6()

score1 = random.randint(0,3)
score2 = random.randint(45,168)
score3 = random.randint(1,60)
score4 = random.randint(75,550)
score5 = random.randint(0, 25)
score6 = random.randint(3, 5)
totalscore = score2 + score3 + score4 + score5 +score6

def show_gameover_screen(): 
        render_multi_line(screen, "\n\n\nWell done!\nYou've played Goin' Retro\n\n You're total score was:\n "+str(totalscore)+" If you want to play again\nPlease press any key\n on the keyboard.",25, WIDTH , HEIGHT/7)
        myfont = pygame.font.SysFont("monospace", 15)

        pygame.display.flip()
        waiting = True
        while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

#if event.type == pygame.KEYDOWN:
#    waiting = False
#    screen.fill(BLACK)
#    show_start_screen()
#    screen.fill(BLACK)
                        

running = True
#g = Goingretro()

while running:
    #homepage()
    screen.fill(BLACK)
    show_start_screen()
    screen.fill(BLACK)
    show_level1_screen()#TERUGVERANDEREN NAAR 2!
    level1()
    