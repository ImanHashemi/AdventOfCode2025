file = open("silver.txt")

def intersect(range_1, range_2):
    xmin = int(range_1[0])
    xmax = int(range_1[1])

    ymin = int(range_2[0])
    ymax = int(range_2[1])

    if (xmin < ymin and xmax < ymin) or (xmin > ymax and xmax > ymax):
        return False
    return True
    
def is_contained(range_1, range_2):
    xmin = int(range_1[0])
    xmax = int(range_1[1])

    ymin = int(range_2[0])
    ymax = int(range_2[1])

    if xmin >= ymin and xmax <= ymax:
        return True
    return False

ranges = []
ingredients = []
ingredient_switch = False
for line in file:
    if line == '\n':
        ingredient_switch = True
        continue
    
    if ingredient_switch:
        ingredients.append(line.strip('\n'))
    else:
        ranges.append(line.strip('\n').split("-"))

def do_run(ranges):
    new_ranges = [ranges[0]]

    ranges.pop(0)
    changed=False
    for ingredient_range in ranges:
        min = int(ingredient_range[0])
        max = int(ingredient_range[1])
        
        add_range = True
        is_contained_bool = False
        for range_index, check_range  in enumerate(new_ranges):
            # print(f"Is {ingredient_range} in {check_range}")


            if is_contained(ingredient_range, check_range):
                add_range = False
                is_contained_bool = True
            elif not intersect(ingredient_range, check_range):
                print(f"{ingredient_range} does not intersects with {check_range}, adding {ingredient_range}")
                add_range = True
            elif int(ingredient_range[0]) < int(check_range[0]):
                new_ranges[range_index][0] = ingredient_range[0]
                add_range = False
                changed = True
                print(f"Updating {new_ranges[range_index]} min with {ingredient_range[0]}")
            elif int(ingredient_range[1]) > int(check_range[1]):
                new_ranges[range_index][1] = ingredient_range[1]
                add_range = False
                changed = True
                print(f"Updating {new_ranges[range_index]} max with {ingredient_range[1]}")
        
        if add_range and not is_contained_bool:
            new_ranges.append([min, max])
        print(new_ranges)

    return (new_ranges, changed)

changed=True
while(changed):
    ranges, changed = do_run(ranges)
    print(f"Running again: {ranges}")

number = 0
for range in ranges:
    print(range)
    number += int(range[1]) - int(range[0]) + 1
print(number)
