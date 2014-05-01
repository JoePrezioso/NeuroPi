import random, os
import pygame
from pygame.locals import *

pygame.init()

#if __name__ == '__main__': main()

#allow for window make a window
screen = pygame.display.set_mode((640, 480))
#title bar caption
pygame.display.set_caption('Leaf')
titleScreen = pygame.image.load('Leaf_Title.jpg')


#Mouse may be set to false in later versions
pygame.mouse.set_visible(True)	

#load_image function for title screen
#store assets in their own directory 
#os.path.join creates the complete path to this file
def load_image(file_name):
	full_name = os.path.join('assets', file_name)
	
	try:
		image = pygame.image.load(full_name)
	except pygema.error, message:
		print ("This image broke: " + full_name)
		raise SystemExit, message
	
	image = image.convert()
	
	return image, image.get_rect()

#screen.blit(background(0,0))

def gameLoop():

    while(True):
        #Break if the player presses 'A'
        if event.key == K_a:
            break;

def main():
	#We will generate objects randomly. So, we must seed.
	random.seed()
    gameLoop()

   
#Call main()
main()
	