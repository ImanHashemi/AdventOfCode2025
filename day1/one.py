

file = open("one.txt", "r")

pointer = 50
zeros = 0
for line in file:
    action = line[0]
    count = int(line[1:])
    print(f"{action}, {count}")

    if action == "R":
        pointer = (pointer + count) % 100
        print(pointer)
    else:
        pointer = (pointer - count) % 100
        print(pointer)

    if pointer == 0:
        zeros += 1

print(zeros)