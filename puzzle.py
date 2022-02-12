from matplotlib import animation
import pygame
import random

class Puzzle():
    def __init__(self, image_file_name, puzzle_size) -> None:
        self.loadedimage = pygame.image.load(image_file_name)
        

        self.size = puzzle_size

        #self.cell_width = puzzle_dim[0]//puzzle_size[0]
        #self.cell_height = puzzle_dim[1]//puzzle_size[1]

        self.puzzle = []
        for i in range(puzzle_size[0]):
            self.puzzle.append([])
            for j in range(puzzle_size[1]):
                self.puzzle[i].append((i,j))

        self.void = (puzzle_size[0]-1, puzzle_size[1]-1)
        self.puzzle[self.void[0]][self.void[1]] = (-1,-1)

        self.animating = None
        self.buffer = (0,0)

    def render(self, screen, pos, dim):
        cell_width = dim[0]//self.size[0]
        cell_height = dim[1]//self.size[1]

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.animating == (i,j):
                    screen.blit(self.loadedimage, (pos[0]+i*cell_width + int(self.buffer[0]*cell_width),pos[1]+j*cell_height+int(self.buffer[1]*cell_height)),(self.puzzle[i][j][0]*cell_width,self.puzzle[i][j][1]*cell_height,cell_width, cell_height))
                else:
                    screen.blit(self.loadedimage, (pos[0]+i*cell_width,pos[1]+j*cell_height),(self.puzzle[i][j][0]*cell_width,self.puzzle[i][j][1]*cell_height,cell_width, cell_height))

        if self.animating != None:
            self.__reduce_buffer()
            if self.buffer == (0,0):
                self.animating = None

    def __reduce_buffer(self):
        REDUC = 0.1

        if self.buffer[0] > 0:
            self.buffer = (max(0,self.buffer[0]-REDUC), self.buffer[1])

        if self.buffer[0] < 0:
            self.buffer = (min(0,self.buffer[0]+REDUC), self.buffer[1])

        if self.buffer[1] > 0:
            self.buffer = (self.buffer[0], max(0,self.buffer[1]-REDUC))

        if self.buffer[1] < 0:
            self.buffer = (self.buffer[0], min(0,self.buffer[1]+REDUC))

    def move_up(self, animate=True):
        if self.void[1] < self.size[1]-1:
            self.puzzle[self.void[0]][self.void[1]] = self.puzzle[self.void[0]][self.void[1]+1]
            self.puzzle[self.void[0]][self.void[1]+1] = (-1,-1)
            self.void = (self.void[0],self.void[1]+1)
            if animate:
                self.animating = (self.void[0], self.void[1]-1)
                self.buffer = (0,1)
        

    def move_down(self, animate=True):
        if self.void[1] > 0:
            self.puzzle[self.void[0]][self.void[1]] = self.puzzle[self.void[0]][self.void[1]-1]
            self.puzzle[self.void[0]][self.void[1]-1] = (-1,-1)
            self.void = (self.void[0],self.void[1]-1)
            if animate:
                self.animating = (self.void[0], self.void[1]+1)
                self.buffer = (0,-1)

    def move_left(self, animate=True):
        if self.void[0] < self.size[0]-1:
            self.puzzle[self.void[0]][self.void[1]] = self.puzzle[self.void[0]+1][self.void[1]]
            self.puzzle[self.void[0]+1][self.void[1]] = (-1,-1)
            self.void = (self.void[0]+1,self.void[1])
            if animate:
                self.animating = (self.void[0]-1, self.void[1])
                self.buffer = (1,0)

    def move_right(self, animate=True):
        if self.void[0] > 0:
            self.puzzle[self.void[0]][self.void[1]] = self.puzzle[self.void[0]-1][self.void[1]]
            self.puzzle[self.void[0]-1][self.void[1]] = (-1,-1)
            self.void = (self.void[0]-1,self.void[1])
            if animate:
                self.animating = (self.void[0]+1, self.void[1])
                self.buffer = (-1,0)

    def is_solved(self, animate=True):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.puzzle[i][j] != (-1,-1) and self.puzzle[i][j] != (i,j):
                    return False
        return True

    def scramble(self):
        moves = [self.move_up, self.move_down, self.move_left, self.move_right]

        for i in range(random.randint(self.size[0]*self.size[1]**2, self.size[0]*self.size[1]**3)):
            random.choice(moves)(False)

        # pieces = []
        # for i in range(self.size[0]):
        #     for j in range(self.size[1]):
        #         if i != self.size[0]-1 or j != self.size[1]-1:
        #             pieces.append((i,j))
        
        # pieces.append((-1,-1))

        # for i in range(self.size[0]):
        #     for j in range(self.size[1]):
        #         x,y = random.choice(pieces)
        #         pieces.remove((x,y))
        #         self.puzzle[i][j] = (x,y)
        #         if (x,y) == (-1,-1):
        #             self.void = (i,j)

