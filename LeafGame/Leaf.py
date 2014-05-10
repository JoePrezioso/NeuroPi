import random, os, pygame
#Need line below to use the mindwave -- commented out for use on other machines
#from python_mindwave_mobile.MindwaveDataPointReader import MindwaveDataPointReader
from pygame.locals import *

#initialize font module
pygame.init()

#May need to use sizes for later calculations
global winX 
winX = 700
global winY 
winY = 500

size = (winX,winY)

#make a window
screen = pygame.display.set_mode(size)
#title bar caption
pygame.display.set_caption('Leaf')

#Mouse may be set to false in later versions
pygame.mouse.set_visible(True)	

##Player score will be based on time, so we need a clock
clock = pygame.time.Clock()

#file name, x value, and y value for image to be loaded
def loadImage(fileName, xVal, yVal):
    img = pygame.image.load(os.path.join('assets', fileName))
    img = img.convert_alpha()
    screen.blit(img, (xVal,yVal))
    
    
#title screen
def titleScreen():
    #load title image
    title = pygame.image.load(os.path.join('assets', 'Leaf_Title.JPG'))
    #draw onto screen at top-left corner -- (0,0)
    title = title.convert()
    screen.blit(title, (0,0))
    
    pygame.display.flip()
    
    done = False
    
    #stay at title screen until space bar is pressed
    while not done:
        for event in pygame.event.get([pygame.KEYDOWN]):
            #check for Keydown event - only calls once
            if event.type == pygame.KEYDOWN:
                #break if player presses space
                if event.key == K_SPACE:
                    done = True
   
#None of my print statements are printing...
def gameLoop():

    ##needed for game loop
    done = False

    ##Player score will be based on time, so we need a clock
    clock = pygame.time.Clock()

    #These variables will determine the leaf's speed and direction
    meditation = 20
    attention = 20
    poor_signal = 50
    
    #Player's Score
    score = 0
    
    #run until done is set to true
    while not done:
        
        for event in pygame.event.get([pygame.KEYDOWN]):
            #check for Keydown event - only calls once
            if event.type == pygame.KEYDOWN:
                #break if player presses space
                if event.key == K_SPACE:
                    done = True
                #increase meditation if up is pressed
                if event.key == K_UP:
                    meditation -= 20
                elif event.key == K_DOWN:
                    meditation += 10
                else:
                    meditation += 5
                #increase attention if left is pressed
                if event.key == K_LEFT:
                    attention -= 20
                elif event.key == K_RIGHT:
                    attention += 10
                else:
                    attention += 2
        
        #screen fill
        screen.fill((0,100,200))
        #screen.fill((120,120,120))

        #dataPoint = mindwaveDataPointReader.readNextDataPoint()
        #if (not dataPoint.__class__ is RawDataPoint):
        #    print dataPoint
        meditation+=random.choice([1,0,-1])
        attention+=random.choice([1,0,-1])
        poor_signal+=random.choice([1,0,-1])

        #leaf lift and leaf acceleration 
        leafLift = meditation*2
        leafAccel = attention*2
        
        #control values by restricting their maximum
        if leafAccel >= (winX - 20):
            leafAccel = (winX - 20)
        
        if leafAccel <= 10:
            leafAccel = 10
        
        if leafLift >= (winY - 20):
            leafLift = (winY - 20)
        if leafLift <= 0:
            leafLift = 0
        
        #test creation of the image
        loadImage('Leaf.png', leafAccel, leafLift)
        
        #'''
        #screen.fill((100,200,200),(100,200-leafLift,100,leafLift))
        #screen.fill((200,200,100),(300,200-leafAccel,100,leafAccel))
        #screen.fill((200,100,100),(500,200-poor_signal,100,poor_signal))
        pygame.display.flip()
        #'''
        
        #speed (210 to keep you from stopping the leaf) reduced by acceleration     
        leafSpeed = 110 - leafAccel
        #height increased by meditation
        leafHeight = 0 + leafLift

        #add number of milliseconds since last call to score
        score += 1
        #Note: Font rendering is not thread safe!
        #(text, anti-alias (boolean), RGB val for color, background=None)
        #pygame.font.Font.render(score, True, (0,255,0))
        #clock ticks
        
        #console print code for testing purposes
        '''        
        s = "Lift: " 
        s += str(leafLift) 
        s += "\nAccel: " 
        s += str(leafAccel)
        s += "\nScore: " 
        s += str(score)
        print(s)
        '''
        
        clock.tick(60)
        
    print("Loop Closed")

def main():
    #We will generate objects randomly. So, we must seed.
    random.seed()

    #Title Screen goes here
    titleScreen()
    
    #run the gameLoop
    gameLoop()
   
#Call main()
main()

#quit pygame
pygame.quit()
	