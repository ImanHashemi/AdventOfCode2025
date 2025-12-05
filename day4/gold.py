import numpy as np

file = open("silver.txt")

# Given an entry, we need to check the following positions:
# [x-1, y+1], [x, y+1] [x+1, y+1],
# [x-1, y], x,y, [x+1, y]
# [x-1, y-1], [x, y-1], [x+1, y-1]


def check_accesible(lists: list[list[str]], index: tuple[int, int]) -> bool:
    counter = 0
    for y_range in [-1,0,1]:
        for x_range in [-1,0,1]:
            print(x_range, y_range)
            if x_range == 0 and y_range == 0:
                print("Passing")
                continue

            x_index = index[0] + x_range
            y_index = index[1] + y_range
            
            if x_index < 0 or y_index < 0:
                continue

            if index[0] == x_index and index[1] == y_index:
                continue
            # Sorry not sorry
            try:
                place = lists[y_index][x_index]
                if place == '@':
                    counter+=1
            except IndexError:
                pass
    
    if counter < 4:
        return True
    
    return False
                
lists = []
for line in file:
    lists.append(list(line.strip('\n')))

print(np.array(lists))

accesible_rolls = 1
removed_rolls = 0
while accesible_rolls > 0:
    accesible_rolls = 0
    for index_v, ver in enumerate(lists):
        for index_h, hor in enumerate(ver):

            if lists[index_v][index_h] == '@':
                if check_accesible(lists=lists, index=(index_h, index_v)):                
                    lists[index_v][index_h] = 'x'
                    accesible_rolls += 1
            
    removed_rolls += accesible_rolls
    
    print(np.array(lists))
    print(f"Removed rolls: {removed_rolls}")

print(f"Final rolls: {removed_rolls}")


