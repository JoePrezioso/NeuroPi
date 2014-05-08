import random, os, pygame
#Need line below to use the mindwave -- commented out for use on other machines
#from python_mindwave_mobile.MindwaveDataPointReader import MindwaveDataPointReader

#initialize font module
pygame.init()

#May need to use size for later calculations
size = (700,500)
#player's score
score = 0

#font for score - (filename, size) -- None for filename = pygame default
scoreFont = SysFont(None, 10)

#make a window
screen = pygame.display.set_mode(size)
#title bar caption
pygame.display.set_caption('Leaf')


#Mouse may be set to false in later versions
pygame.mouse.set_visible(True)	

##needed for game loop
done = False

##Player score will be based on time, so we need a clock
clock = pygame.time.Clock()

#These variables will determine the leaf's speed and direction
meditation = 50
attention = 50
poor_signal = 50

#load_image function for title screen
#store assets in their own directory 
#os.path.join creates the complete path to this file
def load_image(file_name):
	full_name = os.path.join('assets', file_name)
	
	image = pygame.image.load(full_name)
	
	image = image.convert()
	
	return image, image.get_rect()



def titleScreen():
    #load title image
    title = load_image("Leaf_Title.jpg")
    #draw onto screen at top-left corner -- (0,0)
    screen.blit(title,(0,0))
   
#Same error every time: IndentationError: unindent does not match any outer indentation level
#There shouldn't be any reason for me to get this error...
#'''
def gameLoop():
    #run until done is set to true
	while not done:

		for event in pygame.event.get():
			#break out of the loop if 'A' is pressed
			if event.key == K_a:
				done = True
	
	screen.fill((120,120,120))

	#dataPoint = mindwaveDataPointReader.readNextDataPoint()
	#if (not dataPoint.__class__ is RawDataPoint):
	#    print dataPoint
	meditation+=random.choice([1,0,-1])
	attention+=random.choice([1,0,-1])
	poor_signal+=random.choice([1,0,-1])

	#leaf lift and leaf acceleration 
	leafLift = meditation*2
	leafAccel = attention*2

	screen.fill((100,200,200),(100,200-leafLift,100,meditation*2))
	screen.fill((200,200,100),(300,200-leafAccel,100,attention*2))
	screen.fill((200,100,100),(500,200-poor_signal,100,poor_signal))
	pygame.display.flip()

	#speed (210 to keep you from stopping the leaf) reduced by acceleration 
	leafSpeed = 210 - leafAccel
	#height increased by meditation
	leafHeight = 0 + leafLift

	#add number of milliseconds since last call to score
	score += clock.get_time()
	#Note: Font rendering is not thread safe!
	#(text, anti-alias (boolean), RGB val for color, background=None)
	pygame.font.Font.render(score, True, (0,255,0))
	#clock ticks
	clock.tick(60)
		
#'''
def main():
	#We will generate objects randomly. So, we must seed.
	random.seed()
    
    #Title Screen goes here
    
    
    #run the gameLoop
    #gameLoop()
   
#Call main()
main()

#quit pygame
pygame.quit()
	