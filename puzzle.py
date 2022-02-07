import pygame
import random

class Puzzle():
    def __init__(self, image_file_name, puzzle_size, puzzle_dim) -> None:
        loadedimage = pygame.image.load(image_file_name)
        self.image = pygame.Surface(puzzle_dim)

        self.size = puzzle_size

        self.cell_width = puzzle_dim[0]//puzzle_size[0]
        self.cell_height = puzzle_dim[1]//puzzle_size[1]

        self.puzzle = []
        for i in range(puzzle_size[0]):
            self.puzzle.append([])
            for j in range(puzzle_size[1]):
                self.puzzle[i].append((i,j))

        self.void = (puzzle_size[0]-1, puzzle_size[1]-1)
        self.puzzle[self.void[0]][self.void[1]] = (-1,-1)


    def move_up(self, move):
        if self.void[1] < self.size[1]-1:
            temp = self.void
            temp.void = self.puzzle[self.void[0]][self.void[1]+1]
            self.puzzle[self.void[0]][self.void[1]+1] = temp

    def move_down(self, move):
        ...

    def move_left(self, move):
        ...

    def move_right(self, move):
        ...


    def scramble(self):
        pieces = []
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if i != self.size[0]-1 or j != self.size[1]-1:
                    pieces.append((i,j))
        
        pieces.append((-1,-1))

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                x,y = random.choice(pieces)
                pieces.remove((x,y))
                self.puzzle[i][j] = (x,y)
                if (x,y) == (-1,-1):
                    self.void = (i,j)

