from tree import Node
import numpy as np

file = open("silver.txt")

grid = []
y = 0
for line in file:
    print(line)
    hor = line.strip('\n')
    grid.append(hor)
    
grid_x = len(grid[0])
grid_y = len(grid)

print(grid_x, grid_y)
print(np.array(grid))

root_x = grid[0].index("S")
root = Node(root_x, 0)
prev_node = root
beams = [root.x]
splits = 0
for y, hor in enumerate(grid[1:]):
    ind_x = [i for i, val in enumerate(hor) if val == "^"]
    nodes = [Node(x, y) for x in ind_x]
    for node in nodes:
        if node.x in beams:
            splits += 1
            ind = beams.index(node.x)
            beams.pop(ind)
            beams.append(node.x-1) if node.x-1 not in beams else None
            beams.append(node.x+1) if node.x+1 not in beams else None
            
    nodes = [[node.x, node.y] for node in nodes]
    
    print(f"Nodes: {nodes}")
    print(f"Beams: {beams}")

print(splits)














