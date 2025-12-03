file = open("silver.txt")

total_joltage = 0
for line in file:
    battery = line.strip("\n")
    print(battery[:-1])
    max_deca = max(list(battery[:-1]))
    max_deca_index = list(battery).index(max_deca)
    print(f"Max deca: {max_deca}, its index: {max_deca_index}")
    max_single = max(list(battery[max_deca_index+1:]))
    print(f"Max single: {max_single}")

    max_number = int(max_deca + max_single)
    total_joltage += max_number
    print(f"Max number: {max_number}")

print(f"Total joltage: {total_joltage}")












            