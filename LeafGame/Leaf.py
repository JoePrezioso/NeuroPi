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
					
			keystate = pygame.key.get_pressed()
			#if keystate[K_SPACE]:
			#	done = True
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
	