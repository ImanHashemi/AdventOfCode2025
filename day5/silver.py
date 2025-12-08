file = open("silver.txt")

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

print(ranges)
print(ingredients)

counter = 0
for ingredient in ingredients:
    fresh = False
    for range in ranges:
        if int(ingredient) >= int(range[0]) and int(ingredient) <= int(range[1]):
            fresh = True
            print(F"Ingredient {ingredient} is fresh in range {range}")
    if fresh:
        counter+=1


print(counter)