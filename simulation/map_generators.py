from simulation.board import Cell
from simulation.weathers import *

class Basic_generator():
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._map = [[Cell(None, Sunny()) for i in range(self._width)] for j in range(self._height)]
    
    def generate_map(self):
        for i in range(self._height):
            for j in range(self._width):
                self._map[i][j].terrain(("grass", 1), 0)
        
        return self._map
