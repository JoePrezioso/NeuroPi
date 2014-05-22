import random, os, pygame, threading
from python_mindwave_mobile.MindwaveDataPointReader import MindwaveDataPointReader
from pygame.locals import *
from datathread import GetData

#initialize font module
pygame.init()

#May need to use sizes for later calculations
global winX 
winX = 700
global winY 
winY = 500

#Velocity
global xVelocity
xVelocity = 5
global yVelocity
yVelocity = 5

#x and y variables for leaf
global leafX
leafX = 20
global leafY
leafY = 20

size = (winX,winY)

random.seed(100)

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
    img = pygame.image.load(os.path.join('LeafGame', 'assets', fileName))
    img = img.convert_alpha()
    screen.blit(img, (xVal,yVal))
 
#title screen
def titleScreen():
    #load title image
    title = pygame.image.load(os.path.join('LeafGame', 'assets', 'Leaf_Title.jpg'))
    #draw onto screen at top-left corner -- (0,0)
    title = title.convert()
    screen.blit(title, (0,0))
    
    pygame.display.flip()
    
    done = False
    
    #stay at title screen until space bar is pressed
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #check for Keydown event - only calls once
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    done = True
                                        
#code to spawn an apple
def spawnApple():
    yRand = random.randrange(0, (winY - 60))
    loadImage('Apple.png', (winX - 60), yRand)
    
#None of my print statements are printing...
def gameLoop():

    ##needed for game loop
    done = False

    ##Player score will be based on time, so we need a clock
    clock = pygame.time.Clock()
    
    #These variables will determine the leaf's speed and direction
    meditation = 50
    attention = 50
    poor_signal = 100
    
    #Player's Score and velocities
    score = 0
    
    xVelocity = 5
    yVelocity = 5
    leafX = 20
    leafY = 20
    
    leafLift = 1
    leafAccel = 1

    #start the reader
    if __name__ == '__main__':
        mindwaveDataPointReader = MindwaveDataPointReader()
        mindwaveDataPointReader.start('74:E5:43:89:54:2E')

    #start the data thread
    data = GetData(mindwaveDataPointReader)
    data.start()
    #run until done is set to true
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #check for Keydown event - only calls once
            if event.type == pygame.KEYDOWN:
                #break if player presses space
                if event.key == K_SPACE:
                    done = True
            


        #screen fill
        screen.fill((0,100,200))
        #screen.fill((120,120,120))

        #turn the screen red if there's a poor signal
        #screen.fill((200,100,100),(0,600-data.poor_signal*3, 800,data.poor_signal*3))

        #leaf lift and leaf acceleration 
        leafLift = (data.meditation-100)/10.0
        leafAccel = (data.attention-100)/10.0
        
        
        
        #Modify velocities
        xVelocity += leafAccel
        yVelocity += leafLift
        
        #Restrict max/min velocities
        if xVelocity >= 2:
            xVelocity = 2
        if xVelocity <= -2:
            xVelocity = -2
        
        if yVelocity >= 2:
            xVelocity = 2
        if yVelocity <= -2:
            xVelocity = -2
        
        #set values, THEN restrict them *facepalm*
        leafX += attention
        #increase X value by xVelocity
        leafY += meditation
        
        #leafX = leafX/(pygame.time.get_ticks())
        #leafY = leafY/(pygame.time.get_ticks())
        
        #control values by restricting their maximum/minimum
        if leafX >= (winX - 20):
            xVelocity = -2
            leafX = (winX - 20)
        elif leafX <= 0:
            xVelocity = 2
            leafX = 0
        
        if leafY >= winY - 20:
            yVelocity = -2
            leafY = winY - 20
        elif leafY <= 0:
            yVelocity = 2
            leafY = 0
            
        #test creation of the image
        loadImage('Leaf.png', leafX, leafY)
        
        #we can spawn an apple!
        #spawnApple()
        
        #speed (210 to keep you from stopping the leaf) reduced by acceleration     
        leafSpeed = 110 - leafAccel
        #height increased by meditation
        leafHeight = 0 + leafLift

        #add number of milliseconds since last call to score
        score += 1
        #scoreMsg is a string that should make score look prettier.
        scoreMsg = "Score: "
        #Create score font
        scoreFont = pygame.font.Font(None, 30)
        #...and render it! -- not breaking anything, but it's also not displaying anything
        white = (255,255,255)
        #scoreText is what will actually be put onto the screen...ideally
        scoreText = scoreFont.render((scoreMsg + str(score)), 1, white)
        #screen.blit seems to be breaking things
        screen.blit(scoreText, (0,0))

        pygame.display.flip()

        clock.tick(60)
    
        

def main():
    #We will generate objects randomly. So, we must seed.
    random.seed()

    #Title Screen goes here
    titleScreen()
    
    #run the gameLoop
    gameLoop()
   
#Call main()
main()

#end the data thread
data.running = False
data.join()
#quit pygame
pygame.quit()
    
