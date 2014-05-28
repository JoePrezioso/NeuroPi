import pygame
import random
import threading
from python_mindwave_mobile.MindwaveDataPointReader import MindwaveDataPointReader
from python_mindwave_mobile.MindwaveDataPoints import *



class GetData( threading.Thread ):

    def __init__(self):
        super(GetData, self).__init__()
        self.meditation = 50
        self.attention = 50
        self.poor_signal = 100
        self.running = False

    def run ( self ):
        self.meditation = 50
        self.attention = 50
        self.poor_signal = 100
        self.running = True

        while self.running:
            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            if (not dataPoint.__class__ is RawDataPoint):
                if dataPoint.__class__ is AttentionDataPoint:
                    self.attention = dataPoint.attentionValue
                if dataPoint.__class__ is MeditationDataPoint:
                    self.meditation = dataPoint.meditationValue
                if dataPoint.__class__ is PoorSignalLevelDataPoint:
                    self.poor_signal = dataPoint.amountOfNoise
                else:
                    pass
                    #print dataPoint




size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("mindwave mobile")

done = False

clock = pygame.time.Clock()

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start('74:E5:43:89:54:2E')
data = GetData()
data.start()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESC:
                done = True
    screen.fill((120,120,120))
    
    #meditation+=random.choice([1,0,-1])
    #attention+=random.choice([1,0,-1])
    #poor_signal+=random.choice([1,0,-1])

    screen.fill((10,10,10),(50,100,600,200))
    screen.fill((200,100,100),(50,300-data.poor_signal,600,data.poor_signal))
    screen.fill((100,200,200),(50,300-data.meditation*2,100,data.meditation*2))
    screen.fill((200,200,100),(200,300-data.attention*2,100,data.attention*2))
    fps = clock.get_fps()#framerate max 60, display height 200
    screen.fill((100,100,200),(600,300-fps*200/60,50,fps*200/60))
    pygame.display.flip()

    clock.tick(60)

data.running = False
data.join()
pygame.quit()

