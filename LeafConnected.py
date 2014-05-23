import random, os, pygame, threading
from python_mindwave_mobile.MindwaveDataPointReader import MindwaveDataPointReader
from pygame.locals import *
from datathread import GetData
from objects import Item

#initialize font module
pygame.init()

#May need to use sizes for later calculations
global winX 
winX = 700
global winY 
winY = 500

size = (winX,winY)

#debug variable
headset = False


random.seed(100)

#make a window
screen = pygame.display.set_mode(size)
#title bar caption
pygame.display.set_caption('Leaf')

#Mouse may be set to false in later versions
pygame.mouse.set_visible(True)    

##Player score will be based on time, so we need a clock
clock = pygame.time.Clock()

#start the reader
if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    if headset:
        mindwaveDataPointReader.start('74:E5:43:89:54:2E')

#file name, x value, and y value for image to be loaded
def loadImage(fileName):
    img = pygame.image.load(os.path.join('LeafGame', 'assets', fileName))
    img = img.convert_alpha()
    return img

#centers on x, y and draws
def draw(image, x, y, size):
    screen.blit(image, (x-size/2, y-size/2))
def draw_item(item):
    draw(item.image, item.x, item.y, item.size)

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
    yRand = random.randrange(0, (winY - apple.size/2))
    apple = Item(loadImage('Apple.png'), (winX - apple.size/2), yRand)
    return apple
    
def gameLoop():


    ##Player score will be based on time, so we need a clock
    clock = pygame.time.Clock()
    
    #Player's Score and velocities
    score = 0
    
    leaf = Item(loadImage('Leaf.png'), winX/2, winY/2)
    apples = []
    xVelocity = 5
    yVelocity = 5
   

    #start the data thread
    data = GetData(mindwaveDataPointReader)
    if headset:
        data.start()

    done = False
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #check for Keydown event - only calls once
            if event.type == pygame.KEYDOWN:
                #break if player presses space
                if event.key == K_SPACE:
                    done = True
            
        if not headset:
            data.meditation+=random.randrange(-1.0,2.0)
            data.attention+=random.randrange(-1.0,2.0)
            data.poor_signal+=random.randrange(-1.0,2.0)
            if data.meditation<0: data.meditation = 90
            if data.attention<0: data.attention = 90
            if data.meditation>100: data.meditation = 10
            if data.attention>100: data.attention = 10
            if data.poor_signal>200: data.poor_signal = 200

        #screen fill
        screen.fill((0,100,200))
        #screen.fill((120,120,120))

        #turn the screen red if there's a poor signal
        screen.fill((200,100,100),(0,500-data.poor_signal*5/2, 800,data.poor_signal*5/2))
        

        
        
        #modify location by a speed determined by these values
        leaf.x += (data.meditation-50)/-25.0
        leaf.y += (data.attention-50)/-25.0
        
        #control values by restricting their maximum/minimum
        if leaf.x >= (winX - 20):
            leaf.x = (winX - 20)
        elif leaf.x <= 0:
            leaf.x = 0
        
        if leaf.y >= winY - 20:
            leaf.y = winY - 20
        elif leaf.y <= 0:
            leaf.y = 0
            
        draw_item(leaf)
        for apple in apples:
            draw_item(apple)
            apple.x-=1
            if apple.x<-apple.size/2:
                apples.remove(apple)
            elif apple.collides(leaf):
                score -= 900
                apples.remove(apple)
        
        #add number of milliseconds since last call to score
        score += 1
        if score%300==0:
            apples+=[spawnApple()]        

        scoreMsg = "Score: "
        #Create score font
        scoreFont = pygame.font.Font(None, 30)
        white = (255,255,255)


        scoreText = scoreFont.render((scoreMsg + str(score) + 
            " m"+str(data.meditation)+
            " a"+str(data.attention)+
            " s"+str(data.poor_signal)), 1, white)
        screen.blit(scoreText, (0,0))

        pygame.display.flip()

        clock.tick(60)

    if headset:
        #end the data thread
        data.running = False
        data.join()
        

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
    
