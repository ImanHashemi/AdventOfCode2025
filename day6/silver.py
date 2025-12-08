import functools
file = open("silver.txt")

problems = {}
symbols = {}
for line in file:
    split = line.split()
    if line[0] not in ['+', '*']:   
        for index, num in enumerate(split):
            if index in problems.keys():
                problems[index].append(int(num))
            else:
                problems[index] = [int(num)]
    else:
        for index, symbol in enumerate(split):
            symbols[index] = symbol

total = 0
for key, problem in problems.items():
    if symbols[key] == '+':
        answer = functools.reduce(lambda x, y: x+y, problem)
    else:
        answer = functools.reduce(lambda x, y: x*y, problem)
    total += answer
print(total)