import pygame
import random
from python_mindwave_mobile.MindwaveDataPointReader import MindwaveDataPointReader

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("mindwave mobile")

done = False

clock = pygame.time.Clock()

#if __name__ == '__main__':
#    mindwaveDataPointReader = MindwaveDataPointReader()
#    mindwaveDataPointReader.start()
meditation = 50
attention = 50
poor_signal = 50

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((120,120,120))

    #dataPoint = mindwaveDataPointReader.readNextDataPoint()
    #if (not dataPoint.__class__ is RawDataPoint):
    #    print dataPoint
    meditation+=random.choice([1,0,-1])
    attention+=random.choice([1,0,-1])
    poor_signal+=random.choice([1,0,-1])

    screen.fill((100,200,200),(100,200-meditation*2,100,meditation*2))
    screen.fill((200,200,100),(300,200-attention*2,100,attention*2))
    screen.fill((200,100,100),(500,200-poor_signal,100,poor_signal))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
