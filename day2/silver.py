file = open("silver.txt")

def find_invalid_ids(interval: list[str]) -> int:
    invalids = set()
    for id in range(int(interval[0]), int(interval[1])+1):
        is_invalid = check_validity(str(id))
        if is_invalid:
            invalids.add(id)
    print(f"Invalid for this id: {invalids}")
    return sum(invalids)


def check_validity(id: str) -> bool:
    # Get substrings
    id = str(id)

    for i in range(len(id)):
        for j in range(i + 1, len(id) + 1):
            substring = id[i:j]
            if id == substring + substring:                
                return True

for line in file:
    ranges : str = line.split(',')
    sum_of_ids = 0
    for range_text in ranges:
        interval : list[str] = range_text.split("-")

        print(f"First: {interval[0]}, Second: {interval[1]}")
        sum_of_invalid = find_invalid_ids(interval=interval)
        sum_of_ids += sum_of_invalid

    print(sum_of_ids)