file = open("silver.txt")

total_joltage = 0
for line in file:
    battery = line.strip("\n")
    
    number = ""
    battery_base = list(battery)
    for i in range(1, 12):
        print(f"Index: {i}")
        battery_list = battery_base[:-(12-i)]
        max_deca = max(battery_list)
        max_deca_index = battery_list.index(max_deca)
        
        print(f"Battery list: {battery_list}")
        print(f"Max deca: {max_deca}, its index: {max_deca_index}")
        
        number+=max_deca
    
        # battery_base.pop(max_deca_index)
        battery_base = battery_base[max_deca_index+1:]
        print(f"Popped and adjusted batter base: {battery_base}")
        
    number += max(battery_base)
    print("-----------")    
        
    print(f"Number: {int(number)}")
    total_joltage += int(number)

print(f"Total joltage: {total_joltage}")