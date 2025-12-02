def is_invalid_id(n):
    s = str(n)
    length = len(s)

    for sub_len in range(1, length // 2 + 1):
        if length % sub_len != 0:
            continue
        times = length // sub_len
        if times < 2:
            continue
        part = s[:sub_len]
        if part * times == s:
            return True

    return False

def sum_invalid_ids_part2(filename):
    total = 0

    with open(filename, "r") as f:
        line = f.read().strip()

        ranges = line.split(",")

        for r in ranges:
            if "-" not in r:
                continue

            start, end = r.split("-")
            start = int(start)
            end = int(end)

            for num in range(start, end + 1):
                if is_invalid_id(num):
                    total += num

    return total

file_path = "advent-output.txt"
print("Sum of invalid IDs:", sum_invalid_ids_part2(file_path))