import functools
import pandas as pd
file = open("silver.txt")

problems = {}
symbols = {}
for index, line in enumerate(file):
    split = list(str(line).strip('\n'))
    if line[0] not in ['+', '*']:   
        if index in problems.keys():
            problems[index].append(split)
        else:
            problems[index] = [split]
    else:
        for index, symbol in enumerate(line.split()):
            symbols[index] = symbol

problem_lenght = len(problems[0][0])
df = pd.DataFrame(problems)

rows = {}
index = 0
for i in range(0, problem_lenght):
    all_empty = True
    column = ''
    for col in df.columns:
        char = list(df[col][0][i])
        column += str(char[0])
    
    number_str = column.strip(' ')

    if number_str == '':
        index += 1
    else:
        if index in rows.keys():
            rows[index].append(int(number_str))
        else:
            rows[index] = [int(number_str)]

total = 0
for key, problem in rows.items():
    if symbols[key] == '+':
        answer = functools.reduce(lambda x, y: x+y, problem)
    else:
        answer = functools.reduce(lambda x, y: x*y, problem)
    total += answer
print(total)