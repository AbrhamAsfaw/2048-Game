
# 2048 By Abrham Asfaw ATE_5110_09

import random
import layout as lyt

def merge(line):
    #merge function
    
    n_elements = len(line)
    # Remove 0 entries and slide to the left
    line = [value for value in line if value != 0]
    index = 0
    # Iterate while there are possible pairs
    while index < len(line)-1:
        # If a pair is found, merge
        # and remove second element
        if line[index] == line[index+1]:
            line[index] *= 2
            line.pop(index+1)
        # Move on to next item
        index += 1
    line += [0]*(n_elements-len(line))
    return line


class TwentyFortyEight:
    
    #Class to run the game logic.
    

    def __init__(self, grid_height, grid_width, offsets):
        self._offsets = offsets
        self._height = grid_height
        self._width = grid_width
        self._grid = None
        self.reset()
        self._initial_tiles = {lyt.UP: [(0, col, self._height) for col in range(self._width)],
                               lyt.DOWN: [(-1, col, self._height) for col in range(self._width)],
                               lyt.LEFT: [(row, 0, self._width) for row in range(self._height)],
                               lyt.RIGHT: [(row, -1, self._width) for row in range(self._height)]}

    def reset(self):
        #Reset Function 
        
        self._grid = [[0]*self._width for dummy_i in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):        
        return str(self._grid)

    def get_grid_height(self):
        
        #Get the height of the board.
        
        return self._height

    def get_grid_width(self):
        
        #Get the width of the board.
        
        return self._width

    def move(self, direction):
        
        #Move with a direction and add tile function
        
        
        moved = False
        displacement_vector = list(self._offsets[direction])
        initial_tiles = [list(initial_t) for initial_t in self._initial_tiles[direction]]
        # Get row/col to merge in the correct order
        for tile_pos in initial_tiles:
            to_merge = []
            for dummy_i in range(tile_pos[2]):
                to_merge += [self.get_tile(tile_pos[0], tile_pos[1])]
                tile_pos[0] += displacement_vector[0]
                tile_pos[1] += displacement_vector[1]
            merged = merge(to_merge)
            merged.reverse()
            for index in range(tile_pos[2]):
                tile_pos[0] -= displacement_vector[0]
                tile_pos[1] -= displacement_vector[1]
                if merged[index] != self.get_tile(tile_pos[0], tile_pos[1]):
                    moved = True
                self.set_tile(tile_pos[0], tile_pos[1], merged[index])
        if moved:
            self.new_tile()

    def new_tile(self):
        # Look for empty tiles
        candidate_tiles = []
        for row_index in range(self._height):
            for col_index in range(self._width):
                if self._grid[row_index][col_index] == 0:
                    candidate_tiles += [(row_index, col_index)]
        # Randomly select tile
        if candidate_tiles:
            tile_pos = random.choice(candidate_tiles)
            tile_row, tile_col = tile_pos[0], tile_pos[1]
            # Randomly select value with probs: 2->90%, 4->10%
            tile_value = 2 if random.random() <= 0.9 else 4
            self.set_tile(tile_row, tile_col, tile_value)

    def set_tile(self, row, col, value):
                
        self._grid[row][col] = value

    def get_tile(self, row, col):
        
        #Get tile value at col and row
        
        return self._grid[row][col]

    def get_game_state(self):
        
        #Return game state
        
        return self._grid
