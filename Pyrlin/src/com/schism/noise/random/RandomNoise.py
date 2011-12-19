'''
Created on 18/dic/2011

@author: Christian
'''

import pygame
from random import randint

class RandomNoiseMaker(object):
    '''
        Class that creates images of random generated pixels.
    '''


    def __init__(self, w, h, i):
        '''
        Constructor
        '''
        
        self.width = w
        self.height = h
        self.isColor = i
        
    def render(self):
        
        depth = 24 if self.isColor else 8
        image = pygame.Surface((self.width, self.height), depth)

        for x in range(self.width):
            for y in range(self.height):
                if self.isColor:
                    r = randint(0, 255)
                    g = randint(0, 255)
                    b = randint(0, 255)
                    image.set_at((x,y), (r,g,b))
                else:
                    gray = randint(0,255)
                    image.set_at((x,y), (gray,gray,gray))

        return image
    
if __name__ == "__main__":
    
    width, height = (128, 128)
    
    pygame.init()   
    screen = pygame.display.set_mode((width, height), 0, 24)
    
    rnm = RandomNoiseMaker(width, height, False)
    
    image = pygame.Surface((width, height), 24)
    
    #Clock for framerate
    main_clock = pygame.time.Clock()
    
    while True:
        screen.fill((0, 0, 0))
        image = rnm.render() 
        screen.blit(image, (0,0))
        pygame.display.update()
    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                
        milliseconds_passed = main_clock.tick(30)
        print "Millisecond passed " + str(milliseconds_passed)
    
        