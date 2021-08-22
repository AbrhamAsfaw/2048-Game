
# 2048 By Abrham Asfaw ATE_5110_09

# Sizes
PADDING = 10
TILE_SIZE = 125

# Colors
BACKGROUND_COLOR = "#708090"
BACKGROUND_COLOR_EMPTY_TILE = "#536878"
BACKGROUND_TILE_COLORS = {2: "#FFFFFF", 4: "#b3f3f2", 8: "#5aace8", 16: "#5cb85c",
                          32: "#008080", 64: "#005370", 128: "#235300", 256: "#dfa926",
                          512: "#23362f", 1024: "#9a3f5c", 2048: "#4d1648"}
TILE_COLORS = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
               32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
               512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
# Fonts
FONT = ("Arial", 35)


### GAME LOGIC CONSTANTS ###

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

