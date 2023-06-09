gym = \
''' 
 ____________________
|####################|
|####################|
|        GYM         |
| ###           ###  |
| ###           ###  | 
| ###           ###  |
|________|  |________|'''

house_2 = """
 
 _________/\_
|            |
|   House2   |
|            |
|____|  |____|"""
    
house_1 = """
 __________
|          |
|  House1  |
|          |
|___|  |___|"""
pc = """
 ______________
|##############|  
|##### PC #####| 
|##############|
|              |
|_____|  |_____|"""
pm = """
  __________
 |##########|
 | Pokemart |
 |##########|
 |          |
 |___|  |___|"""
    
tree = ''' 
    ^
   ^^^
  ^^^^^
    |
'''

pond = """
####################
##~~~~~~~~~~~~~~~~##
##~~~~~~~~~~~~~~~~##
##~~~~~~~~~~~~~~~~##
##~~~~~~pond~~~~~~##
##~~~~~~~~~~~~~~~~##
##~~~~~~~~~~~~~~~~##
##~~~~~~~~~~~~~~~~##
####################"""

battle_zone = """
            *************
        *******         *******
     *****                   *****
   ****                         ****
  ***           ______            ***
 ***           /      \            ***
 ***----------| Battle |------------***
 ***          \  Zone  /            ***
 ***           \------/             ***
 ****                             ****
   ****                         ****
     *****                   *****
        *******         *******
            *************"""


logo = """
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|"""

cave = """
|     __    |
\____/  \___/"""
import random

# Define ASCII Art of buildings
buildings = {
    "Gym": gym.split('\n'),
    "Pokemart": pm.split('\n'),
    "Pokemon Center": pc.split('\n'),
    "House 1": house_1.split('\n'),
    "House 2": house_2.split('\n'),
    "Tree": tree.split('/n'),
}    

# Define the grid
grid_height = int(input("How tall do you want your city to be? (Default 40, range(30, 50)) ") or 40)
grid_width = int(input("How wide do you want your city to be? (Default 120, range(70, 200)) ") or 120)

# Validate grid dimensions
assert 30 <= grid_height <= 50
assert 70 <= grid_width <= 200

# Create the grid
grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]
occupied = [[False for _ in range(grid_width)] for _ in range(grid_height)]  # To track occupied spaces


def place_building(name, grid, occupied):
    # Choose building randomly
    building = buildings[name]
    # Calculate the size of the building
    building_height = len(building)
    building_width = max(len(line) for line in building)

    while True:
        # Randomly pick a place for the building
        start_row = random.randint(6, grid_height - building_height - 6)  # Adjust the range for start_row
        start_col = random.randint(6, grid_width - building_width - 6)

        # Check if space is occupied (including a 1-cell border around the building)
        if any(
            occupied[start_row + i][start_col + j] or
            (start_row + i == 0 or start_row + i == grid_height - 1) or
            (start_col + j == 0 or start_col + j == grid_width - 1)
            for i in range(-1, building_height + 1) for j in range(-1, building_width + 1)
        ):
            continue

        # Place the building on the grid
        for i in range(building_height):
            for j in range(len(building[i])):
                grid[start_row + i][start_col + j] = building[i][j]
                occupied[start_row + i][start_col + j] = True

        return start_row, start_col, building_width, building_height


def place_tree(grid, occupied):
    # Calculate the size of the tree
    tree_height = len(tree.split('\n'))
    tree_width = max(len(line) for line in tree.split('\n'))

    while True:
        # Randomly pick a place for the tree
        start_row = random.randint(0, grid_height - tree_height - 1)
        start_col = random.randint(0, grid_width - tree_width - 1)

        # Check if space is occupied (including a 1-cell border around the tree)
        if any(
            occupied[start_row + i][start_col + j] or
            (start_row + i == 0 or start_row + i == grid_height - 1) or
            (start_col + j == 0 or start_col + j == grid_width - 1)
            for i in range(-1, tree_height + 1) for j in range(-1, tree_width + 1)
        ):
            continue

        # Place the tree on the grid
        tree_lines = tree.split('\n')
        for i in range(tree_height):
            for j in range(len(tree_lines[i])):
                if tree_lines[i][j] != ' ':
                    grid[start_row + i][start_col + j] = tree_lines[i][j]
                    occupied[start_row + i][start_col + j] = True

        return start_row, start_col, tree_width, tree_height


