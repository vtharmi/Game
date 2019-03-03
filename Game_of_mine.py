import pygame
import time
from random import randint,randrange
yellow = (224,224,102)
white = (255,255,255)
orange = (255, 204, 0)
green_light = (0,45,18)
meroon = (91,18,18)
pink =(214,50,91)
pink2 = (255,102,102)
purple = (100,81,136)
blue = (0,0,102)
color_choices = [orange,green_light,pink,purple,meroon,blue,pink2]

surface_width = 800
surface_height = 500
imageHeight = 60
imageWidth = 80

pygame.init()
surface = pygame.display.set_mode((surface_width,surface_height))
pygame.display.set_caption("Game_of_mine")
clock = pygame.time.Clock()

img = pygame.image.load('download2.jpg')

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score : " + str(count), True, white)
    surface.blit(text, [0,0])

def block(x_block, y_block, block_width, block_height, gap, color_choice):
    pygame.draw.rect(surface, color_choice, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, color_choice, [x_block, y_block+block_height+ gap, block_width, surface_height])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, (128, 43, 0))
    return textSurface, textSurface.get_rect()
    
def game_of_mine(x,y,image):
    surface.blit(img, (x,y))

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    largeText = pygame.font.Font('freesansbold.ttf',80)
		
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surface_width/2,surface_height/2
    surface.blit(titleTextSurf, titleTextRect)
		
    typTextSurf, typTextRect = makeTextObjs("press any key to continue", smallText)
    typTextRect.center = surface_width/2,((surface_height/2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)
    while replay_or_quit() == None:
        clock.tick()
    main()

def gameOver():
    msgSurface('OOPS! game Over')
        
def main():
    x = 150
    y = 200
    y_move = 0
    
    x_block= surface_width
    y_block = 0
    block_width = 60
    block_height = randint(0, (surface_height/2))
    gap = imageHeight * 3 
    block_move = 3

    current_score = 0
    block_color = color_choices[randrange(0,len(color_choices))]
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
        y += y_move
        surface.fill(yellow)
        game_of_mine(x , y, img)
        
        block(x_block,y_block,block_width,block_height,gap,block_color)
        score(current_score)
        x_block -= block_move
        if y>surface_height-40 or y <0:
             gameOver()

        if x_block <(-1*block_width):
            block_color = color_choices[randrange(0,len(color_choices))]
            x_block = surface_width
            block_height = randint(0, (surface_height/2))
            current_score +=1
            

        if x + imageWidth > x_block:
            if x< x_block + block_width:
                print('possible within the boundaries of x ')
                if y< block_height:
                    print('Y crossover UPPER')
                    if x- imageWidth < block_width + x_block:
                        print('Game over upper hit')
                        gameOver()
                        
        if x + imageWidth > x_block:
            print("cross over")
            if y + imageHeight > block_height+ gap:
                print('possible y cross lower')
                if x < block_width + x_block:
                    print('game lower')
                    gameOver()
                    
        if 3<= current_score <5:
            block_move = 5
            gap = imageHeight * 2.8
        if 5<= current_score < 8:
            block_move = 6
            gap = imageHeight * 2.5
        if 8<= current_score <15:
            block_move = 7
            gap = imageHeight * 2.3
        pygame.display.update()
        clock.tick(60)
main()
pygame.quit()
quit()
