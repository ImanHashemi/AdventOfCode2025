

file = open("one.txt", "r")

pointer = 50
zeros = 0
for line in file:
    action = line[0]
    count = int(line[1:])
    print(f"{action}, {count}")
    
    for iter in list(range(count)):
        count = 1
        if action == "R":
            pointer = (pointer + count) % 100
            
        else:
            pointer = (pointer - count) % 100
            

        if pointer == 0:
            zeros += 1
    
    print(f"Pointer: {pointer}")
    print(f"Zero's: {zeros}")

print(zeros)