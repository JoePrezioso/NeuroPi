import pygame
from python-mindwave-mobile import MindwaveDataPointReader

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("mindwave mobile")

done = False

clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((120,120,120))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