def place_pond(grid, occupied):
    # Calculate the size of the pond
    pond_height = len(pond.split('\n'))
    pond_width = max(len(line) for line in pond.split('\n'))

    while True:
        # Randomly pick a place for the pond
        start_row = random.randint(0, grid_height - pond_height - 1)
        start_col = random.randint(0, grid_width - pond_width - 1)

        # Check if space is occupied (including a 1-cell border around the pond)
        if any(
            occupied[start_row + i][start_col + j] or
            (start_row + i == 0 or start_row + i == grid_height - 1) or
            (start_col + j == 0 or start_col + j == grid_width - 1)
            for i in range(-1, pond_height + 1) for j in range(-1, pond_width + 1)
        ):
            continue

        # Place the pond on the grid
        pond_lines = pond.split('\n')
        for i in range(pond_height):
            for j in range(len(pond_lines[i])):
                if pond_lines[i][j] != ' ':
                    grid[start_row + i][start_col + j] = pond_lines[i][j]
                    occupied[start_row + i][start_col + j] = True

        return start_row, start_col, pond_width, pond_height
    
def place_zone(grid, occupied):
    # Calculate the size of the pond
    zone_height = len(battle_zone.split('\n'))
    zone_width = max(len(line) for line in battle_zone.split('\n'))

    while True:
        # Randomly pick a place for the pond
        start_row = random.randint(0, grid_height - zone_height - 1)
        start_col = random.randint(0, grid_width - zone_width - 1)

        # Check if space is occupied (including a 1-cell border around the pond)
        if any(
            occupied[start_row + i][start_col + j] or
            (start_row + i == 0 or start_row + i == grid_height - 1) or
            (start_col + j == 0 or start_col + j == grid_width - 1)
            for i in range(-1, zone_height + 1) for j in range(-1, zone_width + 1)
        ):
            continue

        # Place the pond on the grid
        zone_lines = battle_zone.split('\n')
        for i in range(zone_height):
            for j in range(len(zone_lines[i])):
                if zone_lines[i][j] != ' ':
                    grid[start_row + i][start_col + j] = zone_lines[i][j]
                    occupied[start_row + i][start_col + j] = True

        return start_row, start_col, zone_width, zone_height


def place_cave(grid, occupied):
    # Calculate the size of the cave
    cave_lines = cave.split('\n')
    cave_height = len(cave_lines)
    cave_width = max(len(line) for line in cave_lines)

    # Get all possible start_cols that can accommodate the cave
    possible_start_cols = [i for i in range(0, grid_width - cave_width - 1) if not any(occupied[0][i + j] for j in range(cave_width))]

    # If there are no possible start_cols, return None
    if not possible_start_cols:
        return None

    # Randomly pick a start_col from possible_start_cols
    start_col = random.choice(possible_start_cols)
    start_row = 0

    # Place the cave on the grid
    for i in range(cave_height):
        for j in range(len(cave_lines[i])):
            if cave_lines[i][j] != ' ':
                grid[start_row + i][start_col + j] = cave_lines[i][j]
                occupied[start_row + i][start_col + j] = True

    return start_row, start_col, cave_width, cave_height
    
# Place cave (20% chance of appearing)
#if random.random() < 0.99:
#    place_cave(grid, occupied)
    
# Place battle zone (25% chance of occuring)
if (random.random() * (grid_width/120)) > 0.75:
    place_zone(grid, occupied)   
    
# Place pond (40% chance of appearing)
if random.random() < 0.4:
    place_pond(grid, occupied)

# Place buildings
gy_row, gy_col, gy_wid, gy_hei = place_building("Gym", grid, occupied)
place_building("Pokemart", grid, occupied)
place_building("Pokemon Center", grid, occupied)
for _ in range((grid_height * grid_width) // 950):
    place_building(random.choice(["House 1", "House 2"]), grid, occupied)


# Place trees
num_trees = random.randint(1, 15)
for _ in range(num_trees):
    place_tree(grid, occupied)
    
# Draw border
for i in range(grid_width):
    grid[0][i] = '-'
    grid[grid_height - 1][i] = '-'
for i in range(grid_height):
    grid[i][0] = '|'
    grid[i][grid_width - 1] = '|'

# Add exits
exit_positions = [(0, grid_width // 2), (grid_height - 1, grid_width // 2), (grid_height // 2, 0),
                  (grid_height // 2, grid_width - 1)]
for row, col in exit_positions:
    if row == 0 or row == grid_height - 1:  # top and bottom exits
        for i in range(-3, 4):  # 6 space wide
            grid[row][col + i] = ' '
        grid[row][col] = ' '  # Empty the exit column
    if col == 0 or col == grid_width - 1:  # side exits
        for i in range(-1, 2):  # 3 space tall
            grid[row + i][col] = ' '
        grid[row][col] = ' '  # Empty the exit row

# Add paths
for row, col in exit_positions:
    # Horizontal path
    if row in [0, grid_height - 1]:
        start, end = sorted([col, gy_col + gy_wid // 2])
        for i in range(start, end + 1):
            if grid[row][i] == ' ':
                grid[row][i] = '-'
    # Vertical path
    else:
        start, end = sorted([row, gy_row + gy_hei // 2])
        for i in range(start, end + 1):
            if grid[i][col] == ' ':
                grid[i][col] = '|'               

# Print grid
for row in grid:
    print(''.join(row))
