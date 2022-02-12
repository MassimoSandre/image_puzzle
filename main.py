import math
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from pygame.time import Clock
from puzzle import Puzzle

pygame.init()
pygame.font.init()
SIZE = WIDTH, HEIGHT = (1000,1000)

BGCOLOR = (50,50,50)
GFONT = pygame.font.SysFont("Comic Sans MS", 30)
window = pygame.display.set_mode(SIZE,pygame.RESIZABLE)
pygame.display.set_caption('test')
clock = Clock()

p = Puzzle("image.jpg", (653,980),(3,3), (173,10))
p.scramble()

def main():
    w = a = s = d = False
    
    running = True
    while running:
        clock.tick(60)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if p.moves_allowed():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if not w:
                            p.move_up()
                            w = True
                    elif event.key == pygame.K_a:
                        if not a:
                            p.move_left()
                            a = True
                    elif event.key == pygame.K_s:
                        if not s:
                            p.move_down()
                            s = True
                    elif event.key == pygame.K_d:
                        if not d:
                            p.move_right()
                            d = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    w = False
                elif event.key == pygame.K_a:
                    a = False
                elif event.key == pygame.K_s:
                    s = False
                elif event.key == pygame.K_d:
                    d = False

        window.fill(BGCOLOR)

        p.update()
        p.render(window)

        if p.is_solved():
            p.reveal(window)


        pygame.display.update()

if __name__ == '__main__':
    main()
    